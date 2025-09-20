# NLP_LLM – AI Content Generator

A powerful web application that generates high-quality content using AI. Built with Flask and Bootstrap, it provides a modern, responsive experience, ideal for blogs, social media, marketing, and more.

### Features

⚡ AI-Powered Content Generation: Creates engaging and relevant content using AI

⚡ Modern UI: Clean and responsive design with Bootstrap

⚡ Mobile Friendly: Works seamlessly on all devices

⚡ Fast & Lightweight: Quick content generation with minimal dependencies

⚡ Secure: API key management with environment variables

⚡ Content Analytics: Word count, readability, and paragraph statistics

⚡ Copy & Export: Easily copy or download generated content

### Tech Stack

Backend: Flask (Python)

Frontend: HTML5, CSS3, Bootstrap 5

AI: OpenAI GPT / Google Gemini API

Styling: Custom CSS with gradients and animations

Icons: Font Awesome

Prerequisites

Python 3.7 or higher

AI API key (Google Gemini API or OpenAI API key)

#### Installation & Setup
1. Clone or Download the Project
   
Using Git
git clone <repository-url>
cd ai-content-generator

#### Or download and extract the project files

2. Create Virtual Environment (Recommended)
#### Create virtual environment
python -m venv venv

#### Activate virtual environment
Windows:
venv\Scripts\activate
#### macOS/Linux:
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Set Up Environment Variables

Create a .env file in the project root:

#### AI API key
API_KEY=your_actual_api_key_here

#### Flask configuration
FLASK_ENV=development
FLASK_DEBUG=True

5. Run the Application
python Content_generator.py
it Open your browser

### Project Structure

ai-content-generator/

├── Content_generator.py       # Main Python script

├── requirements.txt           # Python dependencies

├── .env                       # Environment variables

├── README.md                  # Project documentation

### Usage

Open the Application: Navigate to http://localhost:5000

Enter a Prompt: Type the topic or idea for content generation

Generate Content: Click the “Generate Content” button

View Results: Read your AI-generated content

Copy or Export: Use buttons to copy or download the content

### Example Prompts

“Write a blog post about the benefits of AI in healthcare”

“Create engaging social media captions for a travel brand”

“Generate SEO-friendly content for a tech startup website”

“Write a product description for a new smartphone”

### API Configuration

Model: Google Gemini Pro or OpenAI GPT

Enhanced Prompting: Automatically optimizes user prompts

Error Handling: Handles API failures and rate limits gracefully

Content Length: Generates 300–1000 word content

### Customization

Styling: Edit static/style.css to change colors, fonts, and layout

Content Generation: Modify generate_content() in app.py to tweak prompts, content length, or style

Flask Routes: Add new routes or database integration for content storage

### Troubleshooting

API Key Error: Check .env file and API key permissions

Module Not Found: Install dependencies and activate virtual environment

Port Already in Use: Change port in app.py or terminate conflicting process

Content Generation Fails: Check internet connection and API quota

### Production Deployment

Set FLASK_ENV=production

Use Gunicorn or another WSGI server

Configure HTTPS and reverse proxy (Nginx recommended)

### Contributing

Fork the repository

Create a feature branch

Make your changes

Submit a pull request

### License

MIT License

### Support

Check troubleshooting section

Review Flask and API documentation

Open an issue in the repository
