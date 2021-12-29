from demo import substract

def testSubstract():
    assert substract(5, 3) == 2
    assert substract(10, 5) == 5
    print ("Add function works correctly.")

if __name__ == '__main__':
    testSubstract()