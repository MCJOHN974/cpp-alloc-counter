class B {
public:
    B(int x){}
};
#include <string>
class C {
public:
    C(std::string s) {}
};

class A {
public:
    A(B b, C c) {}
};

int main() {
    A* a = new A(B(2), C("eo"));
    delete a;
}