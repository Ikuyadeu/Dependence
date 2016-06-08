import xml.etree.ElementTree as ET
import re
from DependencyClass import Dependency
from DependencyClass import FileDependency as FDp

class IndexDependency(Dependency.Dependency):
    """ 依存関係を管理するインデックスを格納 """
    def __init__(self, fileref):
        self.__root = super().__init__(fileref)
        self.__compoundname = './compound'
        self.__membername = '/member'
        self.__refidname = 'refid'
        self.__kindname = 'kind'

    def get_root(self):
        return self.__root

    def ref_to_compound(self, refid: str, kindref: str) -> str:
        if kindref == "compound":
            return refid
  
        for compound in self.__root.findall(self.__compoundname):
            for member in compound.findall('.' + self.__membername):
                if member.get(self.__refidname) == refid:
                    return compound.find('name').text
                    # return compound.get(self.__refidname)

    def id_to_kind(self, refid: str, kindref: str) -> str:
        """refidからrefの種類(class, function, variable)を取得する
        Args:
            refid:検索するid
            kindref:memberかcompoundかの種類
        Return:
            refの種類(class, function, variable)
        """

        findtag = self.__compoundname
        if kindref == "member":
            findtag += self.__membername

        for tag in self.__root.findall(findtag):
            if tag.get(self.__refidname) == refid:
                return tag.get(self.__kindname)

        return ""

    def get_kind_compound_list(self, kind):
        compound_list = []
        for compound in self.__root.findall(self.__compoundname):
            if kind == compound.get('kind'):
                compound_list.append(compound.get('refid'))
        return compound_list

    def get_file_ref(self, filepass):
        """ファイルパスからファイルのrefidを探す
        Args:
            filepass:検索するファイル名
        Return:
            ファイルのrefid
        """
        for compound in self.get_kind_compound_list('file'):
            fdp = FDp.FileDependency(compound)
            # 末尾と一致していたらOK
            if re.search(filepass + '$',fdp.get_location()):
                return compound
        return None