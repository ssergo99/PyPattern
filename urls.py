from datetime import date
from views import Index, Contacts, Examples, Page


def date_front(request):
    request['date'] = date.today()


def browser_front(request):
    request['browser'] = 'Safari'


frontcontrol = [date_front, browser_front]

routes = {
    '/': Index(),
    '/contactus/': Contacts(),
    '/examples/': Examples(),
    '/page/': Page(),
}