from waitress import serve
from jicasite.wsgi import application

serve(application, host='127.0.0.1', port=9000)
