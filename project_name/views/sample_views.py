# Sample View
#
#   Includes a bunch of unused imports
#

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.conf import settings
from psu_base.classes.Log import Log
from psu_base.classes.Finti import Finti
from psu_base.classes.ConvenientDate import ConvenientDate
from psu_base.services import (
    utility_service,
    email_service,
    date_service,
    auth_service,
    message_service,
)
from psu_base.decorators import require_authority, require_authentication


log = Log()


@require_authentication()
def curriculum_summary(request):
    """
    Render a sample index page
    """
    log.trace()
    user = auth_service.get_user()

    return render(request, "index.html", {"user": user})
