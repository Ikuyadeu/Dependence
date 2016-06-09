import xml.etree.ElementTree as ET

def getroot(fileref):
    filename = ref_to_XMLname(fileref)
    if filename == None:
        return None
    return ET.parse(filename).getroot()

def ref_to_XMLname(refid:str):
    """refidからXMLファイル名を生成
    Args:
        refid:refのid
    Returns:
        XMLのファイル名
    """
    if refid == None:
        return None
    return r'GetDeps\source\doxygen\xml\\' + str(refid) + r".xml"