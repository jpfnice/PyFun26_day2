
# Exercise 6 (function isPrime)
# Exercise 8 (function addList)
# Optional (a function to return a specific line from a file given it's position)

import os.path 

def getLine(fileName, lineNumber=0):
    """
    The function getLine returns the line "lineNumber" from the text file
    "fileName"
    
    Parameters
    ----------
    fileName : str
        the path of the text file to be used
    lineNumber : int, optional
        the line number to return. The default is 0.

    Returns
    -------
    str or None
        a line of the file or None (in case the file does not exists or 
                            there is no line at position lineNumber).

    """
    if not os.path.exists(fileName):
        print(f"{fileName} does not exists !")
        return None
    file=open(fileName)
    for ix,line in enumerate(file):
        if ix == lineNumber:
            return line.strip()
        
    file.close()


res=getLine("data.txt", 3)
print("line 3 of data.txt is", res)
res=getLine("data.txt", 10)
print("line 10 of data.txt is", res)
res=getLine("data.txt")
print("line 0 of data.txt is", res)
res=getLine("data.txt",100)
print("line 100 of data.txt is", res)
res=getLine("nonexisting.txt",100)
print("line 100 of nonexisting.txt is", res)