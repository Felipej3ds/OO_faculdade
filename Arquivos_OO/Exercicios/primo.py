primo = int(input())
divisiveis = 0

for i in range(1, (primo + 1)):
    if primo % i == 0:
        divisiveis += 1

resposta = divisiveis == 2
print(resposta) 

#

def rem(l1, l2):
    for e in l1:
        if e in l2:
            l1.remove(e)

l1 = [1, 2, 3, 4]
l2 = [1, 2, 5, 6]

rem(l1, l2)

print(l1)


def rem(l1, l2):
    l1_copy = l1[:]
    for e in l1_copy:
        if e in l2:
            l1.remove(e)

l1 = [1, 2, 3, 4]
l2 = [1, 2, 5, 6]

rem(l1, l2) 

print(l1)





    
