from DataProcessing import Data
from StorageClass import Storage
from LineClass import Line
from text import text

class Action:

    def __init__(self, storage):
        self.ready_lines = []
        self.storage = storage

    def prepare_data(self):
        d = Data()
        d.prepare_lines()
        d.get_accent()
        self.ready_lines = d.lines_ready

    def save_lines(self):
        for l in self.ready_lines:
            l_tmp = Line(l[0], accents=l[1],
                         acc_scheme=l[2])
            l_tmp.new_rhyme_params()
            parent_node = self.storage.check_path(l_tmp.rhyme_params['pos'],
                                                  l_tmp.rhyme_params['wovel'])
            l_tmp.parent=parent_node
            print(l_tmp.text + " Saved")


new_storage = Storage("dugin")
a = Action(new_storage)
a.prepare_data()
s = a.save_lines()

print(len(s))