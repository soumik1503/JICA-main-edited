from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _
from .models import TinyMCEPluginModel
from django.forms import ModelForm
from tinymce.widgets import TinyMCE

class TinyMCEPluginForm(ModelForm):
    class Meta:
        model = TinyMCEPluginModel
        fields = ['content']
        widgets = {
            'content': TinyMCE(attrs={'cols': 80, 'rows': 30}),
        }

@plugin_pool.register_plugin  # register the plugin
class TinyMCECMSPlugin(CMSPluginBase):
    model = TinyMCEPluginModel
    name = _("TinyMCE Editor")
    render_template = "cmsplugin/plugin.html"
    form = TinyMCEPluginForm
    cache = False

    class Media:
        css = {
            'all': ('tinymce_admin.css',)
        }
