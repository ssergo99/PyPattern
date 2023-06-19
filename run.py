from wsgiref.simple_server import make_server

from Framework.main import Framework
from urls import routes, frontcontrol

app = Framework(routes, frontcontrol)

with make_server('', 8000, app) as simplsrv:
    print("Сервер запущен. Порт: 8000")
    simplsrv.serve_forever()
