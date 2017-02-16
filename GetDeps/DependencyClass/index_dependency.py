from GetDeps.DependencyClass.super_dependency import SuperDependency
from GetDeps.DependencyClass.compound_dependency import CompoundDependency as CDp

class IndexDependency(SuperDependency):
    """ 依存関係を管理するインデックスを格納 """
    def __init__(self, fileref):
        super().__init__(fileref)
        self.__compound_name = './compound'
        self.__member_name = '/member'
        self.__refid_name = 'refid'
        self.__kind_name = 'kind'

    def ref_to_compound(self, refid: str, kindref: str) -> str:
        """refidからクラス名を取得"""
        if kindref == "compound":
            return refid

        for compound in self.root.findall(self.__compound_name):
            for member in compound.findall('.' + self.__member_name):
                if member.get(self.__refid_name) == refid:
                    return compound.find('name').text
                    # return compound.get(self.__refidname)

    def ref_to_kind(self, refid: str, kindref: str) -> str:
        """refidからrefの種類(class, function, variable)を取得する
        Args:
            refid:検索するid
            kindref:memberかcompoundかの種類
        Return:
            refの種類(class, function, variable)
        """

        findtag = self.__compound_name
        if kindref == "member":
            findtag += self.__member_name

        for tag in self.root.findall(findtag):
            if tag.get(self.__refid_name) == refid:
                return tag.get(self.__kind_name)

        return ""

    def ref_to_location(self):
        """ファイルidからファイルパスを取得"""
        compound_dict = {}
        for compound in self.root.findall(self.__compound_name):
            if compound.get('kind') != 'namespace':
                ref_id = compound.get('refid')
                location = CDp(ref_id).location
                compound_dict[ref_id] = location

        return compound_dict

    def get_file_list(self):
        """ファイルのリストを取得"""
        file_list = []
        for compound in self.root.findall(self.__compound_name):
            if compound.get('kind') == 'file':
                file_list.append(compound.get('refid'))
        return file_list
