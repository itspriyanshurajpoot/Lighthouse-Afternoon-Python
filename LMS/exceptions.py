class BookNotFoundError(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class NoAvailableCopiesError(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class OutOfLimitError(Exception):
    def __init__(self, msg):
        super().__init__(msg)