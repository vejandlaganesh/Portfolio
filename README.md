# Ganesh Sharma — AI/ML Portfolio

A modern, AI-powered personal portfolio website built to showcase my projects, technical skills, professional experience, education, certifications, resume, and career journey.

The portfolio includes a custom content management system, AI-powered personal assistant, dynamic project showcase, resume management, career timeline, project comparison, analytics, and a responsive modern UI.

---

## ✨ Features

### 🌐 Public Portfolio

* Modern responsive portfolio design
* Dedicated intro / entry experience
* Floating pill-style navigation
* Interactive hero section
* About Me section
* Dynamic Skills section
* Project showcase
* Experience section
* Education section
* Career Timeline
* Certifications section
* Resume Center
* Contact section
* Mobile-friendly responsive design
* Smooth scrolling and UI animations
* Responsive layouts for desktop, tablet, and mobile

### 🤖 Personal AI Assistant

* AI-powered portfolio assistant
* Ask questions about my:

  * Skills
  * Projects
  * Experience
  * Education
  * Certifications
  * Career journey
  * Technical background
* Powered by Groq
* Server-side API key protection
* Conversation history
* Chat reset functionality
* Rate limiting
* Structured Markdown responses
* Safe response rendering
* Designed to answer using portfolio information without inventing personal details

### 📄 Smart Resume Center

* Centralized resume management
* Multiple resume versions
* Resume categories
* Active/inactive resume management
* Resume viewing
* Resume downloading
* Download tracking
* Legacy resume fallback support
* Admin-controlled resume publishing

### 💼 Project Showcase

Each project can include:

* Project title
* Description
* Technologies
* Project image
* GitHub repository
* Live Demo
* Project details
* Project comparison
* Responsive project layouts
* Image fallback support

Project layouts support alternating visual presentation for a more dynamic portfolio experience.

### ⚖️ Project Comparison

* Compare selected projects
* Compare project information and technologies
* Responsive comparison interface
* Handles empty comparison states
* Works without legacy architecture-node features

### 🕒 Career Timeline

* Education history
* Professional experience
* Projects
* Certifications
* Learning milestones
* Achievements
* Timeline-based presentation
* Responsive desktop and mobile layouts
* Admin-managed timeline entries

### 🏆 Certifications

* Certification cards
* Issuer
* Certification year
* Category
* Credential information
* Responsive card layout

### 🔐 Portfolio CMS

A custom Django-based admin/content management system for managing portfolio content.

The CMS provides management for:

* Dashboard
* Projects
* Skills
* Experience
* Education
* Certifications
* Career Timeline
* Learning Concepts
* Resume Center
* Profile Information
* System Health
* Portfolio publishing

Content can be updated without manually editing portfolio templates.

---

## 🛠️ Technologies

### Backend

* Python
* Django
* SQLite
* Gunicorn

### Frontend

* HTML5
* CSS3
* JavaScript
* Responsive CSS
* Markdown rendering for AI responses

### AI

* Groq API
* AI-powered Personal Portfolio Assistant

### Database

* SQLite
* Django ORM

### Deployment

* Render
* WhiteNoise
* Gunicorn

### Development Tools

* Git
* GitHub
* VS Code

---

## 📂 Portfolio Sections

* **Intro**
* **Home**
* **About**
* **Skills**
* **Projects**
* **Project Comparison**
* **Experience**
* **Education**
* **Career Timeline**
* **Certifications**
* **Resume Center**
* **AI Assistant**
* **Contact**

---

## 🏗️ Project Architecture

```text
portfolio/
│
├── portfolio_project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── portfolio/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── ...
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── project_compare.html
│   ├── ...
│   └── admin/
│
├── static/
│   ├── css/
│   │   └── portfolio.css
│   └── js/
│       └── portfolio.js
│
├── media/
│
├── manage.py
├── requirements.txt
├── build.sh
├── Procfile
└── README.md
```

---

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/vejandlaganesh/portfolio.git
cd portfolio
```

Replace the repository URL with the actual repository URL if different.

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Collect static files

```bash
python manage.py collectstatic --noinput
```

### 7. Start the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## 🔐 Environment Variables

For production, configure the required environment variables.

```text
SECRET_KEY=your-production-secret-key
DEBUG=False
ALLOWED_HOSTS=your-domain.com
CSRF_TRUSTED_ORIGINS=https://your-domain.com
GROQ_API_KEY=your-groq-api-key
GROQ_MODEL=your-groq-model
PORTFOLIO_ADMIN_CODE=your-admin-code
```

Do not commit `.env` files, API keys, passwords, or other secrets to GitHub.

---

## ☁️ Deployment

The portfolio is configured for deployment as a Django web application.

### Build

```bash
./build.sh
```

The build process handles the required production preparation such as dependency installation, static file collection, and database migrations.

### Start

```bash
gunicorn portfolio_project.wsgi:application --log-file -
```

The project uses:

* Gunicorn for the production application server
* WhiteNoise for static files
* Environment variables for production configuration
* Render for hosting

---

## 🔒 Security

The application follows production-oriented security practices including:

* Environment-based secret configuration
* Server-side Groq API key handling
* CSRF protection
* Session-based authentication
* Admin authentication
* Rate limiting for AI requests
* Safe Markdown rendering
* Sanitized AI-generated HTML
* `.env` excluded from Git
* No API keys exposed in frontend JavaScript
* Production `DEBUG=False`

---

## 📱 Responsive Design

The portfolio is designed for:

* Desktop
* Laptop
* Tablet
* Mobile

The UI adapts navigation, project cards, timelines, certifications, resume content, contact sections, and the AI Assistant for smaller screens.

---

## 🧪 Deployment Readiness

Before deployment, the project can be validated using:

```bash
python manage.py check
python manage.py check --deploy
python manage.py makemigrations --check --dry-run
python manage.py migrate --plan
python manage.py collectstatic --noinput
```

The production configuration is designed to work with the existing Render deployment.

---

## 👨‍💻 About

### Ganesh Sharma

**AI/ML | Generative AI | Full Stack Development | QA Automation**

B.Tech Computer Science & Engineering graduate specializing in Artificial Intelligence and Machine Learning, with interests in Generative AI, software development, automation, and building intelligent digital experiences.

### Connect With Me

📧 **Email:** [ganeshvejandla@gmail.com](mailto:ganeshvejandla@gmail.com)

🔗 **LinkedIn:** linkedin.com/in/vejandla-ganesh

💻 **GitHub:** github.com/vejandlaganesh

---

## 📌 Current Focus

* Artificial Intelligence & Machine Learning
* Generative AI
* Full Stack Development
* AI-powered applications
* QA Automation
* Intelligent developer tools
* Building practical software products

---

## 📄 License

This portfolio is a personal project and its content, branding, profile information, and original assets belong to Ganesh Sharma.

---

© Ganesh Sharma. All rights reserved.
