from anytree import NodeMixin
from StorageClass import Storage
import re
import pymorphy2

class AbstractLine:


    @staticmethod
    def is_rhyme(l1, l2):
        _POS = {True: 0.0, False: -1.0}
        _SAMEWORD = {True: -1.0, False: 0.0}
        _WOV = {True: 0.0, False: -1.0}
        _PRE = {True: 0.0, False: -0.25}
        _POST = {True: 0.0, False: -0.25}


        pos_equal = l1.rhyme_params['pos'] == l2.rhyme_params['pos']
        same_word = l1.words[-1] == l2.words[-1]
        wov_equal = l1.rhyme_params['wovel'] == l2.rhyme_params['wovel']
        pre_equal = l1.rhyme_params['pre'] == l2.rhyme_params['pre']
        post_equal = l1.rhyme_params['post'] == l2.rhyme_params['post']
        rhyme_coeff = 1 + _POS[pos_equal] + _WOV[wov_equal] + _PRE[pre_equal] +\
                      _POST[post_equal] + _SAMEWORD[same_word]
        return rhyme_coeff


class Line(NodeMixin, AbstractLine):

    def __init__(self, text: str, words=[], accents=[], acc_scheme=[], children=None, parent=None):

        self.text = text
        self.words = words
        self.words_normal = []
        self.accents = accents
        self.acc_scheme = acc_scheme
        self.rhyme_params = {}


    def new_rhyme_params(self):
        self.rhyme_params['pos'] = self.acc_scheme[::-1].index(1)
        self.rhyme_params['wovel'] = self.text[self.accents[-1]]
        post = ""
        if self.accents[-1] < len(self.text) -1:
            post = self.text[self.accents[-1] + 1]
        self.rhyme_params['post'] = post
        self.rhyme_params['pre'] = self.text[self.accents[-1] - 1]
        morph = pymorphy2.MorphAnalyzer()
        for i in self.words:
            self.words_normal.append(morph.parse(i)[0].normal_form)

    def generate_export(self, id):
        exp = {}
        exp['id'] = id
        exp['text'] = self.text
        signature = ""
        for n in self.acc_scheme:
            signature+=str(n)
        exp['signature'] = signature
        accent1 = {}
        accent1['slog'] = self.accents[-1]
        accent1['l_acc'] = self.rhyme_params["wovel"]
        accent1['l_before'] = self.rhyme_params["pre"]
        accent1['l_after'] = self.rhyme_params["post"]
        exp['accents'] = [accent1]
        exp_words = []
        for i in range(len(self.words)):
            exp_word = {}
            exp_word["word_str"] = self.words[i]
            exp_word["word_normal"] = self.words_normal[i]
            exp_words.append(exp_word)
        exp["words"] = exp_words
        return exp




