class MessagedException(Exception):

    def __init__(self, msg=""):
        self.msg = msg


class BadQueryException(MessagedException):
    pass


class BadInsertException(MessagedException):
    pass


class DBCreateException(MessagedException):
    pass


class DBDropException(MessagedException):
    pass


class CompileException(MessagedException):
    pass