class EmptyStack(Exception):
    """Exception raised when pop or peek from empty stack.
    """

    def __init__(self,value, message="empty stack"):
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'cant pop or peek "{self.value}" from {self.message}'