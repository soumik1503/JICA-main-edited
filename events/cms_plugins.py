# events/cms_plugins.py
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _
from .models import Event

class EventGalleryPlugin(CMSPluginBase):
    render_template = "events/event_gallery.html"
    cache = False
    name = _("Event Gallery")

    def render(self, context, instance, placeholder):
        context["events"] = Event.objects.all()
        return context

plugin_pool.register_plugin(EventGalleryPlugin)
