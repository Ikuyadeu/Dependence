class Dependency(object):
    """依存関係について格納するクラス"""

    def __init__(self, id):
        self.__id = id

    def __str__(self):
        return self.__id