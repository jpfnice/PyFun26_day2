
cities={} # An empty dict

myFile=open("cities.txt")

for line in myFile:
    city,temp=line.split(":") #unpacking is used
    temp=float(temp)
    if city in cities:
        cities[city].append(temp) 
    else:
        cities[city]=[temp]
    
print(cities)   

print("temperature of gimel:", cities["gimel"])
print("temperature of lausanne:", cities["lausanne"])

myFile.close()