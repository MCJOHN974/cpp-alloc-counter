from enum import Enum
from Codelines import Codelines
from Atoms import Atoms


class Method(Enum):
    STACK = 1
    HEEP = 2
    STATIC = 3


class ClassList:
    def __init__(self, codelines : Codelines) -> None:
        self.__codelines = codelines


    # returns a dict where key = name of class, value = tuple of three integers --
    # number of heap stack and static objects created
    def CountCreations(self) -> dict:
        pass


    # here code can be both codeline or atom
    def __HasObjectCreation(self, code : str) -> bool:
        pass


    def __WhichCreation(self, code : str) -> (method : Method, class : str):
        pass