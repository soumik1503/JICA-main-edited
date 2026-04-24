from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _
from .models import ContactPluginModel
from .forms import ContactForm


from django.core.mail import send_mail,EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
import logging
import smtplib

logger = logging.getLogger(__name__) 


def send_query_email(data):
    subject = 'New Query Submission'
    from_email = settings.EMAIL_HOST_USER

    bcc_email=[settings.EMAIL_HOST_USER,data['email']]

    html_content = render_to_string('email_template.html', data)
    text_content = 'New query submitted:\n\n' + '\n'.join(f'{key}: {value}' for key, value in data.items())

    try:
        msg = EmailMultiAlternatives(
            subject=subject,
            body=text_content,
            from_email=from_email,
            bcc=bcc_email,
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    except smtplib.SMTPException as e:
        logger.error(f"SMTP error occurred: {e}")
        # or print(f"SMTP error occurred: {e}")
        return False

    except Exception as e:
        logger.error(f"Unexpected error sending email: {e}")
        # or print(f"Unexpected error: {e}")
        return False

    return True



class ContactFormPlugin(CMSPluginBase):
    model = ContactPluginModel
    name = _("Contact Form")
    render_template = "contactplugin/plugin_form.html"
    cache = False

    def render(self, context, instance, placeholder):
        request = context['request']
        form = ContactForm(request.POST or None)

        if request.method == "POST" and form.is_valid():
            form_instance = form.save()

            data = {
                'name': form.cleaned_data['name'],
                'age': form.cleaned_data['age'],
                'gender': form.cleaned_data['gender'],
                'mobile': form.cleaned_data['mobile'],
                'email': form.cleaned_data['email'],
                'aadhar': form.cleaned_data['aadhar'],
                'query': form.cleaned_data['query'],
            }

            if send_query_email(data):
                context.update({
                'instance': instance,
                'form': ContactForm(),
                'success': True,
                'error':False,
                'name': data['name'],
            })
            else:
                form_instance.delete()
                context.update({'success': False,
                'error':True,
                'error_msg': 'Could not send email. Please try later',
                'instance': instance,
                'form': form,}) 
            
        else:
            context.update({
                'instance': instance,
                'form': form,
                'success': False,
                'error':False,
            })

        return context

plugin_pool.register_plugin(ContactFormPlugin)
