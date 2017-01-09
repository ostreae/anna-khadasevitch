import random


def makelist(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        for line in f.readlines():
            words = line.split(',')
            words[-1] = words[-1].strip('\n')
        return words


def punctuation():
    marks = makelist('punctuation.txt')
    return random.choice(marks)


def nouns(mean):
    noun_s = makelist('noun_s.txt')
    noun_pl = makelist('noun_pl.txt')
    noun_fem = makelist('noun_fem.txt')
    noun_geo = makelist('noun_geo.txt')
    if mean == 's':
        return random.choice(noun_s)
    elif mean == 'pl':
        return random.choice(noun_pl)
    elif mean == 'fem':
        return random.choice(noun_fem)
    else:
        return random.choice(noun_geo)


def verbs():
    verb = makelist('verbs.txt')
    return random.choice(verb)


def adjectives():
    adjective = makelist('adjectives.txt')
    return random.choice(adjective)


def interjections():
    interjection = makelist('interjections.txt')
    return random.choice(interjection)


def prepositions():
    preposition = makelist('prepositions.txt')
    return random.choice(preposition)


def indicators():
    indicator = makelist('indicators.txt')
    return random.choice(indicator)


def verse1():
    return nouns('s') + ' ' + verbs() + ' ' + nouns('s') + punctuation()
print(verse1())


def verse2():
    return interjections() + punctuation() + ' ' + prepositions() + ' ' + indicators() + ' ' + nouns('fem') + ' est' + ' ' + nouns('geo')
print(verse2())


def verse3():
    return nouns('pl') + ' ' + adjectives() + punctuation()
print(verse3())
