from DependencyClass import Dependency
import xml.etree.ElementTree as ET

class CompoundDependency(Dependency.Dependency):
    """description of class"""
    def __init__(self, fileref):
        self.__root = super().__init__(fileref)

    def search_dependencylist(self):
        for reftype in self.__root.findall(r'./compounddef/sectiondef/memberdef/type/ref'):
            refid = reftype.get('refid')
            if refid not in self.__dependency_list:
                self.__dependency_list.append(refid)

    def get_kind(self):
        for compounddef in self.__root.findall(r'./compounddef'):
            return compounddef.get('kind')

    def get_location(self):
        for location in self.__root.findall(r'./compounddef/location'):
            file_name = location.get('file')
            return file_name
        return ""