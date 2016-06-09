import xml.etree.ElementTree as ET

def getroot(fileref):
    return ET.parse(ref_to_XMLname(fileref)).getroot()

def ref_to_XMLname(refid:str):
    """refidからXMLファイル名を生成
    Args:
        refid:refのid
    Returns:
        XMLのファイル名
    """
    return r'GetDeps\source\doxygen\xml\\' + str(refid) + r".xml"