n = int(input('Введите размер списка:'))
A = list(range(1, n+1))
print(A)
j = 0
x = int(input('Введите число, количество вхождений которого в список вы хотите узнать:'))
for i in range(n):
    if A[i] == x:
        j = j+1
print(j, ' раз')