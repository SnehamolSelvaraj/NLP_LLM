#!/usr/bin/env python3
"""
AI Content Generator - Standalone Version
Generates different types of content (blogs, essays, posts, stories, summaries).
"""
import google.generativeai as genai # type: ignore

# Directly set the key here
genai.configure(api_key="AIzaSyClohdGxY-c_MVhaD9O7C5ujINYf2IiRto")

import os
import sys
import json
import urllib.request
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler
import webbrowser
import threading
import time

# Configuration
PORT = 5000
API_KEY = "AIzaSyClohdGxY-c_MVhaD9O7C5ujINYf2IiRto"  # Replace with your Gemini API key


class ContentHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            self.serve_index()
        else:
            self.send_error(404)

    def do_POST(self):
        if self.path == '/generate':
            self.handle_generate()
        else:
            self.send_error(404)

    def serve_index(self):
        html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>AI Content Generator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #89f7fe, #66a6ff);
            padding: 40px;
        }
        .container {
            max-width: 800px;
            margin: auto;
            background: white;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0px 4px 20px rgba(0,0,0,0.15);
        }
        h1 {
            text-align: center;
            color: #2c3e50;
        }
        label {
            font-weight: bold;
        }
        textarea, select {
            width: 100%;
            padding: 12px;
            margin: 10px 0 20px 0;
            border: 1px solid #ccc;
            border-radius: 8px;
            font-size: 1rem;
        }
        button {
            background: #3498db;
            color: white;
            border: none;
            padding: 15px;
            width: 100%;
            font-size: 1.1rem;
            border-radius: 8px;
            cursor: pointer;
        }
        button:hover {
            background: #2980b9;
        }
        .result {
            margin-top: 20px;
            padding: 20px;
            background: #f6f9fc;
            border-radius: 10px;
            white-space: pre-wrap;
            line-height: 1.6;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🤖 AI Content Generator</h1>
        <form id="contentForm">
            <label for="type">Choose Content Type:</label>
            <select id="type" name="type" required>
                <option value="blog">Blog Article</option>
                <option value="essay">Essay</option>
                <option value="social">Social Media Post</option>
                <option value="story">Story</option>
                <option value="summary">Summary</option>
            </select>
            
            <label for="prompt">Enter Your Prompt:</label>
            <textarea id="prompt" rows="4" placeholder="E.g., Climate change and its impact on daily life"></textarea>
            
            <button type="submit">Generate Content</button>
        </form>
        <div id="result"></div>
    </div>

    <script>
        document.getElementById('contentForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            const type = document.getElementById('type').value;
            const prompt = document.getElementById('prompt').value;
            const resultDiv = document.getElementById('result');

            resultDiv.innerHTML = '⏳ Generating your content...';

            try {
                const response = await fetch('/generate', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ type, prompt })
                });

                const data = await response.json();
                if (data.success) {
                    resultDiv.innerHTML = '<div class="result">' + data.content + '</div>';
                } else {
                    resultDiv.innerHTML = '<div class="result">❌ Error: ' + data.error + '</div>';
                }
            } catch (err) {
                resultDiv.innerHTML = '<div class="result">❌ ' + err.message + '</div>';
            }
        });
    </script>
</body>
</html>
        """
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html.encode())

    def handle_generate(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode('utf-8'))

        prompt = data.get('prompt', '')
        content_type = data.get('type', 'blog')

        try:
            output = self.generate_content(prompt, content_type)
            response = {'success': True, 'content': output}
        except Exception as e:
            response = {'success': False, 'error': str(e)}

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())

    def generate_content(self, prompt, content_type):
        """Generate content using Gemini API"""

        # Define style instructions
        style_prompts = {
            "blog": "Write a blog article (400-600 words) with headings, engaging introduction, and conclusion.",
            "essay": "Write a well-structured essay (500 words) with arguments, evidence, and conclusion.",
            "social": "Write a short, catchy social media post (50-100 words) with emojis and hashtags.",
            "story": "Write a creative short story (300-500 words) with characters, plot, and ending.",
            "summary": "Summarize the following topic in 150 words, clear and concise."
        }

        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={API_KEY}"
        data = {
            "contents": [{
                "parts": [{
                    "text": f"{style_prompts.get(content_type, 'Write content')}\n\nTopic: {prompt}\n\n"
                }]
            }]
        }

        req = urllib.request.Request(url, json.dumps(data).encode('utf-8'))
        req.add_header('Content-Type', 'application/json')

        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))

        if 'candidates' in result and len(result['candidates']) > 0:
            return result['candidates'][0]['content']['parts'][0]['text']
        else:
            return f"⚠️ Could not generate {content_type}. Try again."


def start_server():
    server = HTTPServer(('localhost', PORT), ContentHandler)
    print(f"🚀 AI Content Generator running at http://localhost:{PORT}")
    server.serve_forever()


def main():
    if not API_KEY or API_KEY == "your_api_key_here":
        print("❌ Please set your Gemini API key.")
        return

    threading.Thread(target=start_server, daemon=True).start()
    time.sleep(1)
    webbrowser.open(f"http://localhost:{PORT}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("👋 Server stopped.")


if __name__ == "__main__":
    main()
