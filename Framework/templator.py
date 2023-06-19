from jinja2 import Template
from os.path import join


def render(template_name, folder='Html', **kwargs):
    file_path = join(folder, template_name)
    with open(file_path, encoding='utf-8') as temp_file:
        template = Template(temp_file.read())
    return template.render(**kwargs)
