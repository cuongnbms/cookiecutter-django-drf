# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

A **Cookiecutter template** that generates Django + Django REST Framework projects. All generated project code lives under `{{cookiecutter.project_slug}}/`. Template variables use Jinja2 syntax and conditional blocks (e.g., `{% if cookiecutter.use_dramatiq == "y" %}`).

### Template Options (`cookiecutter.json`)

- `use_dramatiq` (y/n) — Dramatiq task queue with Redis
- `use_postgres` (y/n) — PostgreSQL vs SQLite
- `use_whitenoise` (y/n) — Static file serving via WhiteNoise

## Commands (Inside Generated Project)

```bash
make run                    # runserver on 0.0.0.0:8000
make build                  # docker-compose build
make fix-lint               # black --line-length 120 --exclude="migrations"
make worker                 # dramatiq worker (default queue)
make createadmin            # superuser admin/admin
make remove-all-migrations  # delete all migration files

pytest                      # run all tests (--reuse-db enabled)
pytest path/to/test_file.py::TestClass::test_method  # single test

./startapp.sh <app_name>    # scaffold new app + auto-register in settings and urls
```

## Architecture

### Settings System

Settings are split across modules imported in order by `config/settings/__init__.py`:

1. **`base.py`** — env setup, `INSTALLED_APPS`, `MIDDLEWARE`, templates, WSGI
2. **`common/`** — database, caches, logging, security, static/media files, i18n
3. **`vendors/`** — third-party config: REST framework, SimpleJWT, CORS, Spectacular, Debug Toolbar, Dramatiq
4. **`{{cookiecutter.project_slug}}/`** — project-specific overrides

Environment is driven by `STAGE` env var (defaults to `local`), which loads `env/{stage}.env`.

### App Structure

Apps live under `{{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}/`. Two core apps are pre-scaffolded:

- **`core/users`** — custom user model
- **`core/authx`** — JWT authentication with custom `UserJWTAuthentication` class, used as the default DRF auth backend

### Shared Utilities (`common/`)

- **`models.py`** — `TimeStampedModel` (abstract base with `created_at`/`modified_at`), `execute_sql()` helper
- **`exceptions/handler.py`** — custom DRF exception handler returning `{code, detail}` format
- **`pagination.py`** — `StandardPagination` (24/page) and `LargePagination` (1000/page)
- **`throttling.py`** — Cloudflare-aware rate throttling
- **`validation.py`** — shared validators

### URL Convention

URLs are versioned under `v1/`. The `startapp.sh` script auto-appends `path('v1/<app_name>/', ...)` to `config/urls.py`. Sentinel comments `# APPEND_NEW_APP #` and `# APPEND_NEW_URL #` are used by the script — do not remove them.

### API Docs

drf-spectacular provides OpenAPI at `/docs/`, Swagger at `/docs/swagger/`, Redoc at `/docs/redoc/` (gated by `ENABLE_API_DOC` setting).

### DRF Defaults

- JSON-only rendering (no browsable API)
- `AllowAny` default permissions
- `django-filter` as default filter backend
- Custom exception handler with structured `{code, detail}` responses
