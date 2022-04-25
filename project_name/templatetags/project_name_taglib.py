from django.conf import settings
from django import template
from psu_base.classes.Log import Log
from psu_base.templatetags.tag_processing import (
    supporting_functions as support,
    html_generating,
    static_content,
)

register = template.Library()
log = Log()


@register.tag()
def sample_tag():
    """An example"""
    return "Example of a Tag"
