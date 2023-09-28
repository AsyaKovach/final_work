class NotSupportException(Exception):
    def __init__(self, s):
        super().__init__(s)