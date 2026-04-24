from django.shortcuts import render
from django.http import HttpResponseNotFound

def access_denied(request):
    """
    Renders a custom 403 Access Denied page.
    """
    return render(request, 'access_denied.html', status=403)

def csrf_failure(request, reason=""):
    """
    Custom CSRF failure view to return a generic 404 instead of a verbose 403.
    """
    return HttpResponseNotFound("<h1>404 Not Found</h1>")

def static_dir_404(request, exception=None):
    """
    Forces a 404 page for specific static directory listings.
    """
    return render(request, '404.html', status=404)


def figs(request):
    """
    Render the FIGS module page.
    """
    return render(request, "figs.html")

