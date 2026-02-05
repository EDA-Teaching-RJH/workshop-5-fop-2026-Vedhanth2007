import re
captial = []
word = []

def camel_to_snake():
    name = input("Enter name here: ")
    for i in name:
        if i.isupper():
            captial.append(i)
            new = "_" + i
            new = new.lower()
            word.append(new)
        else:
           word.append(i)
    p = "".join(word)
        
            

    print(p)

camel_to_snake()

