def RemoveDeclarations(lines : list) -> list:
    res = []
    opened = 0
    classScope = False
    for line in lines:
        if 'class' in line:
            classScope = True
        if '{' in line:
            opened += 1
        if '}' in line:
            opened -= 1
        if opened == 0:
            classScope = False
        if not (classScope and opened == 1 and (line.replace('\n', '').replace(' ', '').replace('\t', ''))[-1] == ';'):
            res.append(line)
    return res

from Codelines import Codelines

class CodelinesWithoutDeclarations:
    def __init__(self, lines : Codelines) -> None:
        self.lines = RemoveDeclarations(lines.lines)


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
        return self.Iterator(self.lines, len(self.lines), 0)
