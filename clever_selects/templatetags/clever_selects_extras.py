import logging

from django import template
from django.middleware.csrf import get_token
from django.conf import settings
from django.utils.safestring import mark_safe
from django.templatetags.static import static

from clever_selects import VERSION

register = template.Library()

log = logging.getLogger('clever_selects')


@register.simple_tag(takes_context=True)
def clever_selects_js_import(context, csrf=True):
    """ Return the js script tag for the clever-selects.js file.
    If the csrf argument is present and it's ``nocsrf`` clever-selects will not
    try to mark the request as if it need the csrf token. By default use
    the clever_selects_js_import template tag will make django set the csrftoken
    cookie on the current request."""

    csrf = csrf != 'nocsrf'
    request = context.get('request')

    if request and csrf:
        get_token(request)
    elif csrf:
        log.warning("The 'request' object must be accessible within the context. "
                    "You must add 'django.contrib.messages.context_processors.request' "
                    "to your TEMPLATE_CONTEXT_PROCESSORS and render your views using a RequestContext.")

    url = static('js/clever-selects.js')
    return mark_safe('<script src="%s?v=%s" type="text/javascript" charset="utf-8"></script>' % (url,  VERSION))
