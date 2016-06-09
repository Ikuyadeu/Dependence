import xml.etree.ElementTree as ET
from GetDeps.Util import Util

class Dependency(object):
    """依存関係について格納するクラス"""
    def __init__(self, fileref):
         return Util.getroot(fileref)