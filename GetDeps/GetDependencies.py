import xml.etree.ElementTree as ET
from GetDeps.DependencyClass import CompoundDependency as CDp
from GetDeps.DependencyClass import FileDependency as FDp
from GetDeps.DependencyClass import IndexDependency as IDp
from GetDeps.Util import Util
 
class GetDependencies(object):
    def __init__(self, writer):
        # 依存関係のindexを生成
        self.__index = IDp.IndexDependency('index')
        self.__writer = writer
        self.__writer.writerow(("commitNo", "file_location", "date", "author", "is_merge", "kind"))

    def set_commitinfo(self, commit_no, date, author, is_merge):
        self.__commit_no = commit_no
        self.__date = date
        self.__author = author
        self.__is_merge = is_merge
        self.__dependency_dict = self.set_dep()

    def set_dep(self):
        dependency_dict = {}
        compound_list = self.__index.get_kind_compound_list('file')
        for compoundref in compound_list:
            fdp = FDp.FileDependency(compoundref)
            dependency_dict[compoundref] = fdp.get_dependency()
            
        return dependency_dict

    def file_to_depdict(self, root_list, is_to_dep:bool):
        dep_dict = []
        for root in root_list:
            ref = self.__index.get_file_ref(root)
            if is_to_dep:
                try:
                    dep_dict.extend(self.__dependency_dict.get(ref).values())
                except:
                    pass
                else:
                    pass
            else:
                for id, dep in self.__dependency_dict.items():
                    if root in dep.values():
                        dep_dict.append(FDp.FileDependency(id).get_location())

        return dep_dict

    def output_dep(self, file_list, kind):
        #for no, dp in enumerate(file_dict.values()):
        #    self.__writer.writerow((self.__commit_no, dp.get_location(), self.__date, self.__author, self.__is_merge, kind))
        for no, dp in enumerate(file_list):
            self.__writer.writerow((self.__commit_no, dp, self.__date, self.__author, self.__is_merge, kind))

    def get_file_location(self, filepass):
        fileref = self.__index.get_file_ref(filepass)
        if fileref == None:
            return

        return FDp.FileDependency(fileref).get_location()

    def get_deps(self, filepass):
        self.__fileref = self.__index.get_file_ref(filepass)

        self.__fdp = FDp.FileDependency(self.__fileref) # ファイルの依存
        
        ## from(依存されている)ファイルの辞書
        #ed = self.file_to_depdict({self.__fileref:self.__fdp}, False)
        #self.output_dep(ed, "from")

        ## to(依存している)
        #cy = self.file_to_depdict({self.__fileref:self.__fdp}, True)
        #self.output_dep(cy, "to")

        # from(依存されている)ファイルの辞書
        ed = self.file_to_depdict([self.__fdp.get_location()], False)
        self.output_dep(ed, "from")

        # to(依存している)
        cy = self.file_to_depdict([self.__fdp.get_location()], True)
        self.output_dep(cy, "to")

        # from(依存されているものに)_from(依存されている)
        ed2 = self.file_to_depdict(ed, False)
        self.output_dep(ed2, "from_from")

        # from(依存されているものに)_to(依存している)
        ed2 = self.file_to_depdict(ed, True)
        self.output_dep(ed2, "from_to")

        cy2 = self.file_to_depdict(cy, False)
        self.output_dep(cy2, "to_from")

        cy2 = self.file_to_depdict(cy, True)
        self.output_dep(cy2, "to_to")