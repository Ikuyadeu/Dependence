class Dependency(object):
    """依存関係について格納するクラス"""

    def __init__(self, id,  name, lineno, kind, compound):
        self.__id = id
        self.__name = name
        self.__lineno = lineno
        self.__kind = kind
        self.__compound = compound

    def __str__(self):
        return self.__name

    def get_lineno(self):
        return self.__lineno

    def get_kind(self):
        return self.__kind

    def get_compound(self):
        return self.__compound