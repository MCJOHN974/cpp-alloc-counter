from enum import Enum
from Codelines import Codelines
from Atoms import Atoms
from CodelinesWithoutDeclarations import CodelinesWithoutDeclarations

class Method(Enum):
    STACK = 0
    HEAP = 1
    STATIC = 2


def CountConstructors(lines : Codelines) -> dict:
    res = {}
    classSpace = False
    opened = 0
    currentClass = 'rgouwqrogrurqguogrqouqgr'
    line = lines.Begin()
    while not line.IsEnd():
        code = ' ' + line.Code()
        if ' class ' in code:
            classSpace = True
            currentClass = code.split(' ')[2]
        if opened == 1 and classSpace and (code.replace(' ', '').replace('\t', ''))[:len(currentClass)] == currentClass:
            if currentClass in res:
                res[currentClass] += 1
            else:
                res[currentClass] = 1
        if '{' in code:
            opened += 1
        if '}' in code:
            opened -= 1
        if opened == 0:
            classSpace = False
        line.Next()
    return res



class ClassList:
    def __init__(self, codelines : Codelines) -> None:
        self.__codelines = codelines
        # TBD: change to binary tree
        self.__classes = []
        line = self.__codelines.Begin()
        while not line.IsEnd():
            if line.Code()[:5] == "class":
                for char in ('', '*', '&'):
                    self.__classes.append((line.Code()[6:line.Code().find(' ', 6)] + char))
            line.Next()
        self.__classes.sort(key = lambda x: (-1 * len(x), x))
        self.__constructors = CountConstructors(self.__codelines)
        self.__codelines = CodelinesWithoutDeclarations(self.__codelines)
        print(*self.__codelines.lines)


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
                            print(line.Code())
                        else:
                            res[objclass][2] += 1
                    atom.Next()
            line.Next()
        rres = {}
        for key in res:
            if key[-1] != '*' and key[-1] != '&':
                constructors = 0
                if key in self.__constructors:
                    constructors = self.__constructors[key]
                rres[key] = res[key]
                rres[key][1] -= constructors
        return rres


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
            return (Method.HEAP, objectClass[:-1])
        if "static" in code:
            return (Method.STATIC, objectClass)
        return (Method.STACK, objectClass)
