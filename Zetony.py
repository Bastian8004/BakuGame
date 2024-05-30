from Postac import PostacP, PostacG
import time, os, json

postacG = PostacG()
postacP = PostacP()

file_path = "game_data.json"

def save_data(data, filename="game_data.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def load_data(filename="game_data.json"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return None

data = load_data(file_path)

# Żetony Mocy

def ZetonSpiraliGracza(postacG, postacP, MocP, MocG):
    data["Spirala"]["Ilość"] -= 1
    if postacG["Persona"] in ["Persona Płomieni", "Persona Mroku", "Person Lasu"] and postacP["Persona"] in ["Persona Światła", "Persona Oceanu", "Persona Gór"]:
        MocG += 200
        print("Żeton Spirali aktywacja - Boost mocy Gracza - 200 punktów!")
    else:
        MocG += 100
        print("Żeton Spirali aktywacja - Boost mocy Gracza - 100 punktów!")
    return MocG, MocP

def ZetonSkrodoGracza(postacG, postacP, MocP, MocG):
    data["Skrodo"]["Ilosc"] -= 1
    if postacG["Persona"] in ["Persona Światła", "Persona Oceanu", "Persona Gór"] and postacP["Persona"] in ["Persona Płomieni", "Persona Mroku", "Person Lasu"]:
        MocG += 200
        print("Żeton Skrodo aktywacja - Boost mocy Gracza - 200 punktów!")
    else:
        MocG += 100
        print("Żeton Skrodo aktywacja - Boost mocy Gracza - 100 punktów!")
    return MocG, MocP

def ZetonPogromerGracza(postacG, postacP, MocP, MocG):
    data["Pogromer"]["Ilosc"] -= 1
    MocG += 200
    print("Żeton Pogromer aktywacja - Boost mocy Gracza - 200 punktów!")
    return MocG, MocP

def ZetonSyntezaGracza(postacG, postacP, MocP, MocG):
    data["Synteza"]["Ilosc"] -= 1
    synteza = MocP / 2
    MocG += synteza
    MocP -= synteza
    print("Żeton Syntezy aktywacja - Punkty mocy wyrównane!")
    return MocG, MocP

def ZetonDzeusGracza(postacG, postacP, MocP, MocG):
    data["Dzeus"]["Ilosc"] -= 1
    if postacG["Persona"] in ["Persona Mroku", "Persona Światła"]:
        MocG += 300
        print("Żeton Dzeusa aktywacja - Boost mocy Gracza - 300 punktów!")
    else:
        MocG += 150
        print("Żeton Dzeusa aktywacja - Boost mocy Gracza - 150 punktów!")
    return MocG, MocP

def ZetonWulkaniumGracza(postacG, postacP, MocP, MocG):
    data["Wulkanium"]["Ilosc"] -= 1
    if postacG["Persona"] in ["Persona Płomieni", "Persona Oceanu"]:
        MocG += 300
        print("Żeton Wulkanium aktywacja - Boost mocy Gracza - 300 punktów!")
    else:
        MocG += 150
        print("Żeton Wulkanium aktywacja - Boost mocy Gracza - 150 punktów!")
    return MocG, MocP

def ZetonIstotyGracza(postacG, postacP, MocP, MocG):
    data["Istoty"]["Ilosc"] -= 1
    if postacG["Persona"] in ["Persona Lasu", "Persona Gór"]:
        MocG += 300
        print("Żeton Istoty aktywacja - Boost mocy Gracza - 300 punktów!")
    else:
        MocG += 150
        print("Żeton Istoty aktywacja - Boost mocy Gracza - 150 punktów!")
    return MocG, MocP

# Żetony obrony

def ZetonMetaGolemaGracza(postacG, postacP, MocP, MocG):
    data["MetaGolem"]["Ilosc"] -= 1
    if postacG["Persona"] in ["Persona Lasu", "Persona Gór"]:
        MocP -= 200
        print("Żeton MetaGolema aktywacja - Odjęto przeciwnikowi 200 punktów!")
    else:
        MocP -= 100
        print("Żeton MetaGolema aktywacja - Odjęto przeciwnikowi 100 punktów!")
    return MocG, MocP

def ZetonTarczownikGracza(postacG, postacP, MocP, MocG):
    data["Tarczownik"]["Ilosc"] -= 1
    if postacG["Persona"] in ["Persona Mroku", "Persona Oceanu"]:
        MocP -= 200
        print("Żeton Tarczownik aktywacja - Odjęto przeciwnikowi 200 punktów!")
    else:
        MocP -= 100
        print("Żeton Tarczownik aktywacja - Odjęto przeciwnikowi 100 punktów!")
    return MocG, MocP

def ZetonHonoruGracza(postacG, postacP, MocP, MocG):
    data["Honor"]["Ilosc"] -= 1
    if postacG["Persona"] in ["Persona Płomieni", "Persona Światła"]:
        MocP -= 200
        print("Żeton Honoru aktywacja - Odjęto przeciwnikowi 200 punktów!")
    else:
        MocP -= 100
        print("Żeton Honoru aktywacja - Odjęto przeciwnikowi 100 punktów!")
    return MocG, MocP

# Żetony rozkazu

def ZetonDominiumGracza(postacG, postacP, MocP, MocG):
    data["Dominium"]["Ilosc"] -= 1
    if postacG["Status"] in ["Helios", "Lassus"]:
        MocG += 300
        print("Żeton Rozkazu aktywacja - Dominium - Boost mocy Gracza - 300 punktów!")
    elif postacG["Status"] in ["Helios", "Lassus"] and postacP["Status"] in ["Posejdon", "Supterra"]:
        MocG += 300
        MocP -= 300
        print("Żeton Rozkazu aktywacja - Dominium - Wyrównano liczbę punktów!")
    else:
        MocG += 150
        print("Żeton Rozkazu aktywacja - Dominium - Boost mocy Gracza - 200 punktów!")
    return MocG, MocP

def ZetonPrzedwiecznyGracza(postacG, postacP, MocP, MocG):
    data["Przedwieczny"]["Ilosc"] -= 1
    if postacG["Status"] in ["Phoenix", "Hekate"]:
        MocG += 300
        print("Żeton Rozkazu aktywacja - Przedwieczny - Boost mocy Gracza - 300 punktów!")
    elif postacG["Status"] in ["Phoenix", "Hekate"] and postacP["Status"] in ["Helios", "Lassus"]:
        MocG += 300
        synteza = MocP / 2
        MocG += synteza
        MocP -= synteza
        print("Żeton Rozkazu aktywacja - Przedwieczny - Wyrównano liczbę punktów!")
    else:
        MocG += 200
        print("Żeton Rozkazu aktywacja - Przedwieczny - Boost mocy Gracza - 200 punktów!")
    return MocG, MocP

def ZetonProznyGracza(postacG, postacP, MocP, MocG):
    data["Prozny"]["Ilosc"] -= 1
    if postacG["Status"] in ["Posejdon", "Supterra"] and postacP["Status"] in ["Phoenix", "Hekate"]:
        MocG += 250
        synteza = MocP / 1.5
        MocG += synteza
        print("Żeton Rozkazu aktywacja - Próżny - Wyrównano liczbę punktów!")
    elif postacG["Status"] in ["Posejdon", "Supterra"]:
        MocG += 300
        print("Żeton Rozkazu aktywacja - Próżny - Boost mocy Gracza - 300 punktów!")
    else:
        MocG += 250
        print("Żeton Rozkazu aktywacja - Próżny - Boost mocy Gracza - 250 punktów!")
    return MocG, MocP

def ZetonSpiraliPrzeciwnika(MocP, postacP, MocG, postacG):
    if postacP["Persona"] in ["Persona Płomieni", "Persona Mroku", "Person Lasu"] and postacG["Persona"] in ["Persona Światła", "Persona Oceanu", "Persona Gór"]:
        MocP += 200
        print("Żeton Spirali aktywacja - Boost mocy Przeciwnika - 200 punktów!")
    else:
        MocP += 100
        print("Żeton Spirali aktywacja - Boost mocy Przeciwnika - 100 punktów!")
    return MocG, MocP

def ZetonSkrodoPrzeciwnika(MocP, postacP, MocG, postacG):
    if postacP["Persona"] in ["Persona Światła", "Persona Oceanu", "Persona Gór"] and postacG["Persona"] in ["Persona Płomieni", "Persona Mroku", "Person Lasu"]:
        MocP += 200
        print("Żeton Skrodo aktywacja - Boost mocy Przeciwnika - 200 punktów!")
    else:
        MocP += 100
        print("Żeton Skrodo aktywacja - Boost mocy Przeciwnika - 100 punktów!")
    return MocG, MocP

def ZetonPogromerPrzeciwnika(MocP, postacP, MocG, postacG):
    MocP += 200
    print("Żeton Pogromer aktywacja - Boost mocy Przeciwnika - 200 punktów!")
    return MocG, MocP

def ZetonSyntezaPrzeciwnika(MocP, postacP, MocG, postacG):
    synteza = MocG / 2
    MocP += synteza
    MocG -= synteza
    print("Żeton Syntezy aktywacja - Punkty mocy wyrównane!")
    return MocG, MocP

def ZetonDzeusPrzeciwnika(MocP, postacP, MocG, postacG):
    if postacP["Persona"] in ["Persona Mroku", "Persona Światła"]:
        MocP += 300
        print("Żeton Dzeusa aktywacja - Boost mocy Przeciwnika - 300 punktów!")
    else:
        MocP += 150
        print("Żeton Dzeusa aktywacja - Boost mocy Przeciwnika - 150 punktów!")
    return MocG, MocP

def ZetonWulkaniumPrzeciwnika(MocP, postacP, MocG, postacG):
    if postacP["Persona"] in ["Persona Płomieni", "Persona Oceanu"]:
        MocP += 300
        print("Żeton Wulkanium aktywacja - Boost mocy Przeciwnika - 300 punktów!")
    else:
        MocP += 150
        print("Żeton Wulkanium aktywacja - Boost mocy Przeciwnika - 150 punktów!")
    return MocG, MocP

def ZetonIstotyPrzeciwnika(MocP, postacP, MocG, postacG):
    if postacP["Persona"] in ["Persona Lasu", "Persona Gór"]:
        MocP += 300
        print("Żeton Istoty aktywacja - Boost mocy Przeciwnika - 300 punktów!")
    else:
        MocP += 150
        print("Żeton Istoty aktywacja - Boost mocy Przeciwnika - 150 punktów!")
    return MocG, MocP

# Żetony obrony

def ZetonMetaGolemaPrzeciwnika(MocP, postacP, MocG, postacG):
    if postacP["Persona"] in ["Persona Lasu", "Persona Gór"]:
        MocG -= 200
        print("Żeton MetaGolema aktywacja - Odjęto Graczowi 200 punktów!")
    else:
        MocG -= 100
        print("Żeton MetaGolema aktywacja - Odjęto Graczowi 100 punktów!")
    return MocG, MocP

def ZetonTarczownikPrzeciwnika(MocP, postacP, MocG, postacG):
    if postacP["Persona"] in ["Persona Mroku", "Persona Oceanu"]:
        MocG -= 200
        print("Żeton Tarczownik aktywacja - Odjęto Graczowi 200 punktów!")
    else:
        MocG -= 100
        print("Żeton Tarczownik aktywacja - Odjęto Graczowi 100 punktów!")
    return MocG, MocP

def ZetonHonoruPrzeciwnika(MocP, postacP, MocG, postacG):
    if postacP["Persona"] in ["Persona Płomieni", "Persona Światła"]:
        MocG -= 200
        print("Żeton Honoru aktywacja - Odjęto Graczowi 200 punktów!")
    else:
        MocG -= 100
        print("Żeton Honoru aktywacja - Odjęto Graczowi 100 punktów!")
    return MocG, MocP

# Żetony rozkazu

def ZetonDominiumPrzeciwnika(MocP, postacP, MocG, postacG):
    if postacP["Status"] in ["Helios", "Lassus"]:
        MocP += 300
        print("Żeton Rozkazu aktywacja - Dominium - Boost mocy Przeciwnika - 300 punktów!")
    elif postacP["Status"] in ["Helios", "Lassus"] and postacG["Status"] in ["Posejdon", "Supterra"]:
        MocP += 300
        MocG -= 300
        print("Żeton Rozkazu aktywacja - Dominium - Wyrównano liczbę punktów!")
    else:
        MocP += 150
        print("Żeton Rozkazu aktywacja - Dominium - Boost mocy Przeciwnika - 200 punktów!")
    return MocG, MocP

def ZetonPrzedwiecznyPrzeciwnika(MocP, postacP, MocG, postacG):
    if postacP["Status"] in ["Phoenix", "Hekate"]:
        MocP += 300
        print("Żeton Rozkazu aktywacja - Przedwieczny - Boost mocy Przeciwnika - 300 punktów!")
    elif postacP["Status"] in ["Phoenix", "Hekate"] and postacG["Status"] in ["Helios", "Lassus"]:
        MocP += 300
        synteza = MocG / 2
        MocP += synteza
        MocG -= synteza
        print("Żeton Rozkazu aktywacja - Przedwieczny - Wyrównano liczbę punktów!")
    else:
        MocP += 200
        print("Żeton Rozkazu aktywacja - Przedwieczny - Boost mocy Przeciwnika - 200 punktów!")
    return MocG, MocP

def ZetonProznyPrzeciwnika(MocP, postacP, MocG, postacG):
    if postacP["Status"] in ["Posejdon", "Supterra"]:
        MocP += 300
        print("Żeton Rozkazu aktywacja - Próżny - Boost mocy Przeciwnika - 300 punktów!")
    elif postacP["Status"] in ["Posejdon", "Supterra"] and postacG["Status"] in ["Phoenix", "Hekate"]:
        MocP += 250
        synteza = MocG / 1.5
        MocP += synteza
        print("Żeton Rozkazu aktywacja - Próżny - Wyrównano liczbę punktów!")
    else:
        MocP += 250
        print("Żeton Rozkazu aktywacja - Próżny - Boost mocy Przeciwnika - 250 punktów!")
    return MocG, MocP


Mocy = {
        "Nazwa": "Żetony Mocy",
        "Opis": "Żetony Mocy - używając ich dodajesz punkty swojej postaci. \nTwoje \"Żetony Mocy\" to: ",
        "Spirali": data["Spirala"],
        "Pogromer": data["Pogromer"],
        "Skrodo": data["Skrodo"],
        "Synteza": data["Synteza"],
        "Dzeus": data["Dzeus"],
        "Wulkanium": data["Wulkanium"],
        "Istoty": data["Istoty"]
    }

Obrony = {
        "Nazwa": "Żetony Obrony",
        "Opis": "Żetony Obrony - używając ich odejmujesz punkty postaci twojego przeciwnika.\n Twoje \"Żetony Obrony\" to: ",
        "MetaGolem": data["MetaGolem"],
        "Tarczownik": data["Tarczownik"],
        "Honoru": data["Honor"]
    }

Rozkazu = {
        "Nazwa": "Żetony Rozkazu",
        "Opis": "Żetony Rozkazu - używając ich dodajesz sobie, a zarazem odejmujesz punkty postaci twojego przeciwnika. \nTwoje \"Żetony Rozkazu\" to: ",
        "Dominium": data["Dominium"],
        "Przedwieczny": data["Przedwieczny"],
        "Próżny": data["Prozny"]
    }

def listaMoce():
    for v in Mocy.items():
        print(v)

def listaObrony():
    for v in Obrony.items():
        print(v)

def listaRozkazu():
    for v in Rozkazu.items():
        print(v)

def wyborG(MocG, postacG, MocP, postacP):
    zetony = 0
    rozkazu = 1
    while zetony < 3:
        print('''
    1 - Zetony Mocy
    2 - Zetony Obronne
    3 - Zetony Rozkazu
    ''')
        y = str(input("Jakiego typu żetonu chcesz użyć?"))
        if y == "1":
            time.sleep(1)
            listaMoce()
            time.sleep(1)
            print('''
                1 - Żeton Spirali
                2 - Żeton Pogromer
                3 - Żeton Skrodo
                4 - Żeton Syntezy
                5 - Żeton Dzeus
                6 - Żeton Wulkanium
                7 - Żeton Istoty
                0 - Powrót do wyboru typu żetonu
                ''')
            x = str(input("Jaki jest twój wybór? (0 - 7): "))
            if x == "1":
                if data["Spirala"]["Ilosc"] == 0:
                    print("Brak żetonów Spirali w plecaku. Użyj innego!")
                    return x
                else:
                    zetony += 1
                    time.sleep(1)
                    MocG, MocP = ZetonSpiraliGracza(postacG, postacP, MocP, MocG)
                    return MocG, MocP
            elif x == "2":
                if data["Pogromer"]["Ilosc"] == 0:
                    print("Brak żetonów Pogromera w plecaku. Użyj innego!")
                    return x
                else:
                    zetony += 1
                    time.sleep(1)
                    MocG, MocP = ZetonPogromerGracza(postacG, postacP, MocP, MocG)
                    return MocG, MocP
            elif x == "3":
                if data["Skrodo"]["Ilosc"] == 0:
                    print("Brak żetonów Skrodo w plecaku. Użyj innego!")
                    return x
                else:
                    zetony += 1
                    time.sleep(1)
                    MocG, MocP = ZetonSkrodoGracza(postacG, postacP, MocP, MocG)
                    return MocG, MocP
            elif x == "4":
                if data["Synteza"]["Ilosc"] == 0:
                    print("Brak żetonów Syntezy w plecaku. Użyj innego!")
                    return x
                else:
                    zetony += 1
                    time.sleep(1)
                    MocG, MocP = ZetonSyntezaGracza(postacG, postacP, MocP, MocG)
                    return MocG, MocP
            elif x == "5":
                if data["Dzeus"]["Ilosc"] == 0:
                    print("Brak żetonów Dzeusa w plecaku. Użyj innego!")
                    return x
                else:
                    zetony += 1
                    time.sleep(1)
                    MocG, MocP = ZetonDzeusGracza(postacG, postacP, MocP, MocG)
                    return MocG, MocP
            elif x == "6":
                if data["Wulkanium"]["Ilosc"] == 0:
                    print("Brak żetonów Wulkanium w plecaku. Użyj innego!")
                    return x
                else:
                    zetony += 1
                    time.sleep(1)
                    MocG, MocP = ZetonWulkaniumGracza(postacG, postacP, MocP, MocG)
                    return MocG, MocP
            elif x == "7":
                if data["Istoty"]["Ilosc"] == 0:
                    print("Brak żetonów Istoty w plecaku. Użyj innego!")
                    return x
                else:
                    zetony += 1
                    time.sleep(1)
                    MocG, MocP = ZetonIstotyGracza(postacG, postacP, MocP, MocG)
                    return MocG, MocP
            else:
                time.sleep(1)
                print("Powrót do rodzajów żetonów")
                time.sleep(2)
                return y

        elif y == "2":
            time.sleep(1)
            listaObrony()
            time.sleep(1)
            print('''
                1 - Żeton MetaGolema
                2 - Żeton Tarczownika
                3 - Żeton Honoru
                0 - Powrót do wyboru typu żetonu (Jeśli decydujesz się wrócić musisz wybrac zetony od nowa)
                ''')
            x = str(input("Jaki jest twój wybór? (0 - 3): "))
            if x == "1":
                if data["MetaGolem"]["Ilosc"] == 0:
                    print("Brak żetonów MetaGolema w plecaku. Użyj innego!")
                    return x
                else:
                    zetony += 1
                    time.sleep(1)
                    MocG, MocP = ZetonMetaGolemaGracza(postacG, postacP, MocP, MocG)
                    return MocG, MocP
            elif x == "2":
                if data["Tarczownik"]["Ilosc"] == 0:
                    print("Brak żetonów Tarczownika w plecaku. Użyj innego!")
                    return x
                else:
                    zetony += 1
                    time.sleep(1)
                    MocG, MocP = ZetonTarczownikGracza(postacG, postacP, MocP, MocG)
                    return MocG, MocP
            elif x == "3":
                if data["Honor"]["Ilosc"] == 0:
                    print("Brak żetonów Honoru w plecaku. Użyj innego!")
                    return x
                else:
                    zetony += 1
                    time.sleep(1)
                    MocG, MocP = ZetonHonoruGracza(postacG, postacP, MocP, MocG)
                    return MocG, MocP
            else:
                time.sleep(1)
                print("Powrót do rodzajów żetonów")
                time.sleep(2)
                return y

        elif y == "3":
            time.sleep(1)
            listaRozkazu()
            time.sleep(1)
            print('''
                1 - Żeton Dominium
                2 - Żeton Przedwieczny
                3 - Żeton Próżny
                0 - Powrót do wyboru typu żetonu (Jeśli decydujesz się wrócić musisz wybrac zetony od nowa)
                ''')
            x = str(input("Jaki jest twój wybór? (0 - 3): "))
            if x == "1":
                if rozkazu == 0:
                    print('''Wykorzystałeś już żeton rozkazu w tej rundzie
                    Użyj innego typu żetonu
                    Powrót do typów żetonów''')
                    time.sleep(3)
                    return y
                elif data["Dominium"]["Ilosc"] == 0:
                    print("Brak żetonów Dominium w plecaku. Użyj innego!")
                    return x
                else:
                    rozkazu -= 1
                    zetony += 1
                    time.sleep(1)
                    MocG, MocP = ZetonDominiumGracza(postacG, postacP, MocP, MocG)
                    return MocG, MocP
            elif x == "2":
                if rozkazu == 0:
                    print('''Wykorzystałeś już żeton rozkazu w tej rundzie
                    Użyj innego typu żetonu
                    Powrót do typów żetonów''')
                    time.sleep(3)
                    return y
                elif data["Przedwieczny"]["Ilosc"] == 0:
                    print("Brak żetonów Przedwieczny w plecaku. Użyj innego!")
                    return x
                else:
                    rozkazu -= 1
                    zetony += 1
                    time.sleep(1)
                    MocG, MocP = ZetonPrzedwiecznyGracza(postacG, postacP, MocP, MocG)
                    return MocG, MocP
            elif x == "3":
                if rozkazu == 0:
                    print('''Wykorzystałeś już żeton rozkazu w tej rundzie
                    Użyj innego typu żetonu
                    Powrót do typów żetonów''')
                    time.sleep(3)
                    return y
                elif data["Prozny"]["Ilosc"] == 0:
                    print("Brak żetonów Prozny w plecaku. Użyj innego!")
                    return x
                else:
                    rozkazu -= 1
                    zetony += 1
                    time.sleep(1)
                    MocG, MocP = ZetonProznyGracza(postacG, postacP, MocP, MocG)
                    return MocG, MocP
            else:
                time.sleep(1)
                print("Powrót do rodzajów żetonów")
                time.sleep(2)
                return y

        else:
            print("Podano zły numer!")
            print("Spróbuj ponownie!")
            time.sleep(3)
            return y
#MocP, postacP, MocG, postacG

def wyborP(poziom, MocP, postacP, MocG, postacG):
    import random
    import time

    if poziom == "1":
        zetony = [random.randint(1, 7) for _ in range(2)] + [random.randint(8, 10)]
    elif poziom == "2":
        zetony = [random.randint(1, 7)] + [random.randint(8, 10) for _ in range(2)]
    elif poziom == "3":
        zetony = [random.randint(1, 7)] + [random.randint(8, 10)] + [random.randint(11, 13)]

    for zet in zetony:
        time.sleep(1)
        if zet == 1:
            MocG, MocP = ZetonSpiraliPrzeciwnika(MocP, postacP, MocG, postacG)
        elif zet == 2:
            MocG, MocP = ZetonPogromerPrzeciwnika(MocP, postacP, MocG, postacG)
        elif zet == 3:
            MocG, MocP = ZetonSkrodoPrzeciwnika(MocP, postacP, MocG, postacG)
        elif zet == 4:
            MocG, MocP = ZetonSyntezaPrzeciwnika(MocP, postacP, MocG, postacG)
        elif zet == 5:
            MocG, MocP = ZetonDzeusPrzeciwnika(MocP, postacP, MocG, postacG)
        elif zet == 6:
            MocG, MocP = ZetonWulkaniumPrzeciwnika(MocP, postacP, MocG, postacG)
        elif zet == 7:
            MocG, MocP = ZetonIstotyPrzeciwnika(MocP, postacP, MocG, postacG)
        elif zet == 8:
            MocG, MocP = ZetonMetaGolemaPrzeciwnika(MocP, postacP, MocG, postacG)
        elif zet == 9:
            MocG, MocP = ZetonTarczownikPrzeciwnika(MocP, postacP, MocG, postacG)
        elif zet == 10:
            MocG, MocP = ZetonHonoruPrzeciwnika(MocP, postacP, MocG, postacG)
        elif zet == 11:
            MocG, MocP = ZetonDominiumPrzeciwnika(MocP, postacP, MocG, postacG)
        elif zet == 12:
            MocG, MocP = ZetonPrzedwiecznyPrzeciwnika(MocP, postacP, MocG, postacG)
        elif zet == 13:
            MocG, MocP = ZetonProznyPrzeciwnika(MocP, postacP, MocG, postacG)

    return MocG, MocP
