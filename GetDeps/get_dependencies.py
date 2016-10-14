import re
from GetDeps.DependencyClass.file_dependency import FileDependency as FDp
from GetDeps.DependencyClass.index_dependency import IndexDependency as IDp

class GetDependencies(object):
    """依存関係を所得するクラス"""
    def __init__(self):
        self.__index = IDp('index')
        self.__allfilepass = []
        self.__depvector = []
        self.__root_list = []
        self.set_dep()

    def set_dep(self):
        compound_dict = self.__index.ref_to_location()
        file_ref_list = self.__index.get_file_list()
        for compoundref in file_ref_list:
            fdp = FDp(compoundref)
            self.__allfilepass.append(fdp.location)
            self.__depvector.extend(fdp.get_dependency(compound_dict))
        self.__depvector = [x for x in self.__depvector if len(x) != 0]

    def get_file_location(self, file_list):
        for file_pass in file_list:
            for fpass in self.__allfilepass:
                # 末尾と一致していたらOK
                if re.search(file_pass + '$', fpass):
                    self.__root_list.append(fpass)

    def filelist_to_deplist(self, root_list, is_depender):
        if is_depender: #　dependerを取得する
            i = 1 # 取得するほう(１は依存されているもの)
            j = 0 # 元の依存関係のもの
        else:
            i = 0
            j = 1
        return list(set([x[i] for x in self.__depvector if x[j] in root_list]))

    def filelist_to_rec(self, root_list, is_depender):
        if is_depender: #　dependerを取得する
            i = 1 # 取得するほう(１は依存されているもの)
            j = 0 # 元の依存関係のもの
        else:
            i = 0
            j = 1
        return list(set([x[i] for x in self.__depvector if x[j] in root_list and
                         len([y for y in self.__depvector if y[j] == x[j]]) > 1]))

    def get_deps(self):
        # depender(依存されている)ファイルの辞書
        dependee = self.filelist_to_deplist(self.__root_list, False)

        # depender2(依存されているものに依存されている)
        dependee2 = self.filelist_to_deplist(dependee, False)

        deeder = self.filelist_to_rec(dependee, True)

        # dependee(依存している)
        depender = self.filelist_to_deplist(self.__root_list, True)

        depender2 = self.filelist_to_deplist(depender, True)

        derdee = self.filelist_to_rec(depender, False)

        all_dep = list(set(dependee + dependee2 + deeder + depender + depender2 + derdee))
        other = list(set([x for x in self.__allfilepass if x not in all_dep]))

        return [self.__root_list, dependee, dependee2, deeder,
                depender, depender2, derdee, other]
