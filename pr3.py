v=int(input("Введите число v "))
k=int(input("Введите число k "))
if v<k:
    Z=v-k+1
elif k<v:
    Z=k*k-v*v
else:
    Z=k*k-k
print (Z)