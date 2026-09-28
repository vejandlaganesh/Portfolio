# QA Report — Ganesh Portfolio (Django)

**Tested as:** static/code audit (no live Django install/network available in the
review environment — findings below are based on full source review, cross-checking
migrations against `models.py`/templates field-by-field, and Django's documented
`system check` behavior for the components involved).

## Summary

The deployment failure has a clear root cause, plus two more bugs that would have
caused 500 errors immediately after a successful deploy, and several
security/production-readiness gaps. All are fixed in this delivery — see the
"Fixes Applied" section.

---

## 🔴 Critical — breaks the deploy / breaks every page

### 1. Missing `Pillow` dependency (deploy fails at build step)
`models.py` uses `ImageField` (`Portfolio.profile_photo`, `Project.project_image`,
`Certification.cert_image`), which **requires Pillow**. `requirements.txt` only listed
`Django`, `gunicorn`, `whitenoise`.

Django runs system checks automatically on `manage.py migrate`. Without Pillow this
raises:
```
SystemCheckError: System check identified some issues:
ERRORS:
portfolio.Portfolio.profile_photo: (fields.E210) Cannot use ImageField because Pillow is not installed.
```
Since `build.sh` has `set -o errexit` and calls `migrate` right after `collectstatic`,
this aborts the build — **this is almost certainly the exact "error while deploying"
you're seeing.**

### 2. Migrations out of sync with `models.py`
`models.py` and the templates (`home.html`, `admin/form.html`) reference fields that
**don't exist in any migration**:

| Model | In `models.py` / templates | In migration `0001_initial` |
|---|---|---|
| `Portfolio` | `resume`, `profile_photo` | ❌ missing |
| `Project` | `project_image` | ❌ missing |
| `Certification` | `category`, `cert_image`, `cert_file`, `cert_url`, `description` | ❌ missing |
| `Experience` | `start_date`, `end_date`, `is_current` | ❌ missing (migration still has the old `duration` field, which the model no longer defines) |

Only one migration (`0001_initial.py`) exists — it clearly predates several model
changes, and no follow-up migration was ever generated. On a fresh deploy this means
`migrate` builds the **old** schema, and the first real query (e.g. `Portfolio.objects.first()`
on the home page) fails with:
```
django.db.utils.OperationalError: no such column: portfolio_portfolio.profile_photo
```

### 3. `views.py: seed()` passes an invalid field to `Experience.objects.create()`
```python
Experience.objects.create(..., duration='05/2026 — 06/2026', ...)
```
`Experience` no longer has a `duration` field (replaced by `start_date`/`end_date`/
`is_current`). This raises:
```
TypeError: Experience() got an unexpected keyword argument 'duration'
```
`seed()` runs on **every** home-page and admin-login request, so this alone crashes
the site's first load even independent of bug #2.

---

## 🟠 Security — fix before/at deploy

### 4. Hardcoded superuser password in source code
```python
User.objects.create_superuser('V.D.V.G.S', '', '9490360499')
```
The password is a phone number, committed in plaintext to the repo. Anyone with
read access to the code (or the public GitHub repo, if it's public) has admin
credentials.

### 5. Insecure fallback defaults for admin gate & secret key
`PORTFOLIO_ADMIN_CODE` defaults to `'dundi'` and `SECRET_KEY` defaults to
`'portfolio-dev'` if the env vars aren't set. Convenient for local dev, but if
you forget to set these on Render, your "secret" admin URL and Django's
signing key are both the values now sitting in this chat/repo.

### 6. `DEBUG = True` hardcoded
Always-on debug mode in production leaks full stack traces (including local file
paths and settings) to any visitor who triggers a 500 error.

---

## 🟡 Production-readiness (not blockers, but worth knowing)

7. **SQLite + no persistent disk** — `db.sqlite3` is (correctly) gitignored, so
   Render starts with a fresh, empty DB on every deploy. Combined with `seed()`,
   the site self-heals with demo data, but **anything you edit through
   `/portfolio-admin/.../` (uploaded images, edited bios, new projects) will be
   wiped on the next deploy or container restart** unless you attach a persistent
   disk or move to Postgres.
8. No `Procfile` — Render likely has a manually-configured Start Command, but a
   `Procfile` makes the deploy portable/self-documenting.
9. WhiteNoise was configured without `STORAGES`/`STATICFILES_STORAGE`, so static
   files were served uncompressed and without cache-busting hashes.
10. A stray, unused `templates/admin.html` (leftover from an earlier version, not
    referenced by any view) — harmless but confusing.
11. `templates/admin/base.html` linked `admin.css` via a hardcoded `/static/...`
    path instead of the `{% static %}` tag — worked, but inconsistent and bypasses
    the static storage backend.

---

## ✅ Fixes Applied (senior dev pass)

1. Added `Pillow` to `requirements.txt` (pinned all three deps to sane ranges).
2. Added `portfolio/migrations/0002_sync_models.py`, hand-verified field-by-field
   against `models.py` (script-checked, zero mismatches remaining) — adds every
   missing column and drops the retired `Experience.duration` column.
3. Fixed `seed()` in `views.py` to use `start_date`/`end_date`/`is_current` instead
   of the removed `duration` kwarg.
4. Superuser username/email/password now read from `DJANGO_SUPERUSER_USERNAME` /
   `DJANGO_SUPERUSER_EMAIL` / `DJANGO_SUPERUSER_PASSWORD` env vars (with the old
   values kept only as local-dev fallbacks) — **set real values as Render
   environment variables before your next deploy.**
5. `DEBUG` now reads from an env var (defaults to `False`); `ALLOWED_HOSTS` and
   `CSRF_TRUSTED_ORIGINS` are env-configurable.
6. Added production-only hardening (`SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE`,
   `SECURE_PROXY_SSL_HEADER`) gated behind `if not DEBUG`, so local `runserver`
   over plain HTTP is unaffected.
7. Added `STORAGES` with `whitenoise.storage.CompressedManifestStaticFilesStorage`
   for compressed, cache-busted static files (verified both `{% static %}`
   references in templates resolve to real files first, so this can't break
   anything).
8. Added a `Procfile` (`web: gunicorn portfolio_project.wsgi:application`).
9. Removed the stray `templates/admin.html`; switched `admin/base.html` to use
   `{% static %}` for its CSS.

## ⚠️ Action needed on your side before deploying

Set these environment variables in Render's dashboard:
- `SECRET_KEY` — any long random string
- `DEBUG` — leave unset, or `False`
- `PORTFOLIO_ADMIN_CODE` — your own private path segment (not `dundi`)
- `DJANGO_SUPERUSER_USERNAME`, `DJANGO_SUPERUSER_EMAIL`, `DJANGO_SUPERUSER_PASSWORD`
  — your real admin login (not the phone number)
- `ALLOWED_HOSTS` — your Render domain, e.g. `your-app.onrender.com`
- `CSRF_TRUSTED_ORIGINS` — your site's actual URL with its real scheme, e.g.
  `http://your-app.com` (or `https://...` if you have SSL)
- `USE_HTTPS` — leave unset/`False` if serving over plain HTTP; set to `True`
  only once your site actually has SSL, to enable secure cookies + SSL redirect

Locally, if `python manage.py migrate` complains about existing columns on your
old `db.sqlite3`, just delete that file and re-run `migrate` for a clean slate
(it's gitignored, so this never affects the deployed DB).
