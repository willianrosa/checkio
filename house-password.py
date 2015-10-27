#coding: utf-8
import re
def checkio(data):    
    return not re.compile(r"(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])")\
        .match(data) is None\
        and data.__len__() >= 10


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u'A1213pokl') == False, "1st example"
    assert checkio(u'bAse730onE4') == True, "2nd example"
    assert checkio(u'asasasasasasasaas') == False, "3rd example"
    assert checkio(u'QWERTYqwerty') == False, "4th example"
    assert checkio(u'123456123456') == False, "5th example"
    assert checkio(u'QwErTy911poqqqq') == True, "6th example"