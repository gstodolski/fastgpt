from template import Template
from variable import Variable

class App:
    """Handle application operations and interact with GUI"""

    def __init__(self):
        """Initialize list of templates"""
        self.templates = []
        self.add_template("Email", "Write an email to a broker named $broker$ about purchasing their property $property$.")

    def add_template(self, title, content):
        """Create a new template"""
        template = Template(title)
        template.add_content(content)
        template.string = content
        self.templates.append(template)
        return template

    def get_template(self, title):
        """Get the template with the given title"""
        for template in self.templates:
            if template.title == title:
                return template
        return None
    
    def get_template_names(self):
        """Get a list of template names"""
        out = []
        for template in self.templates:
            out.append(template.title)
        return out
