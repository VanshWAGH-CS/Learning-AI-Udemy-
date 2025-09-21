#method Resolution object (MRO)

class A:
    label = "A: Base class"


class B(A):
    label = "B: Masala blend"


class C(A):
    label = "C: Herbal blend"


class D(B, C):#which ever is the first class it's method will be called
    pass


cup = D()
print(cup.label)
print(D.__mro__)#it's is dunder