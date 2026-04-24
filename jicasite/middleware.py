from .models import VisitorStats

class PersistentVisitorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if not request.session.get('has_visited'):
            obj, created = VisitorStats.objects.get_or_create(pk=1)
            obj.count += 1
            obj.save()
            request.session['has_visited'] = True

        return response

class CMSToolbarCSPMiddleware:
    """
    Dynamically relaxes CSP for the CMS Toolbar.
    The django-cms toolbar heavily relies on inline scripts and eval without nonces.
    By removing the nonce and adding 'unsafe-inline' and 'unsafe-eval' ONLY when 
    the toolbar is shown, we maintain Strict CSP for public visitors while 
    allowing staff to manage the site.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        toolbar = getattr(request, 'toolbar', None)
        if toolbar and toolbar.show_toolbar:
            if hasattr(request, '_csp_nonce'):
                delattr(request, '_csp_nonce')
            
            update = getattr(response, '_csp_update', {})
            script_srcs = update.get('script-src', [])
            if "'unsafe-inline'" not in script_srcs:
                script_srcs.append("'unsafe-inline'")
            if "'unsafe-eval'" not in script_srcs:
                script_srcs.append("'unsafe-eval'")
            
            update['script-src'] = script_srcs
            response._csp_update = update

        return response
