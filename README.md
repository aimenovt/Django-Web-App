# Django Demo Project

A modern Django web application built with best practices.

## Features

- Django 5.0.1
- Environment-based configuration
- Modern, responsive UI
- Static files handling with WhiteNoise
- Secure settings management

## Setup Instructions

1. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create environment file:**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and set your `SECRET_KEY` and `DEBUG` settings.

5. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (optional):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

8. **Visit the application:**
   Open your browser and go to `http://127.0.0.1:8000/`

## Project Structure

```
DjangoExample/
├── config/              # Project configuration
│   ├── settings/       # Settings modules (development, production)
│   ├── urls.py         # Main URL configuration
│   └── wsgi.py         # WSGI configuration
├── core/               # Main application
│   ├── views.py
│   ├── urls.py
│   └── templates/
├── manage.py
├── requirements.txt
└── README.md
```

## Best Practices Implemented

- ✅ Separated settings for development and production
- ✅ Environment variables for sensitive data
- ✅ Static files handling
- ✅ Clean project structure
- ✅ Git ignore file
- ✅ Modern, responsive UI
