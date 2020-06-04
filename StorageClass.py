import json
from anytree import NodeMixin, Resolver, ChildResolverError


class NewNode(NodeMixin):

    def __init__(self, name, parent=None, children=None):
        self.name = name
        self.parent = parent
        if children:
            self.children = children


class Storage(NodeMixin):

    _model_ver = '0.1'

    _TRNSL = {"а": "a", "е": "e",
              "ё": "yo", "и": "i",
              "о": "o", "у": "u", "ы": "uu",
              "э": "ae", "ю": "yu", "я": "ya"}

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
        vow_str = self._TRNSL.get(vow, "error")
        try:
            self.get_node(pos_str)

        except ChildResolverError:
            NewNode(pos_str, self)
        try:
            self.get_node(pos_str+"/"+vow_str)

        except ChildResolverError:
            NewNode(vow_str, self.get_node(pos_str))

        return self.get_node(pos_str+"/"+vow_str)

    def export(self):
        exp_model = {}
        exp_model['version'] = self._model_ver
        exp_model['name'] = self.name
        exp_lines = []
        for i in self.leaves:
            id = "id" + str(abs(hash(i.text)))
            exp_lines.append(i.generate_export(id))
        exp_model['lines'] = exp_lines
        json_name = "model_" + self.name +".json"
        with open(json_name, 'w', encoding='utf-8') as f:
            json.dump(exp_model, f, ensure_ascii=False, indent=4)














