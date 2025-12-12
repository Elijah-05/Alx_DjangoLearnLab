from .settings import *

DEBUG = False

ALLOWED_HOSTS = ["your-domain.com", "your-server-ip", "your-heroku-app.herokuapp.com"]

# Security
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True  # If HTTPS is enabled

# Static files
STATIC_ROOT = BASE_DIR / "staticfiles"

# Example PostgreSQL setup
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": os.environ.get("DB_HOST"),
        "PORT": "5432",
    }
}

SECRET_KEY = os.environ.get("SECRET_KEY")
