import jinja2

t = jinja2.Template('Hello {{name}}')
print(t.render(name='John Doe'))
