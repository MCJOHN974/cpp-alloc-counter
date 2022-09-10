#  A* a = new A(B(2) + C("eo"))
#  atoms here will be:
#  1) B(2)
#  2) C("eo")
#  3) operator+(1, 2)
#  4) new A(3)
#  5) A* a = 4
#  I claim that each atom contains one or zero object creation.
class Atoms:
    def __init__(self, codeline : str) -> None:
        pass


    class Iterator:
        def __init__(self) -> None:
            pass


        def Next(self) -> None:
            pass


        def Code(self) -> str:
            pass


        def IsEnd(self) -> bool:
            pass


    def Begin(self) -> Iterator:
        pass
