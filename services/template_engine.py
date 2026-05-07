from jinja2 import Template

def render(subject, body, context):
    subject_rendered = Template(subject).render(**context)
    body_rendered = Template(body).render(**context)
    return subject_rendered, body_rendered