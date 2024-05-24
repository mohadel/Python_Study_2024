dic = {
    "key1" : 1,
    "key2" : 2,
    "key3" : 3
}

for x in dic:
    print(x)

for val in dic.values():
    print(val)

for key,val in dic.items():
    print(key,val)

def foo():
    return (1,2)

x,y = foo()

z = foo()

print(x,y)

print(z)

def zoo():
    return 1,2

m = zoo()
print(m[0])
print(type(m))


    