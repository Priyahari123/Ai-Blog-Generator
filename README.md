# AI Content Generator for Blogs — README

This is a **Django-based AI Content Generator** that uses **Cohere API** to generate blog articles based on a topic.

---

## 📌 Project Overview

* Simple interface to input a blog topic.
* Uses AJAX for smooth user experience (no page reloads).
* Calls Cohere API to generate the article.
* Displays the result instantly on the same page.

---

## 📂 Project Structure

* **views.py** – Handles requests (renders page and processes AJAX calls).
* **utils.py** – Contains function that calls Cohere API and returns generated content.
* **chat.html** – Frontend template with form and result display area.
* **settings.py** – Loads environment variables (Cohere API key, secret key).
* **requirements.txt** – Lists dependencies (Django, Cohere, dotenv).

---

## ⚙ Setup Steps

1. Create and activate virtual environment.
2. Install dependencies from `requirements.txt`.
3. Create `.env` file with Cohere API key and Django secret key.
4. Run migrations and start server with `python manage.py runserver`.
5. Open browser and visit `http://127.0.0.1:8000`.

---

## 🚀 Features

* Generate full blog posts from just a topic.
* Instant result display using AJAX.
* Secure API key handling via environment variables.
* Lightweight and beginner-friendly project.

---

## 📤 Deployment Notes

* Use `.gitignore` to avoid committing `.env` and `venv`.
* Set environment variables securely in production.
* Optionally use Gunicorn + Whitenoise for static file handling.

---

## 🔮 Future Enhancements

* Add tone/length customization options.
* Save generated articles to a database.
* Implement user login to track history.
* Improve formatting of generated articles.

---

This README gives a clear overview of the project without including code, focusing only on what’s important to understand, run, and deploy the app.
