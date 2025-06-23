#mezclarArreglos

A1 = [9, 12, 2018, 1, 8]

A2 = [2, 5, 91, 32, 75]

A3 = []

i = 0

for i in range(5): 
    if i%2 == 0:
        A3.append(A1[i])
    elif i % 2 ==1:
        A3.append(A2[i])

print(A3)