
def multiplica(n):
    return lambda a : a * n

a=multiplica(2)
b=multiplica(3)
c=multiplica(4)

print(a(5))
print(b(5))
print(c(5))

lista = [1,2,4,6,7,6,4,3,5,7,8,89,3,7,6,5,65]
menores=[]
mayores=[]
for x in lista:
    menores.append(x) if x<10 else mayores.append(x)

print(mayores)
print(menores)
