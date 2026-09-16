

data=(45,10)
print(data[0], data[-1])

first,last=data # unpacking

print(first, last)

data=(45,10,78,89,78,89, 100)
first,*middle,last=data # unpacking

print(first)
print(middle)
print(last)

data=[56,78,89,100]

for var1 in enumerate(data):
    print(var1, var1[0], var1[1])

for ix,val in enumerate(data):
    print(ix,"=>", val)



    

    