apel=0
mangga=0
durian=0

buah = {
    "APEL" : "APEL",
    "MANGGA" : "MANGGA",
    "DURIAN" : "DURIAN"
}

while True:
    inp = input("pilih buah (apel/mangga/durian): ")
    bh = inp.upper()
    
    a = buah.get(bh, "pilihan salah")

    if a == "APEL":
        apel += 1
    elif a == "MANGGA":
        mangga += 1
    elif a == "DURIAN":
        durian += 1

    if apel > 1:
        print("Apel", apel)
    if mangga > 1:
        print("Mangga", mangga)
    if durian > 1:
        print("Durian", durian)