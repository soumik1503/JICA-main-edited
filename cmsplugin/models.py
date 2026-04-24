from django.db import models
from cms.models.pluginmodel import CMSPlugin
from tinymce.models import HTMLField
from django.utils.html import strip_tags
from django.utils.text import Truncator

class TinyMCEPluginModel(CMSPlugin):
    content = HTMLField()

    def __str__(self):
        text = strip_tags(self.content or '')
        return Truncator(text).chars(75, truncate='...') or "TinyMCE Editor Plugin"
