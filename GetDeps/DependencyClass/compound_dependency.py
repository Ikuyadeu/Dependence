from GetDeps.DependencyClass.super_dependency import SuperDependency

class CompoundDependency(SuperDependency):
    """クラス単位の依存関係を格納する"""
    def __init__(self, fileref):
        super().__init__(fileref)
        self.location = super().get_location()

    def root_is_none(self):
        return self.root is None

    def get_kind(self):
        for compounddef in self.root.findall(r'./compounddef'):
            return compounddef.get('kind')
