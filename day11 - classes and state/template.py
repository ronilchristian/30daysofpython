import os

FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(FILE_PATH)
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

class Template():
    template_name = ""
    context = None

    def __init__(self, template_name="hello.txt", context=None, *args, **kwargs):
        self.template_name = template_name
        self.context = context

    def get_template(self):
        template_path = os.path.join(TEMPLATE_DIR, self.template_name)
        if not os.path.exists(template_path):
            raise Exception("This path does not exist") 
        template_string = ""
        with open(template_path, "r") as f:
            template_string = f.read()
        return template_string

    def render(self, context=None):
        render_context = context

        if self.context != None:
            render_context = self.context
        if not isinstance(render_context, dict):
            render_context = {}
        template_string = self.get_template()
        return template_string.format(**render_context) # {"name":"Ronil"} -> name="Ronil"
