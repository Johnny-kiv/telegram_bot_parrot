import wikipedia
a=input()
tx = a.lower()
if tx.find("что")>=0 and tx.find("такое")>=0 and len(tx)>10:
    tx = tx.replace("что","")
    tx = tx.replace("такое","")
    tx = tx.replace(" ","")
    print(tx)
    wikipedia.set_lang("ru")
    print(wikipedia.summary(tx))
