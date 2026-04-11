# CLAUDE.md

This file provides guidance to Claude Code when working with this project.

## Commands

```bash
make install                # uv sync — install all dependencies
make run                    # runserver on 0.0.0.0:8000
make build                  # docker-compose build
make lint                   # ruff check
make fix-lint               # ruff check --fix + ruff format
make worker                 # dramatiq worker (default queue)
make createadmin            # create superuser admin/admin
make remove-all-migrations  # delete all migration files

pytest                      # run all tests (--reuse-db enabled)
pytest path/to/test.py::TestClass::test_method  # single test
```

## Project Structure

```
{{cookiecutter.project_slug}}/          # project root
├── config/                             # Django configuration (not an app)
│   ├── settings/
│   │   ├── base.py                     # env, INSTALLED_APPS, MIDDLEWARE
│   │   ├── common/                     # database, caches, logging, security, static, i18n
│   │   ├── vendors/                    # DRF, SimpleJWT, CORS, Spectacular, Debug Toolbar, Dramatiq
│   │   └── {{cookiecutter.project_slug}}/  # project-specific overrides
│   ├── urls.py
│   └── wsgi.py
│
├── {{cookiecutter.project_slug}}/      # all application code lives here
│   ├── apps/                           # all Django apps (both foundational and business)
│   │   ├── users/                      # custom User model + admin
│   │   └── authx/                      # JWT auth with custom UserJWTAuthentication
│   ├── common/                         # shared utilities (not a Django app)
│   │   ├── exception_handler.py        # DRF exception handler → {code, detail}
│   │   ├── filters.py                  # custom django-filter backends
│   │   ├── models.py                   # TimeStampedModel base class
│   │   ├── pagination.py               # StandardPagination (24/page), LargePagination (1000/page)
│   │   └── throttling.py               # Cloudflare-aware rate throttling
│   ├── templates/
│   └── tests/
│
├── env/                                # environment files (local.env, staging.env)
├── docker-compose.yml
├── Dockerfile
└── pyproject.toml
```

## Settings System

Settings are imported in order by `config/settings/__init__.py`:
1. `base.py` — env loading (via `STAGE` env var → `env/{stage}.env`), apps, middleware
2. `common/` — database, caches, logging, security, static/media, i18n
3. `vendors/` — third-party config
4. `{{cookiecutter.project_slug}}/` — project-specific overrides

## Conventions

### Adding a New App

1. Create the app under `{{cookiecutter.project_slug}}/apps/<app_name>/`
2. Set `name = '{{cookiecutter.project_slug}}.apps.<app_name>'` in `apps.py`
3. Add to `INSTALLED_APPS` in `config/settings/base.py`
4. Add URL pattern in `config/urls.py` under `v1/` prefix

### Exceptions

- Custom exceptions belong in the **app that owns the business logic**: `apps/orders/exceptions.py`, not in `common/`
- Only truly cross-app exceptions go in `common/exceptions.py` (file, not directory)
- The global exception handler at `common/exception_handler.py` normalizes all DRF responses to `{"code": "...", "detail": "..."}`

### Models

- Inherit from `common.models.TimeStampedModel` for `created_at`/`modified_at` fields
- Use Django ORM, avoid raw SQL

### URLs

- All API endpoints are versioned under `v1/`
- Pattern: `path('v1/<app_name>/', include(...))`

### API Responses

- JSON-only rendering (no browsable API)
- `AllowAny` default permissions — override per-view as needed
- `django-filter` as default filter backend
- Always raise DRF `APIException` subclasses for errors — never return `Response(status=4xx)` directly. The global exception handler normalizes all exceptions to `{"code": "...", "detail": "..."}`

### Testing

- **App tests** go in `apps/<app>/tests/` — keep tests next to the code they test
- **Shared test infrastructure** lives in `{{cookiecutter.project_slug}}/tests/` — fixtures, helpers, base classes only
- Use `ExtAPIClient` from `tests/test_helpers.py` for API tests
- `tests/conftest.py` provides shared fixtures: `create_user`, `api_client`, `django_mixer`

### Linting

- Ruff for both linting and formatting (line-length: 120)
- Run `make lint` to check, `make fix-lint` to auto-fix
