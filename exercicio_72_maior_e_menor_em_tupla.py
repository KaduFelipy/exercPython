from random import randint
tupla = []
for i in range (0,5):
    a = randint(0,100)
    tupla.append(a)
new_tuple = tuple(tupla)
print(new_tuple)
print(type(new_tuple))
print(max(tupla))
print(min(tupla))
