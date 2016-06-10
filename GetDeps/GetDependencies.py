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

    def output_dep(self, file_dict:dict, cono, date, state):
        for no, dp in enumerate(file_dict.values()):
            #print("%d, %s, %s, %s" % (cono, dp.get_location(), date, state))
            self.__writer.writerow((cono, dp.get_location(), date, state))

    def get_file_location(self, filepass):
        fileref = self.__index.get_file_ref(filepass)
        if fileref == None:
            return

        return FDp.FileDependency(fileref).get_location()

    def get_deps(self, filepass, cono, date):
        self.__fileref = self.__index.get_file_ref(filepass)

        self.__fdp = FDp.FileDependency(self.__fileref) # ファイルの依存
        
        # from(依存されている)ファイルの辞書
        ed = self.file_to_depdict({self.__fileref:self.__fdp}, False)
        self.output_dep(ed, cono, date, "from")

        # to(依存している)
        cy = self.file_to_depdict({self.__fileref:self.__fdp}, True)
        self.output_dep(cy, cono, date, "to")

        ## from(依存されているものに)_from(依存されている)
        #ed2 = self.file_to_depdict(ed, False)
        #self.output_dep(ed2, cono, date, "from_from")

        ## from(依存されているものに)_to(依存している)
        #ed2 = self.file_to_depdict(ed, True)
        #self.output_dep(ed2, cono, date, "from_to")

        #cy2 = self.file_to_depdict(cy, False)
        #self.output_dep(cy2, cono, date, "to_from")

        #cy2 = self.file_to_depdict(cy, True)
        #self.output_dep(cy2, cono, date, "to_to")
