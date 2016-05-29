from DependencyClass import Dependency
import xml.etree.ElementTree as ET

class CompoundDependency(object):
    """description of class"""
    def __init__(self, rootname):
        self.__dependency_list = []
        self.__root = ET.parse(rootname).getroot()
        #return super().__init__(id, name, lineno, kind, compound)

    def add_root(self, rootname):
        self.__root = ET.parse(rootname).getroot()

    def search_dependencylist(self):
        for reftype in self.__root.findall(r'./compounddef/sectiondef/memberdef/type/ref'):
            refid = reftype.get('refid')
            if refid not in self.__dependency_list:
                self.__dependency_list.append(refid)

    def get_dependency_list(self):
        return self.__dependency_list