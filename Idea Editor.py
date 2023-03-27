from datetime import datetime
loop = 1
loop2 = 1
def Input(Extra):
    promt = "IPCP:/"
    if Extra != "": promt = "IPCP:", Extra
    promt = str(promt)
    promt = promt.replace('(','').replace(')','').replace("'",'').replace(',','').replace(' ','')
    return input(promt)

while loop2 == 1:
    I1 = Input("")

    if I1 == 'new' or I1 == 'n' or I1 == 'NEW' or I1 == 'N' or I1 == 'New':
        I2 = Input("/name/")
        Name = I2 + ".txt"
        f = open('list.txt','a')
        f.write(I2)
        f.close()
        f = open(Name,'w')
        print(Name, "opened")
        while loop == 1:
            I3 = Input(":</p>")
            if I3 == 'exit': loop = 0
            if I3 != 'exit': 
                f.write(I3)
                f.write("\n")
        f.close()

    if I1 == 'list' or I1 == 'l' or I1 == 'LIST' or I1 == 'L' or I1 == 'List':
        f = open('list.txt','r')
        list = f.read()
        print(list)
        f.close()

    if I1 == 'edit' or I1 == 'e' or I1 == 'EDIT' or I1 == 'E' or I1 == 'Edit':
        f = open('list.txt','r')
        list = f.read()
        print(list)
        f.close()
        I2 = Input("/edit/")
        Name = I2 + ".txt"
        f = open(Name,'r')
        reading = f.read()
        print(reading)
        f.close
        f = open(Name,'a')
        print(Name, "opened")
        while loop == 1:
            I3 = Input(":</p>")
            if I3 == 'exit': loop = 0
            if I3 != 'exit': 
                f.write(I3)
                f.write("\n")
        f.close()

    if I1 == 'read' or I1 == 'r' or I1 == 'READ' or I1 == 'R' or I1 == 'Read':
        f = open('list.txt','r')
        list = f.read()
        print(list)
        f.close()
        I2 = Input("/read/")
        Name = I2 + ".txt"
        f = open(Name,'r')
        reading = f.read()
        print(reading)
        f.close



    if I1 == 'exit': loop2 = 0
