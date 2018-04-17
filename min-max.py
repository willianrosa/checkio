def min(*args, **kwargs):
    key = kwargs.get("key", None)
    return sorted(get_args(args), key=key, reverse=False)[0]
    
def max(*args, **kwargs):
    key = kwargs.get("key", None)
    return sorted(get_args(args), key=key, reverse=True)[0]

def get_args(args):
    if len(args) == 1:
        args = list(args[0])
    else:
        args = list(args)
    return args

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max([1, 2, 3], [5, 6], [7], [0, 0, 0, 1]) == [7]
    assert min(abs(i) for i in range(-10, 10)) == 0
    assert max(range(6)) == 5
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
