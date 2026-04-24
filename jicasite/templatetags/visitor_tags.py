
from django import template
from jicasite.models import VisitorStats

register = template.Library()

@register.simple_tag
def visitor_count():
    stats = VisitorStats.objects.first()
    if stats:
        try:
            return int(stats.count)
        except (ValueError, TypeError):
            return 0
    return 0
