from GetDeps.DependencyClass.Dependency import Dependency

class CompoundDependency(Dependency):
    """description of class"""
    def __init__(self, fileref):
        self.__root = self.get_root(fileref)

    def root_is_none(self):
        return self.__root is None

    def get_kind(self):
        for compounddef in self.__root.findall(r'./compounddef'):
            return compounddef.get('kind')

    def get_location(self):
        for location in self.__root.findall(r'./compounddef/location'):
            file_name = location.get('file')
            return file_name
        return ""
