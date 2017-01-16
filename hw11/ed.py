#сколько в тексте форм на -ed, а также сколько
# из них образованы от глаголов на -y  или -e
# (например, studied, lied).

def fileopen(file_name, words):
    words = []
    file_name = input()
    with open(file_name, "r", encoding="utf-8") as f:
        for line in f.readlines():
            words += [words.strip('.,!?:;') for words in line.split()]
        return words


def ed_count(sum, words, ed_words):
    ed_sum = 0
    ed_words = []
    for word in words:
        if word.endswith('ed') == True:
            ed_sum += 1
            ed_words.append(word)
    return ed_sum


def ied_count(ied_sum, ed_words):
    ied_sum = 0
    for i in ed_words:
        if i.endswith ('ied') == True:
            ied_sum += 1
    return ied_sum
