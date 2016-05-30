import xml.etree.ElementTree as ET
from DependencyClass import Dependency
from DependencyClass import CompoundDependency as CDp
from DependencyClass import IndexDependency as IDp
from DependencyClass import FileDependency as FDp

class FileDependency(Dependency.Dependency):
    """description of class"""
    def __init__(self, fileref):
        self.__ref = fileref
        self.__root = self.getroot(self.__ref)
        self.__dependency_dict = {}
        self.__dependencied_dict = {}
        self.__innerclass_list = []
        self.add_innnerclass()

    def add_innnerclass(self):
        for innerclass in self.__root.findall('./compounddef/innerclass'):
            self.__innerclass_list.append(innerclass.get('refid'))

    def get_dependency(self):
        for ref in self.__root.findall('./compounddef/programlisting/codeline/highlight/ref'):
            refid = ref.get('refid')

            if refid in self.__dependency_dict or refid in self.__innerclass_list:
                continue
                
            if ref.get('kindref') != "compound":
                continue

            compound = CDp.CompoundDependency(refid)
            if compound.get_kind() != "namespace":
                self.__dependency_dict[refid] = compound
        return self.__dependency_dict

    def get_dependencied(self):
        compound_list = IDp.IndexDependency('index') .get_kind_compound_list('file')
        for compoundref in compound_list:
            if compoundref == self.__ref:
                continue
            fdp = FDp.FileDependency(compoundref)
            for inner_class in self.__innerclass_list:
                if fdp.in_compound(inner_class):
                   self.__dependencied_dict[compoundref] = CDp.CompoundDependency(compoundref)
        return self.__dependencied_dict

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
