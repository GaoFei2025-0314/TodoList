# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Chinese-language (zh-CN) todo list web app built with Flask, SQLAlchemy, and jQuery. Server-rendered with Jinja2 templates, enhanced with client-side AJAX for CRUD operations.

## Tech Stack

- **Backend**: Flask 2.3.3, Flask-SQLAlchemy 3.0.5, Flask-CORS 4.0.0
- **Database**: SQLite (stored at `instance/todos.db`, auto-created on first run)
- **Frontend**: Jinja2 templates, Bootstrap 5.3, jQuery 3.6 (CDN-loaded)
- **Language**: Python 3.11+

## Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run dev server (http://127.0.0.1:5000)
python app.py
```

No test framework, linter, or formatter is configured.

## Architecture

Single-module Flask app with two files:

- `app.py` — All routes. Dual interface: server-side form routes (`/add`, `/toggle/<id>`, `/delete/<id>`) and a JSON API (`/api/todos` CRUD). The form routes redirect back to index; the API routes return JSON and are used by the frontend JS.
- `database.py` — SQLAlchemy model (`Todo`) and db instance. The model has `save()`/`delete()` instance methods, but the routes in `app.py` use `db.session` directly instead.
- `templates/index.html` — Single page. Server-renders the initial todo list via Jinja2, then all subsequent interactions (add, toggle, delete) go through `/api/todos` endpoints via jQuery AJAX.
- `static/style.css` — Minimal custom styles on top of Bootstrap.

## Quirks

- The jQuery AJAX `$.post` sends form-encoded data, but the `/api/todos POST` handler reads `request.get_json()` — this means client-side "add todo" silently fails. To fix, the AJAX call needs `contentType: 'application/json'` and `JSON.stringify`.
- The server-side form routes (`/add`, `/toggle`, `/delete`) are unused by the frontend JS but still functional via direct HTTP requests.
- `Todo.save()` and `Todo.delete()` methods exist on the model but are never called.
- Debug `print()` statements are present throughout `app.py`.
