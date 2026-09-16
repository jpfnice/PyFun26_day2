

data=[5,6,7,8]

for e in enumerate(data):
    print(f"At position {e[0]} there is the element {e[1]}")

afile=open("data.txt")

# for e in enumerate(afile):
#     print(f"line {e[0]} is {e[1]}")
    
for index,value in enumerate(afile):
    print(f"line {index} is {value}")
    
