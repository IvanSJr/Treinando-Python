x = 4 in range(1,6) #true
y = 4 in range(0,6,2)#true
z = 5 in range(0,6,2)#false
a = (2 or 5) and (6 or 10) in range(1,11) #true
b = (2 or 5) and (6 or 11) in range(1,11,2) #false 11 não está contido  (1,3,5,7,9,11)
print(x)
print(y)
print(z)
print(a)
print(b)