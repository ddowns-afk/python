import random
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#for item in set(a):
#    if item in set(b):
#        print(item)

a = []
b = []
max_size = random.randint(5,100)
max_size2 = random.randint(5,100)

for i in range(max_size):
    a.append(random.randint(1,100))

for i in range(max_size2):
    b.append(random.randint(1,100))

for item in set(a):
    if item in set(b):
        print(item)