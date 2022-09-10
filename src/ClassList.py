from enum import Enum
from Codelines import Codelines
from Atoms import Atoms


class Method(Enum):
    STACK = 0
    HEAP = 1
    STATIC = 2


class ClassList:
    def __init__(self, codelines : Codelines) -> None:
        self.__codelines = codelines
        self.__classes = set()
        line = self.__codelines.Begin()
        while not line.IsEnd():
            if line.Code()[:5] == "class":
                for char in ('', '*', '&'):
                    self.__classes.add(line.Code()[6:line.Code().find(' ', 6)] + char)
            line.Next()


    # returns a dict where key = name of class, value = list of three integers --
    # number of heap stack and static objects created
    def CountCreations(self) -> dict:
        res = dict()
        for className in self.__classes:
            res[className] = [0, 0, 0]
        line = self.__codelines.Begin()
        while not line.IsEnd():
            if self.__HasObjectCreation(line.Code()):
                atom = Atoms(line.Code()).Begin()
                while not atom.IsEnd():
                    if self.__HasObjectCreation(atom.Code()):
                        method, objclass = self.__WhichCreation(atom.Code())
                        if method == Method.HEAP:
                            res[objclass][0] += 1
                        elif method == Method.STACK:
                            res[objclass][1] += 1
                        else:
                            res[objclass][2] += 1
                    atom.Next()
            line.Next()
        return res


    def PrintReport(self) -> None:
        creations = self.CountCreations()
        print("Class", "Heap", "Stack", "Static", sep='\t')
        for obj in creations:
            print(obj, creations[obj][0], creations[obj][1], creations[obj][2], sep='\t')


    # here code can be both codeline or atom
    def __HasObjectCreation(self, code : str) -> bool:
        for className in self.__classes:
            if className in code and 'class' not in code:
                return True
        return False


    # here code can be ONLY an atom
    def __WhichCreation(self, code : str) -> tuple((Method, str)):
        objectClass = ""
        for className in self.__classes:
            if className in code:
                objectClass = className
                break
        if "new" in code:
            return (Method.HEAP, objectClass)
        if "static" in code:
            return (Method.STATIC, objectClass)
        return (Method.STACK, objectClass)
