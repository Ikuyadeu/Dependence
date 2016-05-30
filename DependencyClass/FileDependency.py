import xml.etree.ElementTree as ET
from DependencyClass import Dependency
from DependencyClass import CompoundDependency as CDp

class FileDependency(Dependency.Dependency):
    """description of class"""
    def __init__(self, fileref):
        self.__ref = fileref
        self.__root = self.getroot(self.__ref)
        self.__dependency_dict = {}
        self.__innerclass = []

    def get_innnerclass(self):
        for compounddef in self.__root.findall('./compounddef'):
            compoundname = compounddef.find('compoundname').text
            innerclass = compounddef.find('innerclass')
            innerclass_refid = innerclass.get('refid')
        

    def get_dependency(self):
        for ref in self.__root.findall('./compounddef/programlisting/codeline/highlight/ref'):
            refid = ref.get('refid')

            if refid in self.__dependency_dict:
                continue
                
            if ref.get('kindref') != "compound":
                continue

            compound = CDp.CompoundDependency(refid)
            self.__dependency_dict[refid] = compound

    def output_dependency_dict(self):
        for __, compound in self.__dependency_dict.items():
            print(compound.get_location(), compound.get_kind())

    def get_dependency_dict(self):
        return self.__dependency_dict


