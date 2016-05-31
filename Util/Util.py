def __ref_to_XMLname(refid:str):
        """refid����XML�t�@�C�����𐶐�
        Args:
            refid:ref��id
        Returns:
            XML�̃t�@�C����
        """
        return r'source\doxygen\xml\\' + str(refid) + r".xml"