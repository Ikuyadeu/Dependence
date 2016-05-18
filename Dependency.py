class Dependency(object):
    """依存関係について格納するクラス"""

    def __init__(self, id,  text, lineno, kind):
        self.__id = id
        self.__text = text
        self.__lineno = lineno
        self.__kind = kind

    def __str__(self):
        return self.__text

    def get_lineno(self):
        return self.__lineno

    def get_kind(self):
        return self.__kind