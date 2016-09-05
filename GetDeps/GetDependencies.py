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
        self.__dependency_dict = {}
        self.__allfilepass = {}
        self.set_dep()

    def set_dep(self):
        compound_list = self.__index.get_kind_compound_list('file')
        for compoundref in compound_list:
            fdp = FDp.FileDependency(compoundref)
            self.__dependency_dict[compoundref] = fdp.get_dependency()
            self.__allfilepass[compoundref] = fdp.get_location()

    def filelist_to_deplist(self, root_list, is_depender):
        dep_list = []
        for root in root_list:
            if is_depender:
                ref = self.__index.get_file_ref(root)
                try:
                    dep_list.extend(self.__dependency_dict.get(ref).values())
                except:
                    pass
                else:
                    pass
            else:
                for id, dep in self.__dependency_dict.items():
                    if root in dep.values():
                        dep_list.append(self.__allfilepass[id])

        return list(set(dep_list))

    def output_dep(self, file_list, kind):
        for dp in file_list:
            self.__writer.writerow((self.__commit_no, dp, self.__date, self.__author, self.__is_merge, kind))

    def get_file_location(self, filelist):
        self.__root_list = []
        for filepass in filelist:
            fileref = self.__index.get_file_ref(filepass)
            if fileref != None:
                self.__root_list.append(self.__allfilepass[fileref])

    def get_deps(self):
        if len(self.__root_list) < 1:
            return

        self.output_dep(self.__root_list, "root")

        # depender(依存されている)ファイルの辞書
        ee = self.filelist_to_deplist(self.__root_list, False)
        self.output_dep(ee, "ee")

        # depender2(依存されているものに依存されている)
        eeee = self.filelist_to_deplist(ee, False)
        self.output_dep(eeee, "eeee")

        eeer = self.filelist_to_deplist(ee, True)
        self.output_dep(eeer, "eeer")

        # dependee(依存している)
        er = self.filelist_to_deplist(self.__root_list, True)
        self.output_dep(er, "er")

        eree = self.filelist_to_deplist(er, False)
        self.output_dep(eree, "eree")

        erer = self.filelist_to_deplist(er, True)
        self.output_dep(erer, "erer")

        all = list(set(ee + er + eeee + eeer + erer + eree))
        other = [x for x in self.__allfilepass.values() if x not in all]
        self.output_dep(other, "other")