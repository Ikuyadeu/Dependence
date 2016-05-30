import xml.etree.ElementTree as ET

class Dependency(object):
    """依存関係について格納するクラス"""
    def __init__(self, filename):
        pass

    def __ref_to_XMLname(self, refid:str):
        """refidからXMLファイル名を生成
        Args:
            refid:refのid
        Returns:
            XMLのファイル名
        """
        return r'source\doxygen\xml\\' + str(refid) + r".xml"

    def getroot(self, fileref):
        return ET.parse(self.__ref_to_XMLname(fileref)).getroot()
