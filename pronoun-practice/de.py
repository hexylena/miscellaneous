#!/usr/bin/env python3
# encoding=utf-8
import os
import random
import time

LOGFILE = os.path.join(os.path.expanduser("~"), '.de_practice')

prep = {
    'akk': ['bis', 'durch', 'für', 'gegen', 'ohne', 'um', 'entlang'],
    'dat': ['ab', 'aus', 'bei', 'mit', 'nach', 'seit', 'außer', 'von', 'zu'],
    'wechselpräpositionen': ['an', 'auf', 'hinter', 'in', 'neben', 'über', 'unter', 'zwischen', 'vor']
}

prep_immer = {
    'akk': {
        'intressantent': 'für',
        'ärger': 'über',
        # 'gewoher': 'an',
        'freuen': 'auf',
        'warten': 'auf',
    },
    'dat': {
        'anfangen': 'mit',
        'einladen': 'mit',
        'angst haben': 'vor',
        'sich treffen': 'mit',
        'helfen': 'bei',
    }
}


trennbare_prefixes = [
    # Mit
    'an', 'auf', 'ab', 'zurück', 'vor', 'bei',
    # Trenn das verb in zwei //
    'los', 'weg', 'nach', 'zu', 'aus', 'ein',
    # Bring ans End das muss sein
    # Other ones that don't fit in the nice rhyme.
    'fern', 'her', 'mit', 'statt', 'teil', 'um', 'weiter', 'zurecht',
    'zusammen',
]

nouns = {
    'm': [('Man', 'Mann'), ('Bird', 'Vogel')],
    'f': [('Woman', 'Frau'), ('Flower', 'Blumen')],
    'n': [('Child', 'Kind'), ('Fruit', 'Obst')],
    'pl': [('Children', 'Kinder')],
}

pp = {
    'i': {'nom': 'ich', 'akk': 'mich', 'dat': 'mir'},
    'you': {'nom': 'du', 'akk': 'dich', 'dat': 'dir'},
    'he': {'nom': 'er', 'akk': 'ihn', 'dat': 'ihm'},
    'she': {'nom': 'sie', 'akk': 'sie', 'dat': 'ihr'},
    'it': {'nom': 'es', 'akk': 'es', 'dat': 'ihm'},
    'we': {'nom': 'wir', 'akk': 'uns', 'dat': 'uns'},
    "y'all": {'nom': 'ihr', 'akk': 'euch', 'dat': 'euch'},
    "you/y'all (polite)": {'nom': 'Sie', 'akk': 'Sie', 'dat': 'Ihnen'},
}

arts = {
    'the': {
        ('m', 'nom'): {'_': 'der'},
        ('m', 'akk'): {'_': 'den'},
        ('m', 'dat'): {'_': 'dem'},
        ('m', 'gen'): {'_': 'des', 'ns': 's'},

        ('f', 'nom'): {'_': 'die'},
        ('f', 'akk'): {'_': 'die'},
        ('f', 'dat'): {'_': 'der'},
        ('f', 'gen'): {'_': 'der'},

        ('n', 'nom'): {'_': 'das'},
        ('n', 'akk'): {'_': 'das'},
        ('n', 'dat'): {'_': 'dem'},
        ('n', 'gen'): {'_': 'des', 'ns': 's'},

        ('pl', 'nom'): {'_': 'die'},
        ('pl', 'akk'): {'_': 'die'},
        ('pl', 'dat'): {'_': 'den', 'ns': 'n'},
        ('pl', 'gen'): {'_': 'der'},
    },
    'a': {
        ('m', 'nom'): {'_': 'ein'},
        ('m', 'akk'): {'_': 'einen'},
        ('m', 'dat'): {'_': 'einem'},
        ('m', 'gen'): {'_': 'eines', 'ns': 's'},

        ('f', 'nom'): {'_': 'eine'},
        ('f', 'akk'): {'_': 'eine'},
        ('f', 'dat'): {'_': 'einer'},
        ('f', 'gen'): {'_': 'einer'},

        ('n', 'nom'): {'_': 'ein'},
        ('n', 'akk'): {'_': 'ein'},
        ('n', 'dat'): {'_': 'einem'},
        ('n', 'gen'): {'_': 'eines', 'ns': 's'},
    }
}

case_names = {
    'nom': 'nominative',
    'akk': 'accusative',
    'dat': 'dative',
    'gen': 'genative',
}


try:
    if random.random() < 0.3:
        case = random.choice(list(prep.keys()))
        prep = random.choice(prep[case])

        print("[prep] What case for %s" % prep)
        asked = time.time()
        expected = case
        observed = input("Answer: ").strip()
        answered = time.time()

        if observed != expected[0:3]:
            print("WRONG:", expected[0:3])
        else:
            if answered - asked < 5:
                print("Acceptable.")
            else:
                print("Slow.")

        with open(LOGFILE, 'a') as handle:
            handle.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (asked, '_prep_', '', case, observed == expected[0:3], observed, expected[0:3], answered - asked))
    elif random.random() < 0.7:
        defindef = random.choice(list(arts.keys()))
        (gender, case) = random.choice(list(arts[defindef]))
        noun_en, noun_de = random.choice(nouns[gender])
        print("Translate: %s %s as %s" % (defindef, noun_en, case_names[case]))
        asked = time.time()
        parts = arts[defindef][(gender, case)]
        expected = parts['_'] + ' ' + noun_de + parts.get('ns', '')
        observed = input("Answer: ").strip()
        answered = time.time()

        if observed != expected:
            print("WRONG:", expected)
        else:
            if answered - asked < 5:
                print("Acceptable.")
            else:
                print("Slow.")

        with open(LOGFILE, 'a') as handle:
            handle.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (asked, defindef, gender, case, observed == expected, observed, expected, answered - asked))
    else:
        pronoun = random.choice(list(pp.keys()))
        case = random.choice(list(pp[pronoun].keys()))
        print("Translate: %s %s" % (pronoun, case_names[case]))
        asked = time.time()
        expected = pp[pronoun][case]
        observed = input("Answer: ").strip()
        answered = time.time()

        if observed != expected:
            print("WRONG:", expected)
        else:
            if answered - asked < 5:
                print("Acceptable.")
            else:
                print("Slow.")

        with open(LOGFILE, 'a') as handle:
            handle.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (asked, '_pronoun_', pronoun, case, observed == expected, observed, expected, answered - asked))
except KeyboardInterrupt:
    pass
