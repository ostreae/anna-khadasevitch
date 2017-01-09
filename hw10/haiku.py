import random


def punctuation():
    marks = ['!', '.', '...']
    return random.choice(marks)


def nouns(mean):
    noun_s = ['la neige', 'la merde', 'le chat', 'le chien', 'la nuit', 'le doigt', 'le pied', 'la branche', 'la ville', 'le lit', 'la salle', 'le soir', 'le cul', 'le lait']
    noun_pl = ['les cheveux', 'les châteaux', 'les genoux', 'les vitraux']
    noun_fem = ['tête', 'femme', 'veuve', 'sotte', 'brune', 'mère', 'tante']
    noun_geo = ['l\'Asie', 'l\'Afrique', 'l\'Europe', 'la France']
    if mean == 's':
        return random.choice(noun_s)
    elif mean == 'pl':
        return random.choice(noun_pl)
    elif mean == 'fem':
        return random.choice(noun_fem)
    else:
        return random.choice(noun_geo)


def verbs():
    verb = ['quitte', 'donne', 'laisse', 'est', 'dit', 'paie', 'soigne']
    return random.choice(verb)


def adjectives():
    adjective = ['français', 'orange', 'marron', 'rapids', 'idéaux', 'heureux']
    return random.choice(adjective)


def interjections():
    interjection = ['ah', 'aie', 'crac', 'diable', 'boum', 'ouf']
    return random.choice(interjection)


def prepositions():
    preposition = ['sur', 'au', 'dans', 'chez', 'sous']
    return random.choice(preposition)


def indicators():
    indicator = ['cette', 'ma', ]
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



