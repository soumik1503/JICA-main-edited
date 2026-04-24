from waitress import serve
from jicasite.wsgi import application # Replace 'jicasite' with your project name
import os
if __name__ == '__main__':
    host = os.environ.get('WAITRESS_HOST', '127.0.0.1')
    print(f"Serving on http://{host}:8002")
    serve(application, host=host, port=8002, threads=6)