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

        # from(依存されている)ファイルの辞書
        ed = self.filelist_to_deplist(self.__root_list, False)
        self.output_dep(ed, "depender")

        # from(依存されているものに)_from(依存されている)
        ed2 = self.filelist_to_deplist(ed, False)
        self.output_dep(ed2, "depender2")

        # from(依存されているものに)_from(依存されている)
        ed3 = self.filelist_to_deplist(ed2, False)
        self.output_dep(ed3, "depender3")

        # from(依存されているものに)_from(依存されている)
        ed3 = self.filelist_to_deplist(ed3, False)
        self.output_dep(ed3, "depender4")

        # to(依存している)
        cy = self.filelist_to_deplist(self.__root_list, True)
        self.output_dep(cy, "dependee")

        cy2 = self.filelist_to_deplist(cy, True)
        self.output_dep(cy2, "dependee2")

        all = list(set(ed + cy + ed2 + cy2 + self.__root_list))
        other = [x for x in self.__allfilepass.values() if x not in all]
        self.output_dep(other, "other")