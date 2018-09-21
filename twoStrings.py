from TestSuite import TwoSparseStringsTests

def twoStrings(s1, s2):
    '''since the existence of a substring, any substring, is all that is being proven and since the substring
    can be as small as a single character, a single character match is all that is being checked for. 
    '''
    for letter in s1:
        if letter in s2:
            #the method terminates as soon as the first match is made
            return 'YES'
    #if the method reaches this return statement, no match was found
    return 'NO'


if __name__ == '__main__':
    for i in range(0,10):
        s1, s2, expectedAnswer = TwoSparseStringsTests(i)
        print("String 1: " + s1)
        print("String 2: " + s2)
        print("Expected Answer: " + expectedAnswer)
        print("Answer: " + twoStrings(s1, s2))
        print()

