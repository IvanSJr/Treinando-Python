class A:
    vc = 123


a1 = A()
a2 = A()
a3 = A()
a4 = A()
a2.vc = 321  # Só muda nesse
print(a1.vc)
print(a2.vc)  # Só muda nesse
print(a3.vc)
A.vc = 432  # muda menos o a2 que foi alterado

print(a1.vc)
print(a2.vc)
print(a3.vc)
print(a4.vc)
