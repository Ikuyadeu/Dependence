def ref_to_XMLname(refid:str):
    """refidからXMLファイル名を生成
    Args:
        refid:refのid
    Returns:
        XMLのファイル名
    """
    return r'source\doxygen\xml\\' + str(refid) + r".xml"
