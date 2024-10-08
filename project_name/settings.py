"""
Django settings for {{ project_name }} project.

For more information on this file, see
https://docs.djangoproject.com/en/{{ docs_version }}/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/
"""
import os
from django.contrib.messages import constants as messages
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from pathlib import Path

# -------------------------------------------------------------------------
# Application Metadata
# -------------------------------------------------------------------------

# App identifiers
APP_CODE = "{{ project_name }}".upper()  # Used for database lookups
APP_NAME = "The {{ project_name }} Site"  # Displayed in some generic UI scenarios

# On-premises apps will have additional "context" appended to the URL
#   i.e. https://app.banner.pdx.edu/{{ project_name }}/index
# AWS apps will not have this (set to None)
URL_CONTEXT = None  # for on-premises, use: "{{ project_name }}"

# When no local_settings.py file exists, assume running in AWS
is_aws = not os.path.isfile("{{ project_name }}/local_settings.py")

# I needed this in APC, but it caused issues in the demo site.
# APPEND_SLASH = False

# -------------------------------------------------------------------------
# -------------------------------------------------------------------------

# Build paths inside the project like this: BASE_DIR / "subdir".
BASE_DIR = Path(__file__).resolve().parent.parent

# For local development, Finti responses can be stored in SQLite for simulated Finti calls
# Override these in local_settings.py
FINTI_SAVE_RESPONSES = False            # Save/record actual Finti responses for offline use?
FINTI_SIMULATE_CALLS = False            # Simulate Finti calls. 404 if response not previously saved.
FINTI_SIMULATE_WHEN_POSSIBLE = False    # Simulate Finti calls only when cached response exists.

# SECURITY WARNING: Overwrite this key in local_settings.py for production!
SECRET_KEY = "{{ secret_key }}"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # PSU Base Plugin:
    "django_cas_ng",
    "crequest",
    "psu_base",
    "sass_processor",
    # This app:
    "{{ project_name }}",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "{{ project_name }}.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["{{ project_name }}/templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "psu_base.context_processors.auth",
                "psu_base.context_processors.util",
            ],
            "libraries": {
                "{{ project_name }}_taglib": "{{ project_name }}.templatetags.{{ project_name }}_taglib",
            },
        },
    },
]

WSGI_APPLICATION = "{{ project_name }}.wsgi.application"

# Database
# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#databases
if is_aws:
    # AWS Database
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ.get("RDS_DB_NAME", "eb"),
            "USER": os.environ.get("RDS_USERNAME"),
            "PASSWORD": os.environ.get("RDS_PASSWORD"),
            "HOST": os.environ.get("RDS_HOSTNAME"),
            "PORT": os.environ.get("RDS_PORT"),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        },
    }

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# For caching things (like database results)
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "127.0.0.1:11211",
    }
}

# SESSION_ENGINE = "django.contrib.sessions.backends.cache"

# Password validation
# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/{{ docs_version }}/topics/i18n/
LANGUAGE_CODE = "en-us"
TIME_ZONE = "America/Vancouver"
USE_I18N = True
USE_L10N = True
USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/{{ docs_version }}/howto/static-files/
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# SASS (https://github.com/jrief/django-sass-processor)
SASS_PROCESSOR_ROOT = os.path.join(BASE_DIR, "sass_build")
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "sass_processor.finders.CssFinder",
]

SASS_PROCESSOR_INCLUDE_DIRS = [
    os.path.join("{{ project_name }}", "static", "css"),
]
SASS_PROCESSOR_AUTO_INCLUDE = (
    True  # App specific static folders are added to the libsass include dirs
)
SASS_PROCESSOR_INCLUDE_FILE_PATTERN = r"^.+\.scss$"
SASS_PRECISION = 8

SASS_PROCESSOR_CUSTOM_FUNCTIONS = {
    "get-color": "psu_base.services.template_service.get_sass_color",
    "get-string": "psu_base.services.template_service.get_sass_string",
}

# #########################################################################
# PSU Base Plugin Settings
# #########################################################################

# PSU Centralized Repository
CENTRALIZED_NONPROD = "https://content.oit.pdx.edu/nonprod"
CENTRALIZED_PROD = "https://content.oit.pdx.edu"

ICON_PROVIDER = "BOOTSTRAP_ICONS"  # "FONT_AWESOME"

# Message classes
MESSAGE_TAGS = {
    messages.DEBUG: "alert-info",
    messages.INFO: "alert-info",
    messages.SUCCESS: "alert-success",
    messages.WARNING: "alert-warning",
    messages.ERROR: "alert-danger",
}
FLASH_MESSAGE_POSITION = "BOTTOM"  # TOP, BOTTOM

if (not is_aws) and (not os.path.isdir("logs")):
    os.mkdir("logs")

# Logging Settings
if is_aws:
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": True,
        "formatters": {
            "standard": {
                "format": "[%(asctime)s] %(levelname)s %(message)s",
                "datefmt": "%d/%b/%Y %H:%M:%S",
            },
        },
        "handlers": {
            "null": {
                "level": "DEBUG",
                "class": "logging.NullHandler",
            },
            "console": {
                "level": "DEBUG",
                "class": "logging.StreamHandler",
                "formatter": "standard",
            },
        },
        "loggers": {
            "django": {
                "handlers": ["console"],
                "propagate": True,
                "level": "WARN",
            },
            "django.db.backends": {
                "handlers": ["console"],
                "level": "ERROR",
                "propagate": False,
            },
            "psu": {
                "handlers": ["console"],
                "level": "DEBUG",
            },
        },
    }
else:
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": True,
        "formatters": {
            "standard": {
                "format": "[%(asctime)s] %(levelname)s %(message)s",
                "datefmt": "%d/%b/%Y %H:%M:%S",
            },
        },
        "handlers": {
            "null": {
                "level": "DEBUG",
                "class": "logging.NullHandler",
            },
            "console": {
                "level": "DEBUG",
                "class": "logging.StreamHandler",
                "formatter": "standard",
            },
            "file": {
                "level": "DEBUG",
                "class": "logging.FileHandler",
                "filename": "logs/{{ project_name }}.log",
                "formatter": "standard",
            },
        },
        "loggers": {
            "django": {
                "handlers": ["console", "file"],
                "propagate": True,
                "level": "WARN",
            },
            "django.db.backends": {
                "handlers": ["console", "file"],
                "level": "ERROR",
                "propagate": False,
            },
            "psu": {
                "handlers": ["console", "file"],
                "level": "DEBUG",
            },
        },
    }

# SSO SETTINGS
CAS_APPLY_ATTRIBUTES_TO_USER = True
CAS_CREATE_USER = True
CAS_IGNORE_REFERER = True
CAS_LOGIN_MSG = None
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "django_cas_ng.backends.CASBackend",
)

# EMAIL SETTINGS
EMAIL_HOST = "mailhost.pdx.edu"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = None  # Add to local_settings.py
EMAIL_HOST_PASSWORD = None  # Add to local_settings.py
EMAIL_SENDER = "noreply@pdx.edu"

# Session expiration
SESSION_COOKIE_AGE = 30 * 60  # 30 minutes

# Globally require authentication by default
REQUIRE_LOGIN = True

# List of URLs in your app that should be excluded from global authentication requirement
# By default, the root (landing page) is public
APP_PUBLIC_URLS = ["^/$"]

# If deployed on-prem, root URL will contain additional context:
if URL_CONTEXT:
    APP_PUBLIC_URLS.append(f"^/{URL_CONTEXT}/?$")

# CAS will return users to the root of the application
CAS_REDIRECT_URL = f"/{URL_CONTEXT if URL_CONTEXT else ''}"
LOGIN_URL = "cas:login"

# May be overwritten in local_settings (i.e. to use sso.stage):
CAS_SERVER_URL = "https://sso.oit.pdx.edu/idp/profile/cas/login"

# Get SASS Variables
if os.path.isfile("{{ project_name }}/sass_variables.py"):
    from .sass_variables import *

# In AWS (Elastic Beanstalk), values will be in environment variables
if is_aws:

    # If this is not actually an AWS instance, print an error message (but continue)
    if "us-west" not in str(os.environ.get('HOSTNAME')):
        print("\nERROR: Missing local_settings.py\n")

    HOST_NAME = os.environ.get("HOST_NAME", "localhost")
    HOST_IP = os.environ.get("HOST_IP")
    HOST_URL = os.environ.get("HOST_URL")

    # This forces the CAS redirect to use SSL. Required when deployed in AWS.
    CAS_ROOT_PROXIED_AS = f"https://{HOST_URL}"

    # Do not attempt to compile SASS in AWS (permission errors)
    SASS_PROCESSOR_ENABLED = False

    # https://docs.djangoproject.com/en/2.2/topics/security/#ssl-https
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

    # https://docs.djangoproject.com/en/2.2/ref/middleware/#http-strict-transport-security
    SECURE_HSTS_SECONDS = 31536000  # One Year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True

    ALLOWED_HOSTS = ["*", "localhost", HOST_NAME, HOST_IP, HOST_URL]
    ENVIRONMENT = os.environ.get("ENVIRONMENT", "DEV")
    CAS_SERVER_URL = os.environ.get(
        "CAS_SERVER_URL", "https://sso-stage.oit.pdx.edu/idp/profile/cas/login"
    )
    DEBUG = str(os.environ.get("DEBUG", "False")).lower() == "true"
    SECRET_KEY = os.environ.get("SECRET_KEY", "{{ secret_key }}")
    FINTI_URL = os.environ.get("FINTI_URL", "https://sf-stage.oit.pdx.edu")
    FINTI_TOKEN = os.environ.get("FINTI_TOKEN", None)

    # Email Settings
    EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", None)
    EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", None)

    # Sentry log and performance monitoring
    USE_SENTRY = str(os.environ.get("USE_SENTRY", "True")).lower() == "true"
    if USE_SENTRY:
        # Limit performance logging on health-check endpoints
        # ----------------------------------------------------------------------
        def traces_sampler(sampling_context):
            exclusions = ["/psu/test", "/scheduler/run"]
            if URL_CONTEXT:
                exclusions = [f"/{URL_CONTEXT}{ep}" for ep in exclusions]

            default_rate = float(
                os.environ.get(
                    "SENTRY_SAMPLE_RATE", 0.1 if ENVIRONMENT == "PROD" else 0.0
                )
            )
            chosen_rate = default_rate
            try:
                if sampling_context and sampling_context["parent_sampled"] is not None:
                    return sampling_context["parent_sampled"]

                path_info = sampling_context["wsgi_environ"].get(
                    "PATH_INFO") if "wsgi_environ" in sampling_context else None
                if path_info:
                    chosen_rate = 0 if path_info in exclusions else default_rate
            except Exception as ee:
                print(f"Sampling context error: {ee}")

            return chosen_rate
        # ----------------------------------------------------------------------

        # Prevent [POSTED] log messages from creating issues in Sentry
        # ----------------------------------------------------------------------
        def ignore_posted_messages(event, hint):
            ignore = logged_msg = browser = None

            # Get the log message that caused this event
            if "log_record" in hint and hasattr(hint["log_record"], "msg"):
                logged_msg = hint["log_record"].msg
            if (
                (not logged_msg)
                and "logentry" in event
                and "message" in event["logentry"]
            ):
                logged_msg = event["logentry"]["message"]

            # Get the browser (was this an AWS health check?)
            if (
                "request" in event
                and "headers" in event["request"]
                and "User-Agent" in event["request"]["headers"]
            ):
                browser = event["request"]["headers"]["User-Agent"]
            is_health_check = browser and "ELB-HealthChecker" in browser

            # Ignore POSTED errors (i.e. "You forgot to enter this required field...")
            ignore = logged_msg and ("[POSTED]" in logged_msg or "[DUPLICATE]" in logged_msg)

            return None if ignore else event

        # ----------------------------------------------------------------------

        # To which project should data be sent
        psu_base_dsn = "https://ddc37feb8671440a81c31c9e3eea4b36@o50547.ingest.sentry.io/5553836"
        SENTRY_DSN = os.environ.get("SENTRY_DSN", psu_base_dsn)

        # Determine environment name
        if SENTRY_DSN == psu_base_dsn:
            # Using generic project, include app code in environment
            sentry_env = f"{APP_CODE}-{ENVIRONMENT}".lower()
        else:
            # Using app-specific project, so app code not needed
            sentry_env = ENVIRONMENT.lower()

        # Default Sampling Rate
        default_sample_rate = 0.01 if ENVIRONMENT == "PROD" else 0.0
        default_sample_rate = 0.0

        sentry_sdk.init(
            environment=sentry_env,
            dsn=SENTRY_DSN,
            integrations=[DjangoIntegration()],
            traces_sample_rate=float(os.environ.get("SENTRY_SAMPLE_RATE", default_sample_rate)),
            before_send=ignore_posted_messages,
            # If you wish to associate users to errors you may enable sending PII data.
            send_default_pii=str(os.environ.get("SENTRY_PII", "True")).lower() == "true"
        )

# Otherwise, override settings with values from local_settings.py
else:
    from .local_settings import *
