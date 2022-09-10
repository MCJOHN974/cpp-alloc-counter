#  A* a = new A(B(2) + C("eo"));
#  atoms here will be:
#  1) B;
#  2) C;
#  5) A* a = new A;
#  I claim that each atom contains one or zero object creation.


class Atoms:
    # later, when we teach the code to make a differ between * as a multiplication and * as a pointer 
    # here will be a '*' special character
    __special_characters = frozenset((',', '+', '-', '+=', '-=', '<<', '>>', '/', '/=', '*='))


    def __init__(self, codeline : str) -> None:
        self.__atoms = self.__GenerateAtoms(codeline.replace('{', '').replace('}', '').replace(';', ''))
        print(*self.__atoms, sep='\n')


    def __GenerateAtoms(self, codeline : str) -> list:
        for i in range(len(codeline)):
            if codeline[i] in self.__special_characters:
                return self.__GenerateAtoms(codeline[:i]) + self.__GenerateAtoms(codeline[i + 1:])
            if codeline[i] == '(':
                j = self.__FindClose(codeline, i)
                return self.__GenerateAtoms(codeline[:i] + codeline[j + 1:]) + self.__GenerateAtoms(codeline[i+1:j])
        return [codeline]


    def __FindClose(self, codeline : str, open : int) -> int:
        opened = 1
        close = open
        while opened != 0:
            close += 1
            if codeline[close] == '(':
                opened += 1
            if codeline[close] == ')':
                opened -= 1
        return close


    class Iterator:
        def __init__(self, lst : list, len : int, pos : int) -> None:
            self.__lst = lst
            self.__len = len
            self.__pos = pos


        def Next(self) -> None:
            self.__pos += 1


        def Code(self) -> str:
            return self.__lst[self.__pos]


        def IsEnd(self) -> bool:
            return self.__pos >= self.__len


    def Begin(self) -> Iterator:
        return self.Iterator(self.__atoms, len(self.__atoms), 0)