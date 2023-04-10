TEXT = 0
NUMBER = 1
DATE = 2

class Variable:
    """Variable within a template"""

    def __init__(self, name, type):
        """Initialize a new Variable"""
        self.name = name
        self.type = type
        self.value = None
