from anytree import NodeMixin, Resolver, ChildResolverError


class NewNode(NodeMixin):

    def __init__(self, name, parent=None, children=None):
        self.name = name
        self.parent = parent
        if children:
            self.children = children


class Storage(NodeMixin):

    _TRNSL = {"a": "a", "е": "e", "о": "o", "у": "u"}

    def __init__(self, name, parent=None, children=None):
        super(Storage, self).__init__()
        self.name = name
        self.parent = parent
        if children:
            self.children = children

    def get_node(self, path):
        r = Resolver('name')
        path_str = "/{}/{}".format(self.name, path)
        return r.get(self, path_str)


    def check_path(self, pos, vow):
        pos_str = "pos" + str(pos)
        vow_str = self._TRNSL.get(vow, "a")
        try:
            self.get_node(pos_str)

        except ChildResolverError:
            NewNode(pos_str, self)
        try:
            self.get_node(pos_str+"/"+vow_str)

        except ChildResolverError:
            NewNode(vow_str, self.get_node(pos_str))

        return self.get_node(pos_str+"/"+vow_str)




# d = Storage("dug")
# NewNode("pos0", d)







