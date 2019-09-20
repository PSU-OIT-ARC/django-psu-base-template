# -----------------------------------------------------------------------------
# REQUIRED VALUES
# -----------------------------------------------------------------------------
# Environment choices: {DEV, TEST, PROD}
ENVIRONMENT = 'DEV'

# SECURITY WARNING: Change this and keep it a secret in production!
SECRET_KEY = '{{ secret_key }}'

# Name of machine running the application
ALLOWED_HOSTS = ['localhost']

# Debug mode (probably only true in DEV)
DEBUG = True

# SSO URL
CAS_SERVER_URL = 'https://sso-stage.oit.pdx.edu/idp/profile/cas/login'

# `````````````````
# FINTI
# `````````````````
# If you have the "PSU Key" file, Finti will be configured to access the test server.
# You MUST provide real Finti URL and token for access to your APIs
# Finti URLs (for reference)
# -  http://localhost:8888
# -  https://ws-test.oit.pdx.edu
# -  https://ws.oit.pdx.edu

# REQUIRED: Finti URL and Token (uncomment these):
# FINTI_TOKEN = '<< put your Finti token here >>'
# FINTI_URL = 'https://ws-test.oit.pdx.edu'


# -----------------------------------------------------------------------------
# OPTIONAL VALUES
# -----------------------------------------------------------------------------

# You may want to disable elevated developer access while running locally
# ELEVATE_DEVELOPER_ACCESS = False

# You may want to extend session expiration during local development
# SESSION_COOKIE_AGE = 4 * 60 * 60  # 4 hours
