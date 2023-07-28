#This is Python file

apel= 0
mangga= 0
durian= 0

a = "APEL"
m = "MANGGA"
d = "DURIAN"

while True:
    inp = input("pilih buah (apel/mangga/durian): ")
    if inp.upper() == a.upper():
        apel += 1
    elif inp.upper() == m.upper():
        mangga += 1
    elif inp.upper() == d.upper():
        durian += 1
    else:
        print("Wrong input")

    #print
    if apel > 1:
        print("apel", apel)
    if mangga > 1:
        print("mangga", mangga)
    if durian > 1:
        print("durian", durian)
 