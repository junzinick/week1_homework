"""
Challenge: solve the equation:

(a + (b - c) * d - e) * f = 75

where a, b, c, d, e, and f are unique integers in the range [1, 6].

Hints:

Computers are so fast that your program can simply try all possible valid values of a, b, c, d, e, and f until it finds one permutation of 1-6 that solves the challenge! 
(Btw, there is only one permutation that will solve it.)
Use 6 nested for-loops to enumerate all ways of setting each of a, b, c, d, e, and f to the values 1-6.
Use if-statements to ensure all values of a, b, c, d, e, and f are valid. (I.e. to ensure that each value is unique)
Use an if-statement to test if the current permutation solves the challenge.
"""
# Python function to print permutations of a given list
"""
a=−bdf+cdf+2.718282f+75
------------------------
f
"""

"""
def multi_table(a,b,c,d,e,f):
    for i in range(1,6):
        print('{0:.2f} // {1:.2f} = {2:.2f}'.format(a,i, a/i))
if __name__ == "__main__":
    a = input('enter a number: ')
    multi_table(float(a))
"""

def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return


