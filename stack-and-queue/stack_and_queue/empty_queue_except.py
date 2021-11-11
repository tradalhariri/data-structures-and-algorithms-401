class EmptyQueue(Exception):
    """Exception raised when dequeue or peek from empty Queue.
    """

    def __init__(self,value, message="empty Queue"):
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'cant dequeue or peek "{self.value}" from {self.message}'