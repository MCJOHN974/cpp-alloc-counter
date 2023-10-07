# cpp-alloc-counter
A tool to count a number of heap, stack and static creations in the program

## Dependencies
You just need to install a python3:
```
sudo apt install python3 -y
```

## How to use:
Run main with a directory of your program as a argument:
```
python3 src/main.py <directory with C++ code>
```
For example, runned in test/simple will give next output:
```
$ python3 src/main.py test/simple
Class   Heap    Stack   Static
B       0       2       0
C       1       1       0
AAA     1       0       1
```

bebera