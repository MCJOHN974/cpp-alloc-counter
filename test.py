from os import system


system("touch tmp")
system("python3 src/main.py test/simple > tmp")
with open("tmp", "r") as test1:
    lines = test1.readlines()
    print(lines[0])
    assert lines[0] == "Class\tHeap\tStack\tStatic"
    assert lines[1] == "C\t1\t1\t0"
    assert lines[2] == "B\t0\t1\t0"
    assert lines[3] == "AAA\t1\t0\t1"
system("rm tmp")
print("Test1 OK")
