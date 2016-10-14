from GetDeps.DependencyClass.super_dependency import SuperDependency

class FileDependency(SuperDependency):
    """description of class"""
    def __init__(self, fileref):
        super().__init__(fileref)
        self.location = super().get_location()

    def get_dependency(self, compound_dict):
        dev_vec = []
        innerclass_list = []
        for innerclass in self.root.findall('./compounddef/innerclass'):
            innerclass_list.append(innerclass.get('refid'))

        for ref in self.root.findall('./compounddef/programlisting/codeline/highlight/ref'):
            refid = ref.get('refid')
            if refid not in innerclass_list and \
            ref.get('kindref') == "compound" and refid in compound_dict:
                dev_vec.append([self.location, compound_dict[refid]])
                innerclass_list.append(refid)

        return dev_vec
