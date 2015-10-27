#coding: utf-8
def checkio(data):
    if len(data) % 2:
        return sorted(data)[len(data)/2]
    else: return reduce(lambda x,y: (x+y)/2.0,sorted(data)[(len(data)/2)-1:(len(data)/2)+1])

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    print("Start the long test")
    assert checkio(range(1000000)) == 499999.5, "Long."
    print("The local tests are done.")