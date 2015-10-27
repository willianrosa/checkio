import re
VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
REGEXVOWELS='[%s]' % VOWELS
REGEXCONSONANTS='[%s]' % CONSONANTS
​
def checkio(text):
    text=re.sub('\d','0',text.upper())
    text=re.sub(REGEXVOWELS,'0',text)
    text=re.sub(REGEXCONSONANTS,'1',text)
    text=re.sub('\W',' ',text)     
    return sum([re.search('(00|11)',i) is None and len(i) > 1 for i in text.split()])
​
​
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"My name is ...") == 3, "All words are striped"
    assert checkio(u"Hello world") == 0, "No one"
    assert checkio(u"A quantity of striped words.") == 1, "Only of"
    assert checkio(u"Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"