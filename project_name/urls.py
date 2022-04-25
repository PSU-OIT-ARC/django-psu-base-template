from django.contrib import admin
from django.conf import settings
from django.conf.urls import url
from django.views.generic import RedirectView
from django.urls import path, include

# After creating a views module or file, include this:
# import {{ project_name }}.views as {{ project_name }}_views
# and remove this:
import psu_base.views as psu_views

app_patterns = [
    # Django admin site. Probably won't use this. Our apps typically use Banner security classes.
    # Finti's sso_proxy app has JWT-specific permission endpoints that could be modified for service-to-service calls
    path("admin/", admin.site.urls),
    # PSU and CAS views are defined in psu_base app
    url("psu/", include(("psu_base.urls", "psu_base"), namespace="psu")),
    url("accounts/", include(("psu_base.urls", "psu_base"), namespace="cas")),
    # Example of a path in the new app's views module
    # (not created by default because you could use a single file, or a module)
    # path('', {{ project_name }}_views.index),
    # Since no views exist yet, display the status page (temporarily)
    path("", psu_views.test_status),
]

# On-prem apps will have additional URL context
if settings.URL_CONTEXT:
    urlpatterns = [
        path("", RedirectView.as_view(url="/" + settings.URL_CONTEXT)),
        url(settings.URL_CONTEXT + "/", include(app_patterns)),
    ]

# AWS apps will NOT have additional URL context
else:
    urlpatterns = app_patterns
