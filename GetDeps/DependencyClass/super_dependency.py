import xml.etree.ElementTree as ET
import os.path

class Dependency(object):
    """refidからXMLファイル名を生成
    Args:
        refid:refのid
    Returns:
        XMLのファイル名
    """
    def get_root(self, fileref):
        if fileref is not None:
            filename = r'GetDeps\source\doxygen\xml\\' + str(fileref) + r".xml"
            return ET.parse(filename).getroot() if os.path.isfile(filename) else None
    
        return None
