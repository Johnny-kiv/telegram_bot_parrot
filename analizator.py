from aiogram.types import Message
#####################################
# Исправление Москва и Россия
def jhn_moscow(t):
    r=""
    if t.lower()=="москва" or t.lower()=="moscow" or t.lower()=="москва" or t.lower()=="moscow":
        r = jhn_ispr(t)
    else:
        r=t
    return r

#####################################
# делает слово с большой буквы
def jhn_ispr(tx):
    mas = list(tx.lower())
    mas[0] = mas[0].upper()
    return "".join(mas)

#####################################
# Анализирует и отвечате на Привет и на как дела
def jhn_analizator(tx):
    lx = tx.lower()
    r=""
    etoumno = False

    if lx.find("привет")>=0 or lx.find("салют")>=0 or lx.find("здорово")>=0 or lx.find("здарова")>=0 or lx.find("здарово")>=0 or lx.find("здаров")>=0 or lx.find("здравствуйте")>=0:
        r="Салют! "
        etoumno = True

    if lx.find("как дела")>=0 or lx.find("как делы")>=0 or lx.find("как че")>=0:
        r=r+"У меня все отлично! А как тебя? "
        etoumno = True

    if lx.find("как")>=0 and (lx.find("зовут")>=0 or lx.find("звать")>=0 or lx.find("имя")>=0):
        r=r+"Меня зовут Кеша! "
        etoumno = True
    if lx.find("что")>=0 or lx.find("Cто")>=0 or lx.find("Што")>=0 and lx.find("умеешь")>=0 or lx.find("умееш")>=0:
        r=r+"Я могу общаться с тобой, передразнивать тебя, могу выполнять твои комады"
        etoumno = True


    if etoumno == False:
        r = jhn_bolsheneznau()
    return r

#####################################
# Отвечает что больше ничего не знает
def jhn_bolsheneznau():
    return "Прости больше ничего сказать умного не могу. Я сильно засекречен. 🥺"
def jhn_peredraz(mes: Message):
    print(mes)
    new_text = ""
    l = "?!.,@#$%^&*()\"\'№;:<>+={}]["
    b = "АБВГДЕЁЖЗИЙКЛМНОПРСТУХФЦЧШЩЬЫЪЭЮЯABCDEFGHIJKLMNOPQRSTUVWXZY"
    var = ""
    global text
    for leter in mes.text:
        if leter not in l:
            new_text += leter
        elif leter in l:
            var = leter
    text = "Сам, " + new_text.lower() + ", профессор" + var
