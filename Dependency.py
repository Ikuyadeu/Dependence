class Dependency(object):
    """依存関係について格納するクラス"""

    def __init__(self, id, ref, lineno, text):
        self._id = id
        self._kindref = ref
        self._lineno = lineno
        self._text = text
        self._kind = None

    def __str__(self):
        return self._text

    def get_kindref(self):
        return self._kindref

    def get_lineno(self):
        return self._lineno

    def set_kind(self, kind):
        self._kind = kind

    def get_kind(self):
        return self._kind