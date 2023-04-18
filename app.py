from template import Template
import pickle

class App:
    """Handle application operations and interact with GUI"""

    def __init__(self):
        """Initialize list of templates"""
        self.templates = []

        def new_template(self, title):
            """Create a new template"""
            template = Template(title)
            self.templates.append(template)
            return template

        def get_template(self, title):
            """Get the template with the given title"""
            for template in self.templates:
                if template.title == title:
                    return template
            return None
