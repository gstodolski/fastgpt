import string
from variable import Variable
from open_ai import run_chatgpt

class Template:
    """Template for ChatGPT prompts"""

    def __init__(self, title):
        """Initializes the template"""
        self.title = title
        self.content = []
        self.string = ""

    def get_content(self):
        """Returns the content of the template"""
        return self.content
    
    def get_variable(self, name):
        """Returns the variable with the given name"""
        for var in self.get_variables():
            if var.name == name:
                return var
        return None

    def get_variables(self):
        """Returns the variables of the template"""
        out = []
        for word in self.content:
            if isinstance(word, Variable):
                out.append(word)
        return out
            
    def set_variable(self, name, value):
        """Sets the variable with the given name to the given value"""
        for var in self.get_variables():
            if var.name == name:
                var.value = value

    def add_content(self, content):
        """Adds strings and variables to the template"""
        for word in content.split():
            punc = None
            if word[-1] in string.punctuation and word[-1] not in ['$', '#', '*']:
                punc = word[-1]
                word = word[:-1]

            if word[0] == '$' and word[-1] == '$':
                word = Variable(word[1:-1], "text")
            elif word[0] == '#' and word[-1] == '#':
                word = Variable(word[1:-1], "number")
            elif word[0] == '*' and word[-1] == '*':
                word = Variable(word[1:-1], "date")
            
            if punc is not None and isinstance(word, Variable):
                word.punc = punc
            elif punc is not None:
                word += punc
            
            self.content.append(word)

    def prepare_string(self):
        """Prepares the string for ChatGPT"""
        out = ''
        for word in self.content:
            if isinstance(word, Variable):
                if word.punc is not None:
                    out += word.value + word.punc + ' '
                else:
                    out += word.value + ' '
            else:
                out += word + ' '
        return out.rstrip()

    def execute_template(self):
        """Runs the template in ChatGPT"""
        # Check that variables are defined
        for var in self.get_variables():
            if var.value is None:
                raise ValueError('Variable %s is not defined' % var.name)
        
        prompt = self.prepare_string()
        return run_chatgpt(prompt)
