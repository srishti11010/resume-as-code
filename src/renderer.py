from jinja2 import Environment, FileSystemLoader
import os

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), 'themes')

env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))

def render_html(resume_data: dict, theme: str = 'modern') -> str:
    template = env.get_template(f'{theme}.html.j2')
    return template.render(resume=resume_data)
