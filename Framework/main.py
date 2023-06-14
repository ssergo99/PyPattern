
class Page404:
    def __call__(self, request):
        return '404 WHAT', 'PAGE 404. Wrong Address'


class Framework:

    def __init__(self, urls, front_cont):
        self.urls_lst = urls
        self.frcontr_lst = front_cont

    def __call__(self, environ, st_response):
        url_path = environ['PATH_INFO']
        if not url_path.endswith('/'):
            url_path = f'{url_path}/'
        if url_path in self.urls_lst:
            view = self.urls_lst[url_path]
        else:
            view = Page404()
        req = {}
        for front in self.frcontr_lst:
            front(req)
        head, body = view(req)
        st_response(head, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]
