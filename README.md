# ACME Project

A Django learning project — multi-app scaffold with a homepage and a birthday feature stub.

---

## Apps

- **pages** — static homepage (`/`)
- **birthday** — birthday form page stub (`/birthday/`)
- **admin** — Django admin at `/admin/`

---

## Tech Stack

| | |
|---|---|
| Language | Python 3 |
| Framework | Django 3.2 |
| Templates | Django templating (base + extends) |
| Database | SQLite3 (default) |

---

## Quick Start

```bash
git clone https://github.com/Shipovmax/acme_project
cd acme_project

python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

cd acme_project
python manage.py migrate
python manage.py runserver
```

---

## Project Structure

```
acme_project/
├── acme_project/       # Django settings and root URLs
├── birthday/           # Birthday app (views, urls, models)
├── pages/              # Static pages app
└── templates/
    ├── base.html
    ├── birthday/
    └── pages/
```

---

## Author

- GitHub: [Shipovmax](https://github.com/Shipovmax)
- Email: shipov.max@icloud.com
