import xml.etree.ElementTree as ET
from GetDeps.DependencyClass import CompoundDependency as CDp
from GetDeps.DependencyClass import FileDependency as FDp
from GetDeps.DependencyClass import IndexDependency as IDp
from GetDeps.Util import Util
 
class GetDeps(object):
    def __init__(self, filepass):
        # 依存関係のindexを生成
        self.__index = IDp.IndexDependency('index')
        self.__fileref = self.__index.get_file_ref(filepass)
        
        self.__fdp = FDp.FileDependency(self.__fileref) # ファイルの依存

    def file_to_depdict(self, root_dict:dict, is_to_dep:bool):
        dep_dict = {}
        for dep in root_dict.values():
            ref = self.__index.get_file_ref(dep.get_location())
            fdp = FDp.FileDependency(ref)
            get_dep = fdp.get_dependency() if is_to_dep else fdp.get_dependencied()

            for id, dp2 in get_dep.items():
                if not (id in root_dict or id in dep_dict):
                    dep_dict[id] = dp2


        return dep_dict

    def output_dep(self, file_dict:dict, state):
        for no, dp in enumerate(file_dict.values()):
            print("%s, %s" % (dp.get_location(), state))

    def getdeps(self):
        # from(依存されている)ファイルの辞書
        ed = self.file_to_depdict({self.__fileref:self.__fdp}, False)
        self.output_dep(ed, "from")

        # to(依存している)
        cy = self.file_to_depdict({self.__fileref:self.__fdp}, True)
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
