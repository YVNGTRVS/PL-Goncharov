# 1. В одномерном числовом массиве D длиной n вычислить сумму элементов с 
# нечетными индексами. Вывести на экран массив D, полученную сумму.

n=int(input("Введите длину массива:"))
D=[]
for i in range(n):
    print("Введите", i, "эллемент:")
    D.append(int(input()))
print("Сумма нечетных индексов:", sum(x for i,x in enumerate(D) if i % 2 == 1))


# 2. Дан одномерный массив из 8 элементов. Заменить все элементы массива 
# меньшие 15 их удвоенными значениями. Вывести на экран монитора 
# преобразованный массив.

n=8 
x=[]
print("\nДлина второго массива - 8 эллементов")
for i in range (n):
    print("\nВведите", i, "эллемент:")
    x.append(int(input()))
    if x[i]<15:
        x[i]=x[i]*2
print(x)
