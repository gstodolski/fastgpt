from variable import Variable

TEXT = 0
NUMBER = 1
DATE = 2

class Template:
    """Template for ChatGPT prompts"""

    def __init__(self, title):
        """Initializes the template"""
        self.title = title
        self.content = []

    def get_content(self):
        """Returns the content of the template"""
        return self.content

    def get_variables(self):
        """Returns the variables of the template"""
        out = []
        for word in self.content:
            if isinstance(word, Variable):
                out.append(word)
        return out

    def add_content(self, content):
        """Adds strings and variables to the template"""
        for word in content.split():
            if word[0] == '$' and word[-1] == '$':
                word = Variable(word[1:-1], TEXT)
            elif word[0] == '#' and word[-1] == '#':
                word = Variable(word[1:-1], NUMBER)
            elif word[0] == '*' and word[-1] == '*':
                word = Variable(word[1:-1], DATE)
            self.content.append(word)

    def prepare_string(self):
        """Prepares the string for ChatGPT"""
        out = ''
        for word in self.content:
            if isinstance(word, Variable):
                out += word.value + ' '
            else:
                out += word + ' '
        return out.rstrip()

    def execute_template(self):
        """Runs the template in ChatGPT"""
        # Check that variables are defined
        for var in self.get_variables():
            if var.name == "name":
                    var.value = "GRAHAM"
            if var.value is None:
                raise ValueError('Variable %s is not defined' % var.name)
        
        prompt = self.prepare_string()
        return prompt
        # return runChatGPT(prompt)

if __name__ == '__main__':
    template = Template('Hello')
    template.add_content('My name is $name$')
    print(template.get_content())
    print(template.execute_template())
