#include "A.h"
#include "B.h"

class C {
public:
    C(A a, B b) {}
};

int main() {
    C* c = new C(A(2), B("eo"));
    delete c;
}
