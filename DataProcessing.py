from text import text
#


class Data:

    def __init__(self):

        self.words = text.split()
        self.lines = []
        self.lines_ready = []

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
                    phrases.append(phrase)
                    break

        raw_lines = []
        for f in phrases:
            string = ""
            for i in f:
                string += self.words[i] + " "
            raw_lines.append(string)
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
                if acc_line[i] in 'аеиуоыэюя':
                    scheme.append(0)
                elif acc_line[i] == '^':
                    scheme[-1] = 1
                    accents.append(i - (len(accents) + 1))
            lines_ready.append([line, accents, scheme])
        self.lines_ready = lines_ready


# d = Data()
#
# d.prepare_lines()
#
# d.get_accent()
# print(d.lines_ready)




