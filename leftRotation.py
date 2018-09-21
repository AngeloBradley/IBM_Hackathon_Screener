from random import randint
from TestSuite import LeftRotationTests

def rotateLeft(n, d):
    #this method pushes the value at the head of the list onto the tail and then deletes the head
    for i in range(0, d):
        n.append(n[0])
        del n[0]

    return n

if __name__ == '__main__':

    print('**If the size of the list is greater than 20, the visible list is only a subset of the actual list.')
    print()
    print()

    for i in range(0, 7):
        
        numRotations, original, expected = LeftRotationTests(i)

        print('Size of List: ', end='')
        print(len(original))
        print('Initial List (n): ', end='')
        print(original[:20])
        print('Number of Rotations (d): ', end='')
        print(numRotations)
        print('Expected List: ', end='')
        print(expected[:20])
        print('My List: ', end='')
        rotated = rotateLeft(original, numRotations)
        print(rotated[:20])

        if rotated == expected:
            print('Successful Rotation')
        else:
            print('Rotation Unsuccessful')
        print()
