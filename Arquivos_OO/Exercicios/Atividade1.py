i = float(input())

if i >= 0.1 and i <= 2.9:
    print('II')
elif i >= 3.0 and i <= 4.9:
    print("MI")
elif i >= 5.0 and i <= 6.9:
    print('MM')
elif i >= 7.0 and i <= 8.9:
    print('MS')
elif i >= 9 and i <= 10:
    print("SS")


#

i = 1
j = 0
while i > 0:
    i = int(input())
    if i > j:
        j = i

print(j)  


#   

i = 0
arranjo = [] * 10
while True:
    i = int(input())
    if i < 0:
        break
    arranjo.append(i)

arranjo.sort()


for i in arranjo:
    print(i)







