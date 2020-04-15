from django import template

register = template.Library()

from ..models import Entry

@register.inclusion_tag('partials/_entry_history.html')
def entry_history():
    entries = Entry.objects.all()[:6]
    return {'entries': entries}
