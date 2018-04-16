import operator
import re

def checkio(text):
    pattern = r'[a-zA-Z]'
    letters = re.findall(pattern, text.lower())
    letters_sorted = sorted(letters)
    letters_dict = {}
    for letter in letters_sorted:
       letters_dict.update({letter:letters_dict.get(letter,0) + 1})
    letter = max(letters_dict,key=lambda k: letters_dict[k])
    return letter

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")

