import os
from pathlib import Path
import mimetypes

mimetypes.add_type("text/css", ".css", True)

BASE_DIR=Path(__file__).resolve().parent.parent

# SECURITY WARNING: set a real SECRET_KEY env var in production. The
# fallback below is fine for local development only.
SECRET_KEY=os.environ.get('SECRET_KEY', 'portfolio-dev')

# DEBUG must be OFF in production - set DEBUG=False (or leave unset) in
# your Render/host environment. It only defaults to True for local runs.
DEBUG = True

ALLOWED_HOSTS = [h.strip() for h in os.environ.get('ALLOWED_HOSTS', '*').split(',') if h.strip()]

# Needed for CSRF-protected POST requests (admin login, forms) once the
# site is served over HTTPS behind Render's proxy. Set to your real domain
# with the SAME scheme you actually serve over, e.g. "http://your-app.com"
# or "https://your-app.onrender.com" (comma-separated for multiple).
CSRF_TRUSTED_ORIGINS = [o.strip() for o in os.environ.get('CSRF_TRUSTED_ORIGINS', '').split(',') if o.strip()]
INSTALLED_APPS=['django.contrib.admin','django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles','portfolio']
MIDDLEWARE=['django.middleware.security.SecurityMiddleware','whitenoise.middleware.WhiteNoiseMiddleware','django.contrib.sessions.middleware.SessionMiddleware','django.middleware.common.CommonMiddleware','django.middleware.csrf.CsrfViewMiddleware','django.contrib.auth.middleware.AuthenticationMiddleware','django.contrib.messages.middleware.MessageMiddleware'];ROOT_URLCONF='portfolio_project.urls';TEMPLATES=[{'BACKEND':'django.template.backends.django.DjangoTemplates','DIRS':[BASE_DIR/'templates'],'APP_DIRS':True,'OPTIONS':{'context_processors':['django.template.context_processors.request','django.contrib.auth.context_processors.auth','django.contrib.messages.context_processors.messages']}}]
WSGI_APPLICATION='portfolio_project.wsgi.application';DATABASES={'default':{'ENGINE':'django.db.backends.sqlite3','NAME':BASE_DIR/'db.sqlite3'}}
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
MEDIA_ROOT = BASE_DIR / 'media'

if not DEBUG:
    # Production-only hardening. OFF by default so plain-http deployments
    # (no SSL termination) keep working. Set USE_HTTPS=True in your env
    # once your site is actually served over https to turn these on.
    USE_HTTPS = os.environ.get('USE_HTTPS', 'False').lower() in ('1', 'true', 'yes')
    if USE_HTTPS:
        SECURE_SSL_REDIRECT = True
        SESSION_COOKIE_SECURE = True
        CSRF_COOKIE_SECURE = True
        SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
