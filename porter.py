def is_vowel(letter):
    return letter.lower() in 'aeiou'    

def form(word):
    foo = []
    foo.append('V' if is_vowel(word[0]) else 'C')
    for i in word[1:]:
        typ = 'V' if is_vowel(i) or (i.lower() == 'y' and foo[-1] == 'C') else 'C'
        if foo[-1] != typ:
            foo.append(typ)
    return "".join(foo)

def is_cvc(stem):
    return 'CVC' == "".join(['V' if ((is_vowel(x) or (x.lower() == 'y')) and (not stem[-1] in 'wxy')) else 'C' for x in stem[-3:]])  

def get_m(word):
    return form(word).count('VC')

def step1a(word):
    endings = {'sses' : 'ss',
                'ies' : 'i',
                'ss' : 'ss',
                's' : ''}
    for i in endings:
        if word.endswith(i):
            return word[:word.rfind(i)] + endings[i]
    return word

def step1b(word):
    if get_m(word) and word.endswith('eed'):
        return word[:-3] + 'ee'
    for i in ('ed','ing'):
        if word.endswith(i) and ('V' in form(word[:word.rfind(i)])):
            return step1b_part2(word[:word.rfind(i)])
    return word

def step1b_part2(stem):
    for i in ('at','bl','iz'):
        if stem.endswith(i):
            return stem + 'e'
    if (stem[-1] == stem[-2]):
        return stem if stem[-2:] in ('ll','ss','zz') else stem[:-1]
    if get_m(stem) == 1 and is_cvc(stem):
        return stem + 'e'
    return stem

def step1c(word):
    return word[:-1] + 'i' if word.endswith('y') and any([is_vowel(x) for x in word]) else word

def step2(word):
    endings = {'ational':'ate',
                'tional':'tion',
                'enci':'ence',
                'anci':'ance',
                'izer':'ize',
                'abli':'able',
                'alli':'al',
                'entli':'ent',
                'eli':'e',
                'ousli':'ous',
                'ization':'ize',
                'ation':'ate',
                'ator':'ate',
                'alism':'al',
                'iveness':'ive',
                'fulness':'ful',
                'ousness':'ous',
                'aliti':'al',
                'iviti':'ive',
                'biliti':'ble'}
    for i in endings:
        if word.endswith(i) and form(word[:word.rfind(i)]).count('VC'):
            return word[:word.rfind(i)] + endings[i]
    return word

def step3(word):
    endings = {'icate':'ic',
                'ative': '',
                'alize':'al',
                'iciti':'ic',
                'ical':'ic',
                'ful':'',
                'ness':''}
    for i in endings:
        if word.endswith(i):
            return word[:word.rfind(i)] + endings[i]
    return word

def step4(word):
    endings = ('al','ance','ence','er','ic','able','ible','ant','ement','ment',
                'ent','ou','ism','ate','iti','ous','ive','ize','tion','sion')
    if get_m(word) > 1:
        for i in endings:
            if word.endswith(i):
                return word[:word.rfind(i)] if not word[-4] in ('t','s') else word[:word.rfind(i) + 1]
    return word

def step5a(word):
    f = form(word)
    m = get_m(word)
    if ((m > 1) and (word.endswith('e'))) or (m == 1 and is_cvc(word)):
        return word[:-1]
    return word

def step5b(word):
    return word[:-1] if (get_m(word) > 1) and (word.endswith('ll')) else word

def porter_stem(word):
    for step in [step1a,step1b,step1c,step2,step3,step4,step5a,step5b]:
        word = step(word)
    return word
