import xml.etree.ElementTree as ET
from Util import Util

class Dependency(object):
    """依存関係について格納するクラス"""
    def __init__(self, filename):
        pass

    def getroot(self, fileref):
        return ET.parse(Util.ref_to_XMLname(fileref)).getroot()
