import xml.etree.ElementTree as ET
from GetDeps.DependencyClass import FileDependency as FDp
from GetDeps.DependencyClass import IndexDependency as IDp
 
class GetDependencies(object):
    def __init__(self, writer):
        # 依存関係のindexを生成
        self.__writer = writer
        self.__writer.writerow(("commitNo", "file_location", "date", "author", "is_merge", "kind"))

    def set_commitinfo(self, commit_no, date, author, is_merge):
        self.__index = IDp.IndexDependency('index')
        self.__commit_no = commit_no
        self.__date = date
        self.__author = author
        self.__is_merge = is_merge
        self.__allfilepass = {}
        self.__depvector = []
        self.set_dep()

    def set_dep(self):
        compound_list = self.__index.get_kind_compound_list('file')
        for compoundref in compound_list:
            fdp = FDp.FileDependency(compoundref)
            self.__allfilepass[compoundref] = fdp.get_location()
            self.__depvector.extend(fdp.get_dependency())
        self.__depvector = [x for x in self.__depvector if x != []]

    def filelist_to_deplist(self, root_list, is_depender, notrecurusion):
        if is_depender: #　dependerを取得する
            i = 1 # 取得するほう(１は依存されているもの)
            j = 0 # 元の依存関係のもの
        else:
            i = 0
            j = 1
        if notrecurusion:
            return [x[i] for x in self.__depvector if x[j] in root_list and x[i] not in root_list]
        else:
            return [x[i] for x in self.__depvector if x[j] in root_list]

    def filelist_to_rec(self, root_list, is_depender):
        if is_depender: #　dependerを取得する
            i = 1 # 取得するほう(１は依存されているもの)
            j = 0 # 元の依存関係のもの
        else:
            i = 0
            j = 1
        return  [x[i] for x in self.__depvector if x[j] in root_list and x[i] not in root_list and 
                 not(x[i] in self.__root_list and 
                     len([y for y in self.__depvector if y[j] == x[j] and y[i] in self.__root_list]) < 2)]

    def output_dep(self, file_list, kind):
        for dp in file_list:
            self.__writer.writerow((self.__commit_no, dp, self.__date, self.__author, self.__is_merge, kind))

    def get_file_location(self, filelist):
        self.__root_list = []
        for filepass in filelist:
            fileref = self.__index.get_file_ref(filepass)
            if fileref != None:
                self.__root_list.append(self.__allfilepass[fileref])

    # rootにある要素がない
    def is_dev_recursion(self, devlist):
        return len(set(self.__root_list) & set(devlist)) < 2

    def get_deps(self):
        if len(self.__root_list) < 1:
            return

        self.output_dep(self.__root_list, "root")

        # depender(依存されている)ファイルの辞書
        ee = self.filelist_to_deplist(self.__root_list, False, False)
        self.output_dep(ee, "e")

        # depender2(依存されているものに依存されている)
        eeee = self.filelist_to_deplist(ee, False, True)
        self.output_dep(eeee, "ee")

        #eeer = self.filelist_to_deplist(ee, True, True)
        eeer = self.filelist_to_rec(ee, True, True)
        self.output_dep(eeer, "er")

        # dependee(依存している)
        er = self.filelist_to_deplist(self.__root_list, True, False)
        self.output_dep(er, "r")

        #eree = self.filelist_to_deplist(er, False, True)
        eree = self.filelist_to_rec(er, False, True)
        self.output_dep(eree, "re")

        erer = self.filelist_to_deplist(er, True, True)
        self.output_dep(erer, "rr")

        all = list(set(ee + er + eeee + eeer + erer + eree))
        other = [x for x in self.__allfilepass.values() if x not in all]
        self.output_dep(other, "o")