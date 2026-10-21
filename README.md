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