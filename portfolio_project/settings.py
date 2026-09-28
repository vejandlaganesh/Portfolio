import os
from pathlib import Path
import mimetypes

mimetypes.add_type("text/css", ".css", True)

BASE_DIR=Path(__file__).resolve().parent.parent

# DEBUG must be OFF in production - set DEBUG=False (or leave unset) in
# your Render/host environment. It only defaults to True for local runs.
# Render sets RENDER=true automatically, so a forgotten DEBUG variable there now means
# "off" instead of "on". Local runs (no RENDER variable) still default to on.
DEBUG = os.environ.get("DEBUG", "False" if os.environ.get("RENDER") else "True").lower() in ("1", "true", "yes")

# SECURITY WARNING: set a real SECRET_KEY env var in production. The
# fallback below is fine for local development only.
# Accept either name: DJANGO_SECRET_KEY (what this project always read) or
# SECRET_KEY (what QA_REPORT.md told you to set on Render).
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY") or os.environ.get("SECRET_KEY") or "portfolio-dev"

if not DEBUG and SECRET_KEY == "portfolio-dev":
    raise RuntimeError(
        "Set DJANGO_SECRET_KEY (or SECRET_KEY) in production."
    )

ALLOWED_HOSTS = [h.strip() for h in os.environ.get('ALLOWED_HOSTS', '*').split(',') if h.strip()]

# Needed for CSRF-protected POST requests (admin login, forms) once the
# site is served over HTTPS behind Render's proxy. Set to your real domain
# with the SAME scheme you actually serve over, e.g. "http://your-app.com"
# or "https://your-app.onrender.com" (comma-separated for multiple).
CSRF_TRUSTED_ORIGINS = [o.strip() for o in os.environ.get('CSRF_TRUSTED_ORIGINS', '').split(',') if o.strip()]
INSTALLED_APPS=['django.contrib.admin','django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles','portfolio']
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'portfolio_project.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
WSGI_APPLICATION='portfolio_project.wsgi.application';DATABASES={'default':{'ENGINE':'django.db.backends.sqlite3','NAME':Path(os.environ.get('SQLITE_PATH', BASE_DIR/'db.sqlite3'))}}
LANGUAGE_CODE='en-us';TIME_ZONE='Asia/Kolkata';USE_I18N=True;USE_TZ=True
STATIC_URL='/static/'
STATICFILES_DIRS=[BASE_DIR/'static']
STATIC_ROOT=BASE_DIR/'staticfiles'

# WhiteNoise: serve compressed, cache-busted static files in production.
STORAGES = {
    "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
    "staticfiles": {"BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage"},
}

DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'

# SECURITY WARNING: change this via the PORTFOLIO_ADMIN_CODE env var before
# deploying - anyone who knows this code can reach /portfolio-admin/<code>/.
# The 'dundi' fallback below is a placeholder for local dev only.
PORTFOLIO_ADMIN_CODE=os.environ.get('PORTFOLIO_ADMIN_CODE', 'dundi')

MEDIA_URL = '/media/'
# On hosts with an ephemeral disk (e.g. Render free tier) uploads and the SQLite file are
# wiped on every deploy. Point these at a persistent disk to keep them, e.g.
#   SQLITE_PATH=/var/data/db.sqlite3   MEDIA_ROOT=/var/data/media
MEDIA_ROOT = Path(os.environ.get('MEDIA_ROOT', BASE_DIR / 'media'))

SECURE_SSL_REDIRECT = os.environ.get(
    "SECURE_SSL_REDIRECT",
    "False" if DEBUG else "True"
).lower() in ("1", "true", "yes")

SESSION_COOKIE_SECURE = os.environ.get(
    "SESSION_COOKIE_SECURE",
    "False" if DEBUG else "True"
).lower() in ("1", "true", "yes")

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

CSRF_COOKIE_SECURE = os.environ.get(
    "CSRF_COOKIE_SECURE",
    "False" if DEBUG else "True"
).lower() in ("1", "true", "yes")

SECURE_HSTS_SECONDS = int(
    os.environ.get(
        "SECURE_HSTS_SECONDS",
        "0" if DEBUG else "31536000"
    )
)

SECURE_HSTS_INCLUDE_SUBDOMAINS = os.environ.get(
    "SECURE_HSTS_INCLUDE_SUBDOMAINS",
    "False" if DEBUG else "True"
).lower() in ("1", "true", "yes")

SECURE_HSTS_PRELOAD = os.environ.get(
    "SECURE_HSTS_PRELOAD",
    "False"
).lower() in ("1", "true", "yes")

# Behind Render's HTTPS proxy Django must trust X-Forwarded-Proto even when the SSL
# redirect is switched off; otherwise the admin login POST fails CSRF with a 403.
if SECURE_SSL_REDIRECT or not DEBUG:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
