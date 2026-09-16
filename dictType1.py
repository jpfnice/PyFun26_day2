"""
dict: a mutable collection

    len(), for, in, not in, ... are available because a dict is a "collection"
"""

# # To create an empty dict:
# d1=dict() # dict() is a built-in function a "constructor" of dict
# #or
# d1={}

# print(d1, type(d1), len(d1))

# # To create a dict with a few elements in it:
# d1={
#     "maria":27845676, 
#     "peter":27867899
# }

# print(d1, type(d1), len(d1))

# for name in d1:
#     print(name, d1[name])
    
# if "mario" in d1:
#     print(d1["mario"])

# print(d1["maria"])
# print(d1.get("maria"))

# d1["paul"]=27977666 # I add a new pair to d1
# print(d1, type(d1), len(d1))

# d1["maria"]=27977665 # I update the value associated with the key Maria

# print(d1["maria"])

# print(d1, type(d1), len(d1))

# print(d1.keys())
# print(d1.values())

# if "maria" in d1:
#     d1.pop("maria")
    
# print(d1, type(d1), len(d1))

d1={
          10:["raphael", "gabriel", "thomas"], 
          11:["julia", "yann"],
          12:[],
          13:["mario", "robert"]
}


# d1={
#     'jean':{'city':'Geneva', 'street':'Grand Pré', 'phone':789999}
    
#     }


# print(d1["jean"]["phone"])

print(d1, type(d1), len(d1))

print(d1[10])

# print(d1.get(10))

d1[9]=["maria"]
print(d1)

print(d1, type(d1), len(d1))

for k in d1:
    print(k,"->",d1[k])
    
d1[9].append("julia")

for k in d1:
    print(k,"->",d1[k])


