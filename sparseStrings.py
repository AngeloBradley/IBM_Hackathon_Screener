from TestSuite import GenerateSparseStringsData_GenerateExpectedValues
from TestSuite import GenerateStringsList_GenerateQueriesList
from TestSuite import ConvertToInt

def matchingStrings(strings, queries):
    found = {}
    #Here, the strings are counted and stored in a dictionary where the string is associated with the number of times it appears. 
    #The dictionary is used for faster retrieval during the next phase. 
    for string in strings:
        if string in found:
            found[string] = found[string] + 1
        else:
            found[string] = 1
    
    queryCount = []
    
    #Here, the dictionary of found strings is checked against individual queries. If the query is found, the associated value
    #is appended on the bottom of a list of query counts. 
    #If the query is not in the dictionary, a 0 is pushed into the list instead. 
    for query in queries:
        if query in found:
            queryCount.append(found[query])
        else:
            queryCount.append(0)
    
    return queryCount

if __name__ == '__main__':
    print('**************************************************************************************************')
    print()
    print(' If the size of the list is greater than 5, the visible list is only a subset of the actual list. ')
    print()
    print('**************************************************************************************************')
    print()
    print()

    for i in range(1, 6):
        iString = str(i)
        content = GenerateSparseStringsData_GenerateExpectedValues('Data' + iString + '.txt')
        strings, queries = GenerateStringsList_GenerateQueriesList(content)
        expected = ConvertToInt(GenerateSparseStringsData_GenerateExpectedValues('expected' + iString + '.txt'))
        
        output = matchingStrings(strings, queries)
        print('Test ' + iString + ': ')
        print('Strings(' + str(len(strings)) + '): ', end='')
        print(strings[:5])
        print('Queries(' + str(len(queries)) + '): ', end='')
        print(queries[:5])
        print('Expected Output: ', end='')
        print(expected[:5])
        print('Actual Output: ', end='')
        print(output[:5])

        if output == expected:
            print('Test Succeeded')
        else:
            print('Test Failed')
        print()
        print()
