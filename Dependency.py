class Dependency:
    """依存関係について格納するクラス"""

    def __init__(self, id, ref, lineno):
        self._id = id
        self._kindref = ref
        self._lineno = lineno

    def __str__(self):
        return self._id

    def get_kindref(self):
        return self._kindref

    def get_lineno(self):
        return self._lineno