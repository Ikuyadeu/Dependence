import xml.etree.ElementTree as ET
from GetDeps.DependencyClass import Dependency
from GetDeps.DependencyClass import CompoundDependency as CDp
from GetDeps.DependencyClass import IndexDependency as IDp
from GetDeps.DependencyClass import FileDependency as FDp

class FileDependency(Dependency.Dependency):
    """description of class"""
    def __init__(self, fileref):
        self.__ref = fileref
        self.__root = self.get_root(fileref)
        self.__depvec = []
        self.__innerclass_list = []
        self.add_innnerclass()
        self.__location = self.get_location()

        # 自分自身のクラスを取得
    def add_innnerclass(self):
        for innerclass in self.__root.findall('./compounddef/innerclass'):
            self.__innerclass_list.append(innerclass.get('refid'))

    def get_dependency(self):
        for ref in self.__root.findall('./compounddef/programlisting/codeline/highlight/ref'):
            refid = ref.get('refid')

            if refid in self.__innerclass_list or ref.get('kindref') != "compound":
                continue
                
            compound = CDp.CompoundDependency(refid)
            if compound.root_is_none() or compound.get_kind() == "namespace":
                continue

            self.__depvec.append([self.__location, compound.get_location()])
            self.__innerclass_list.append(refid)

        return self.__depvec

    def in_compound(self, refid):
        for ref in self.__root.findall('./compounddef/programlisting/codeline/highlight/ref'):
            if refid == ref.get('refid'):
                return True
        return False

    def get_location(self):
        for location in self.__root.findall(r'./compounddef/location'):
            file_name = location.get('file')
            return file_name
        return ""
