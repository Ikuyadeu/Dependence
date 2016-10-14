from GetDeps.DependencyClass.file_dependency import FileDependency as FDp
from GetDeps.DependencyClass.index_dependency import IndexDependency as IDp
import re

class GetDependencies(object):
    def __init__(self, writer):
        # 依存関係のindexを生成
        self.__writer = writer

    def set_commitinfo(self, commit_no, date, author, is_merge):
        self.__index = IDp('index')
        self.__commit_no = commit_no
        self.__date = date
        self.__author = author
        self.__is_merge = is_merge
        self.__allfilepass = []
        self.__depvector = []
        self.__root_list = []
        self.set_dep()

    def get_file_location(self, file_list):
        for file_pass in file_list:
            for fpass in self.__allfilepass:
                # 末尾と一致していたらOK
                if re.search(file_pass + '$', fpass):
                    self.__root_list.append(fpass)

    def set_dep(self):
        compound_dict = self.__index.ref_to_location()
        file_ref_list = self.__index.get_file_list()
        for compoundref in file_ref_list:
            fdp = FDp(compoundref)
            self.__allfilepass.append(fdp.location)
            self.__depvector.extend(fdp.get_dependency(compound_dict))
        self.__depvector = [x for x in self.__depvector if len(x) != 0]

    def filelist_to_deplist(self, root_list, is_depender):
        if is_depender: #　dependerを取得する
            i = 1 # 取得するほう(１は依存されているもの)
            j = 0 # 元の依存関係のもの
        else:
            i = 0
            j = 1
        return [x[i] for x in self.__depvector if x[j] in root_list]

    def filelist_to_rec(self, root_list, is_depender):
        if is_depender: #　dependerを取得する
            i = 1 # 取得するほう(１は依存されているもの)
            j = 0 # 元の依存関係のもの
        else:
            i = 0
            j = 1
        return [x[i] for x in self.__depvector if x[j] in root_list and 
                len([y for y in self.__depvector if y[j] == x[j]]) > 1]

    def output_dep(self, file_list, kind):
        for linedep in file_list:
            self.__writer.writerow((self.__commit_no, linedep, self.__date, self.__author, self.__is_merge, kind))


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
        other = [x for x in self.__allfilepass if x not in all_dep]

        dep_list = [self.__root_list, dependee, dependee2, deeder, depender, depender2, derdee, other]
        KIND_NAME = ["root", "e", "ee", "er", "r", "rr", "re", "o"]

        for (dep_files, kind) in zip(dep_list, KIND_NAME):
            for dep_file in set(dep_files):
                self.__writer.writerow((self.__commit_no, dep_file, self.__date, self.__author, self.__is_merge, kind))
    

