import xml.etree.ElementTree as ET
import os.path

class SuperDependency(object):
    """Super class of dependency"""

    def __init__(self, fileref):
        self.root = self.get_root(fileref)

    @staticmethod
    def get_root(fileref):
        """filerefからxmlのrootを取得する"""

        if fileref is not None:
            filename = r'GetDeps\source\doxygen\xml\\' + str(fileref) + r".xml"
            try:
                return ET.parse(filename).getroot() if os.path.isfile(filename) else None
            except:
                return None

        return None

    def get_location(self):
        """rootからファイルのパスを得る"""
        if self.root is not None:
            for location in self.root.findall(r'./compounddef/location'):
                file_name = location.get('file')
                return file_name
        return ""
