from ClassList import ClassList
from Codelines import Codelines
from colorama import Fore, Back, Style
import sys


OK = 0
FAIL = 0

def Results() -> None:
    print("\nTOTAL:")
    print(Fore.GREEN + f"Passed : {OK}")
    if FAIL > 0:
        print(Style.RESET_ALL, end='')
        print(Fore.RED, end='')
    print(f"Failed : {FAIL}")


def Assert(test, creations, object, expected) -> None:
    global OK
    global FAIL
    try:
        assert creations[object] == expected
        print(f"test : {test}, class : {object} -- {Fore.GREEN}OK{Style.RESET_ALL}")
        OK += 1
    except Exception as e:
        print(f"\ntest : {test}, class : {object} -- {Fore.RED}FAIL{Style.RESET_ALL}")
        print(f"Creations of {object} :")
        print(f"Expected : {expected}")
        print(f"Finded   : {creations[object]}")
        FAIL += 1


# simple
def test1() -> None:
    creations = ClassList(Codelines("test/simple")).CountCreations()


    def Assert1(obj, exp):
        Assert('simple', creations, obj, exp)


    Assert1('AAA', [1, 0, 1])
    Assert1('B', [0, 2, 0])
    Assert1('C', [1, 1, 0])


# complicated-line
def test2() -> None:
    creations = ClassList(Codelines("test/complicated-line")).CountCreations()

    def Assert2(obj, exp):
        Assert('complicated-line', creations, obj, exp)


    Assert2('A', [1, 0, 0])
    Assert2('B', [0, 2, 0])
    Assert2('C', [0, 2, 0])


# many-files
def test3() -> None:
    creations = ClassList(Codelines("test/many-files")).CountCreations()

    def Assert3(obj, exp):
        Assert('many-files', creations, obj, exp)


    Assert3('A', [0, 2, 0])
    Assert3('B', [0, 2, 0])
    Assert3('C', [1, 0, 0])    


# references
def test4() -> None:
    creations = ClassList(Codelines("test/references")).CountCreations()

    def Assert3(obj, exp):
        Assert('references', creations, obj, exp)


    Assert3('A', [0, 1, 0])   


if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    Results()
    sys.exit(FAIL)
