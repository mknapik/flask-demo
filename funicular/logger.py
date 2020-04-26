from logging import Logger as _Logger


class Logger(_Logger):
    def __init__(self):
        super().__init__("flask")
