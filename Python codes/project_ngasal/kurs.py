while True:
    inp = input("kurs / conv ? ")
    

    if inp.upper() == "KURS":
        reg = input("idr / cad / jpy / myr? ")
        pri = int(input("masukkan nominal: "))
        if reg.upper() == "IDR":
            id_price = pri 
        elif reg.upper() == "CAD":
            cad_price = pri
        elif reg.upper() == "JPY":
            jpy_price = pri
        elif reg.upper() == "MYR":
            myr_price = pri
        else:
            print("wrong")

    elif inp.upper() == "CONV":
        reg = input("idr / cad / jpy / myr? ")
        pri = int(input("masukkan nominal: "))
        if reg.upper() == "IDR":
            print("USD", pri/id_price)
        elif reg.upper() == "CAD":
            print("USD", pri/cad_price)
        elif reg.upper() == "JPY":
            print("USD", pri/jpy_price)
        elif reg.upper() == "MYR":
            print("USD", pri/myr_price)
        else:
            print(inp.upper(), pri)
    else:
        print("wrong input")