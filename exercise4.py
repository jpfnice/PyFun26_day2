"""
Exercise 4:
    
Step1: Create a french/english dict with the help of the file fr_en.txt or  directly in this script

Step2: Prompt the user for a french word

Step3: Check if the word exists or not, if it exists print its translation in English.
If it does not exist you could print a sorted list of all the french words your script could translate

Note: you should be able to enter the french word using any case
"""

# The dict is created here:
    
file=open("fr_en.txt")
fr_en_dict=dict()
for line in file:
    fr,en=line.split(":")
    fr_en_dict[fr]=en.strip()
file.close()

# fr_en_dict={"Ciel":"Sky",
#             "Terre":"Earth", 
#             "Ville":"City", 
#             "Voiture":"Car", 
#             "Rouge":"Red", 
#             "Mer":"Sea"}

# To print the dict:
print(fr_en_dict)

# To print it again in a more readable way:
for k,v in fr_en_dict.items():
    print(k,"->",v)
    
fr=input("Enter a french word, I'll give you it's translation in English: ")

# This is to "normalize" the input: the french word is
# always capitalized:
fr=fr.strip().capitalize()

if fr in fr_en_dict: # Is the word present ?
    print(f"The translation of {fr} is {fr_en_dict[fr]}")
    # or
    # print("The translation of",fr,"is",fr_en_dict[fr])
else:
    print(f"No translation for {fr} but I can translate:")
    print(sorted(fr_en_dict.keys()))
