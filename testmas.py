
fo = open("input.txt","r", encoding="utf-8")

tx = fo.read()

tx = tx.replace("[", "{")
tx = tx.replace("]", "}")
rez = []
if len(tx) < 4096:
    rez.append(tx)
else:
    mas = list(tx)
    ost = tx


    kol = int(len(tx) // 4096) + 2

    for k in range(kol):
        if len(mas) > 0:
            pos = ost.rfind(".", 0, 4095)
            print(pos)
            if pos != -1:
                ms = mas[0:pos+1]
            else:
                ms = mas
            #print("".join(ms))
            rez.append("".join(ms))

            #print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            #print(pos)
            #print("\n")

            #print(len(mas))
            #print(mas)

            if pos != -1:
                for i in range(pos + 1):
                    #mas.pop(0)
                    del mas[0]
            else:
                for i in range(len(mas)):
                    #mas.pop(0)
                    del mas[0]
            ost = "".join(mas)

print(rez)
