
def multiplica(n):
    return lambda a : a * n

a=multiplica(2)
b=multiplica(3)
c=multiplica(4)

print(a(5))
print(b(5))
print(c(5))
