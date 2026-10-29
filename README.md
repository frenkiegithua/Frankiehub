# Frankiehub

A Django-powered personal technical portfolio and knowledge base covering
Django, networking, and cybersecurity. Built sprint by sprint using Scrum.

## Setup

```bash
git clone git@github.com:frenkiegithua/Frankiehub.git
cd Frankiehub
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Edit `.env` and set a real `SECRET_KEY`. Generate one with:

```bash
python -c "from django.core.management.utils import get_random_secret_key as g; print(g())"
```

Set `DEBUG=True` in `.env` for local development (the default is off).

## Run

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/

## Test

```bash
python manage.py test
```

## Status

Sprint 1: project foundation and homepage.

## First-time setup (after cloning)

1. Copy `.env.example` to `.env` and fill in `SECRET_KEY`. Set `DEBUG=True` for local work.
2. Run `python manage.py migrate`.
3. Run `python manage.py createsuperuser` and choose a strong password.
4. Run `python manage.py runserver` and log in at `/admin/`.

## Security notes

- `ALLOWED_HOSTS` is read from `.env` as a comma-separated list.
- When `DEBUG` is False, secure cookies and the HTTPS redirect are enabled automatically.
- `SECURE_HSTS_SECONDS` (check W004) is deliberately not set yet. Set it only once a real HTTPS host exists, starting with a small value.