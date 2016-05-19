class DependencyIndex(object):
    """ 依存関係を管理するインデックスを格納 """
    def __init__(self, root):
        self.__root = root
        self.__compoundname = './compound'
        self.__membername = '/member'
        self.__refidname = 'refid'
        self.__kindname = 'kind'

    def get_root(self):
        return self.__root

    def ref_to_compound(self, refid, kindref):
        if kindref == "compound":
            return refid
  
        for compound in self.__root.findall(self.__compoundname):
            for member in compound.findall('.' + self.__membername):
                if member.get(self.__refidname) == refid:
                    return compound.find('name').text
                    # return compound.get(self.__refidname)

    def id_to_kind(self, refid, kindref):
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

    def get_file_ref(self, filename):
        """ファイル名からファイルのrefidを探す
        Args:
            filename:検索するファイル名
        Return:
            ファイルのrefid
        """
        for compound in self.__root.findall(self.__compoundname):
            if compound.get(self.__kindname) == "file" and filename == compound.find('name').text:
                return compound.get(self.__refidname)

        return None

