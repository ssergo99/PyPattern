from Framework.templator import render


class Index:
    def __call__(self, request):
        return '200 OK', render('index.html', date=request.get('date', None),
                                browser=request.get('browser', None))


class Contacts:
    def __call__(self, request):
        return '200 OK', render('contact.html', date=request.get('date', None),
                                browser=request.get('browser', None))


class Examples:
    def __call__(self, request):
        return '200 OK', render('examples.html', date=request.get('date', None),
                                browser=request.get('browser', None))


class Page:
    def __call__(self, request):
        return '200 OK', render('page.html', date=request.get('date', None),
                                browser=request.get('browser', None))
