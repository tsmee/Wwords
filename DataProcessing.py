import re
from text import text
import simplejson


class Data:


    def __init__(self):

        self.words = text.split()
        self.lines = []
        self.lines_ready = []

    def is_pretty(self, phrase):
        if len(self.words[phrase[-1]]) <= 3:
            return False
        return True

    def prepare_lines(self):

        words_slogi = []
        for n in self.words:
            sl = 0
            for i in n:
                if i in 'аеиуоыэюя':
                    sl += 1

            words_slogi.append(sl)

        phrases = []
        for i in range(len(words_slogi) - 3):
            phrase = [i]
            slogi = words_slogi[i]
            count = 1
            while slogi <= 8:
                phrase.append(i + count)
                slogi += words_slogi[i + count]
                count += 1
                if slogi == 7 or slogi == 8 or (i + count) == len(words_slogi):
                    if self.is_pretty(phrase):
                        phrases.append(phrase)
                    break

        raw_lines = []
        for f in phrases:
            string = ""
            for i in f:
                string += self.words[i] + " "
            if not re.search('^[a-zA-Z]+$', string):
                raw_lines.append(string.strip(",").strip())
        self.lines = raw_lines

    def get_accent(self):
        lines_ready = []
        from russtress import Accent
        accent = Accent()
        for line in self.lines:
            acc_line = accent.put_stress(line, "^")
            scheme = []
            accents = []
            for i in range(len(acc_line)):
                if acc_line[i] in 'аеёиуоыэюя':
                    scheme.append(0)
                elif acc_line[i] == '^':
                    print(acc_line)
                    scheme[-1] = 1
                    accents.append(i - (len(accents) + 1))
            lines_ready.append([line, accents, scheme])
        self.lines_ready = lines_ready

    def save_to_file(self):
        f = open('output.txt', 'w')
        simplejson.dump(self.lines_ready, f)
        f.close()

    def read_from_file(self):
        with open('output.txt', 'r') as f:
            a = simplejson.loads(f.read())
        self.lines_ready = a












