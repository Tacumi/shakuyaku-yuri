import random
class Word:
    def __init__(self, yo, mi):
        self.yomi = yo
        self.midasi = mi
def generate(w3,w4,w5):
    ww3 = random.choice(w3)
    ww4 = random.choice(w4)
    ww5 = random.choice(w5)
    return "立てば" + ww4.yomi + " 座れば" + ww3.yomi + " 歩く姿は" + ww5.yomi

with open ("fields.dat") as file:
    word3 = []
    word4 = []
    word5 = []
    for line in file:
        line = line[:-1]
        words = line.split(',')
        if len(words) < 2:
            continue
        mrph = Word(words[1], words[0])
        if len(mrph.midasi) == 3:
            word3.append(mrph)
        elif len(mrph.midasi) == 4:
            word4.append(mrph)
        elif len(mrph.midasi) == 5:
            word5.append(mrph)
        else:
            pass
    print(generate(word3, word4, word5))

