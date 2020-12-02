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
# REQUIRED: Finti URL and Token (uncomment these):
# FINTI_TOKEN = '<< put your Finti token here >>'
# FINTI_URL = 'https://ws-dev.oit.pdx.edu'

# Finti URLs (for reference)
# -  http://localhost:8888
# -  https://ws-dev.oit.pdx.edu
# -  https://ws-stage.oit.pdx.edu
# -  https://ws.oit.pdx.edu

# As-of psu-base 0.11.0, Finti responses can be cached for offline development
# FINTI_SIMULATE_CALLS = False          # Simulate Finti calls; Never use real Finti
# FINTI_SIMULATE_WHEN_POSSIBLE = False  # Use cached calls when possible, call Finti when not cached
# FINTI_SAVE_RESPONSES = False          # Save/record actual Finti responses for offline use?

# Required for sending email:
# EMAIL_HOST_PASSWORD = '<< put the email password here >>'
# EMAIL_HOST_USER = '<< put the email user here >>'

# -----------------------------------------------------------------------------
# OPTIONAL VALUES
# -----------------------------------------------------------------------------

# You may want to disable elevated developer access while running locally
# ELEVATE_DEVELOPER_ACCESS = False

# You may want to extend session expiration during local development
# SESSION_COOKIE_AGE = 4 * 60 * 60  # 4 hours
