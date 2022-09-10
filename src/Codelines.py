import os


def RemoveScope(line : str) -> str:
    pos = line.find('::')
    if pos == -1:
        return line
    original = pos
    while pos > -1 and line[pos] not in (' ', '\n', '\t', '(', '[', '{'):
        pos -= 1
    return RemoveScope(line[:pos + 1] + line[original + 2:])


class Codelines:
    def __init__(self, dir : str) -> None:
        self.__lines = []
        for file in os.listdir(dir):
            with open(dir + '/' + file, "r") as f:
                self.__lines += [RemoveScope(line) for line in f.readlines() if line[0] != '#']
        print(*self.__lines, sep='\n')


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
        return self.Iterator(self.__lines, len(self.__lines), 0)
