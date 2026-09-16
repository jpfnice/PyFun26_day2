d1={
    "maria":27845676, 
    "peter":27867899
}

d1["paul"]=27977666

# for e in d1:
#     print(e, "->", d1[e])

# for e in d1.items():
#     #print(e)
#     print(e[0],"->", e[1])
    
for k,v in d1.items(): # unpacking
    print(k,"->", v)

for v in d1.values():
    print(v)


for k in d1.keys():
    print(k)
    
d1.pop("paul")

print()

for k in d1.keys():
    print(k)
    
# if "peter" in d1:
#     d1.pop("peter")

# print(d1)