from DataProcessing import Data
from StorageClass import Storage
from LineClass import Line
from text import text
import re
import pymorphy2
from random import choices
from itertools import combinations

"""
from ActionClass import Action
s = Storage('dug')
a = Action(s)
a.prepare_data()
a.save_lines()

"""

class Action:

    def __init__(self, storage):
        self.ready_lines = []
        self.storage = storage
        self.str8 = []
        self.str7 = []

    def prepare_data(self):
        d = Data()
        # d.prepare_lines()
        # d.get_accent()
        d.read_from_file()
        self.ready_lines = d.lines_ready

    def save_lines(self):
        morph = pymorphy2.MorphAnalyzer()
        for l in self.ready_lines:
            words = re.sub('\?|\.|\,|\!|\/|\;|\:|\“|\…', '', l[0]).split()
            words[-1] = morph.parse(words[-1])[0].normal_form

            l_tmp = Line(l[0], words=words, accents=l[1],
                         acc_scheme=l[2])
            l_tmp.new_rhyme_params()
            parent_node = self.storage.check_path(l_tmp.rhyme_params['pos'],
                                                  l_tmp.rhyme_params['wovel'])
            for n in parent_node.children:
                rate = Line.is_rhyme(l_tmp, n)
                if rate == 1.0:
                    print(l_tmp.text + "|", n.text)
            l_tmp.parent=parent_node
            # print(l_tmp.text + " Saved")
        for i in self.storage.leaves:
            if i.acc_scheme == [0, 0, 1, 0, 0, 0, 1, 0]:
                self.str8.append(i)
            elif i.acc_scheme == [0, 0, 1, 0, 0, 0, 1]:
                self.str7.append(i)

    def best_rhyme(self, lines_list):
        rhyme_ranks = []
        combos = list(combinations(lines_list, 2))
        for c in combos:
            rank = Line.is_rhyme(*c)
            rhyme_ranks.append((rank, c))
        return sorted(rhyme_ranks, key=lambda tup: tup[0], reverse=True)



    def chast(self):
        l1, l3 = choices(self.str8, k=2)
        l2, l4 = choices(self.str7, k=2)
        chast_str = "{}\n{}\n{}\n{}!".format(l1.text, l2.text, l3.text, l4.text)
        print(chast_str)




