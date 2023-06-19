import os
import sys
from quopri import decodestring

filename = sys.argv[0]


class Page404:
    def __call__(self, request):
        return '404 WHAT', 'PAGE 404. Wrong Address'


class Framework:

    def __init__(self, urls, front_cont):
        self.urls_lst = urls
        self.frcontr_lst = front_cont

    @staticmethod
    def parsing_params(param_str):
        pars_dict = {}
        if param_str:
            param = param_str.split('&')
            for item in param:
                key, value = item.split('=')
                pars_dict[key] = value
        return pars_dict

    @staticmethod
    def take_post_req(envir):
        content_len = envir.get('CONTENT_LENGTH')
        if content_len:
            content_len = int(content_len)
        else:
            content_len = 0
        res = envir['wsgi.input'].read(content_len) \
            if content_len > 0 else b''
        return res

    @staticmethod
    def decode_value(data):
        new_data = {}
        for k, v in data.items():
            val = bytes(v.replace('%', '=').replace("+", " "), 'UTF-8')
            val_decode_str = decodestring(val).decode('UTF-8')
            new_data[k] = val_decode_str
        return new_data

    @staticmethod
    def parse_post_req(req):
        post_params = {}
        if req:
            req_dec = req.decode(encoding='utf-8')
            post_params = Framework.parsing_params(req_dec)
        return post_params

    def __call__(self, environ, st_response):
        req = {}
        method = environ['REQUEST_METHOD']
        req['method'] = method
        url_path = environ['PATH_INFO']
        file_name = url_path.split('/')[-1]
        file_path = os.path.abspath(filename + "/../.." + "/PyPattern/Html/style/" + file_name)
        if 'png' in file_name:
            status = '200 OK'
            headers = [('Content-type', 'image/png')]
            st_response(status, headers)
            return open(file_path, "rb")
        if not url_path.endswith('/'):
            url_path = f'{url_path}/'
        if url_path in self.urls_lst:
            view = self.urls_lst[url_path]
            if req['method'] == 'GET':
                qry_str = environ['QUERY_STRING']
                parsed__params_dict = self.parsing_params(qry_str)
                req['req_params'] = Framework.decode_value(parsed__params_dict)
                print(f"Параметры GET запроса: {req['req_params']}")
            if req['method'] == 'POST':
                post_data = self.take_post_req(environ)
                post_data = self.parse_post_req(post_data)
                post_data = Framework.decode_value(post_data)
                req['post_params'] = post_data
                print(f"POST запрос: {req['post_params']}")
        else:
            view = Page404()
        for front in self.frcontr_lst:
            front(req)
        head, body = view(req)
        st_response(head, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]
