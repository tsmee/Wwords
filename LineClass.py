from anytree import NodeMixin
from StorageClass import Storage

class AbstractLine:


    @staticmethod
    def is_rhyme(l1, l2):
        _POS = {True: 0.0, False: -1.0}
        _WOV = {True: 0.0, False: -1.0}
        _PRE = {True: 0.0, False: -0.25}
        _POST = {True: 0.0, False: -0.25}

        pos_equal = l1.rhyme_params['pos'] == l2.rhyme_params['pos']
        wov_equal = l1.rhyme_params['wovel'] == l2.rhyme_params['wovel']
        pre_equal = l1.rhyme_params['pre'] == l2.rhyme_params['pre']
        post_equal = l1.rhyme_params['post'] == l2.rhyme_params['post']
        rhyme_coeff = 1 + _POS[pos_equal] + _WOV[wov_equal] + _PRE[pre_equal] + _POST[post_equal]
        return rhyme_coeff


class Line(NodeMixin, AbstractLine):

    def __init__(self, line: str, accents=[], acc_scheme=[], children=None, parent=None, storage=None):

        self.text = line
        self.accents = accents
        self.acc_scheme = acc_scheme
        self.rhyme_params = {}

    def new_rhyme_params(self):
        self.rhyme_params['pos'] = self.acc_scheme[::-1].index(1)
        self.rhyme_params['wovel'] = self.text[self.accents[-1]]
        post = ""
        if self.accents[-1] < len(self.text) + 1:
            post = self.text[self.accents[-1] + 1]
        self.rhyme_params['post'] = post
        self.rhyme_params['pre'] = self.text[self.accents[-1] - 1]



#
#
# l = Line("подвернувшийся журнал")
# l.accents = [4, 19]
# l.acc_scheme = [0, 1, 0, 0, 0, 0, 1]
# p = l.new_rhyme_params()
#
# l2 = Line("из своей квартиры и")
# l2.accents = [6, 14]
# l2.acc_scheme = [0, 0, 1, 0, 1, 0, 0]
# p = l2.new_rhyme_params()
# print(p)



