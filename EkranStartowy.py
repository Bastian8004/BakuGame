from functools import wraps
import json
import os
import random



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


global poziom
def wybierz():

    print("Twoje statystyki:")
    print("Wygrane {}".format(data["Gracz"]["Wygrane"]))
    print("Przegrane {}".format(data["Gracz"]["Przegrane"]))
    print("Najwieksza Moc {}".format(data["Gracz"]["NajwiekszaMoc"]))
    print("Najmniejsza Moc {}".format(data["Gracz"]["NajmniejszaMoc"]))
    print('''Zasady:
    1 - W każdej rundzie możesz użyć 3 żetonów
    2 - W każdej rundzie możesz użyć tylko 1 żetonu rozkazu
    3 - zwracaj uwagę na status przeciwnika w wyborach zetonów - protip
    4 - Bitwe wygrywa ten kto zdobędzie 2 punkty
    5 - Baw się dobrze!''')
    print('''Wybierz poziom trudności:
        1 - Łatwy
        2 - Średni
        3 - Trudny
        4 - Powrót do menu
        ''')

    poziom = str(input("Jaki jest twój wybór?"))
    if poziom == "1" or poziom == "2" or poziom == "3":
        print("Wybrałeś poziom trudność")
        print("Naszykuj się do walki")
        time.sleep(3)
        bitwa(poziom)
    elif poziom == "4":
        print("Wracasz do menu")
        time.sleep(3)
        Menu()
    else:
        print("Podano zły numer!")
        print("Spróbuj ponownie!")
        time.sleep(3)
        wybierz()



import time
import builtins
def delay_after_print_decorator(func):
    def wrapper(*args, **kwargs):
        original_print = builtins.print

        def delayed_print(*args, **kwargs):
            original_print(*args, **kwargs)
            time.sleep(1)

        builtins.print = delayed_print
        try:
            result = func(*args, **kwargs)
        finally:
            builtins.print = original_print
        return result

    return wrapper



@delay_after_print_decorator
def bitwa(poziom):
    import random
    import time
    from Postac import PostacP, PostacG

    PunktyGracza = 0
    PunktyPrzeciwnika = 0
    round = 0
    postacG = PostacG()
    postacP = PostacP()

    print(f'''Oto twoja postać:
        Nazwa: {postacG["Nazwa Postaci Gracza"]},
        Persona: {postacG["Persona"]},
        Moc: {postacG["Moc"]},
        Status: {postacG["Status"]}''')
    time.sleep(2)
    print(f'''Oto postac przeciwnika:
        Nazwa: {postacP["Nazwa Postaci Przeciwnika"]},
        Persona: {postacP["Persona"]},
        Moc: {postacP["Moc"]},
        Status: {postacP["Status"]}''')
    time.sleep(2)

    bitwa_main(poziom, postacG, postacP, PunktyGracza, PunktyPrzeciwnika, round)

def bitwa_main(poziom, postacG, postacP, PunktyGracza, PunktyPrzeciwnika, round):
    from Status import StatusPostacG, StatusPostacP
    from Kontry import kontryGracza, kontryPrzeciwnika
    import Zetony
    while round < 3:
        MocG = postacG["Moc"]
        MocP = postacP["Moc"]

        x = random.randint(1, 2)
        if PunktyPrzeciwnika == 2 or PunktyGracza == 2:
            break

        if (PunktyPrzeciwnika == 0 and PunktyGracza == 0 and x == 1) or (x == 1):
            print("Rozpoczynasz rundę!")
            time.sleep(2)
            round += 1

            MocG, MocP = StatusPostacG(MocG, postacG, MocP, postacP)
            print(f"Moc twojej postaci: {MocG}")
            print(f"Moc postaci przeciwnika: {MocP}")
            MocP, MocG = StatusPostacP(MocP, postacP, MocG, postacG)
            print(f"Moc postaci przeciwnika: {MocP}")
            print(f"Moc twojej postaci: {MocG}")
            MocG, MocP = kontryGracza(postacG, postacP, MocP, MocG)
            print(f"Moc twojej postaci: {MocG}")
            print(f"Moc postaci przeciwnika: {MocP}")
            MocG, MocP = kontryPrzeciwnika(postacG, postacP, MocP, MocG)
            print(f"Moc postaci przeciwnika: {MocP}")
            print(f"Moc twojej postaci: {MocG}")
            for _ in range(3):
                zeton = Zetony.wyborG(MocG, postacG, MocP, postacP)
                MocG, MocP = zeton
            print(f"Moc twojej postaci: {MocG}")
            print(f"Moc postaci przeciwnika: {MocP}")
            for _ in range(1):
                zeton = Zetony.wyborP(poziom, MocP, postacP, MocG, postacG)
                MocG, MocP = zeton
            print(f"Moc twojej postaci: {MocG}")
            print(f"Moc postaci przeciwnika: {MocP}")
            print("Podsumowanie mocy")
            print(f"Moc twojej postaci: {MocG}")
            print(f"Moc postaci przeciwnika: {MocP}")

        else:
            print("Runde rozpoczyna przeciwnik!")
            time.sleep(2)
            round += 1

            MocP, MocG = StatusPostacP(MocP, postacP, MocG, postacG)
            print(f"Moc postaci przeciwnika: {MocP}")
            print(f'Moc twojej postaci: {MocG}')
            MocG, MocP = StatusPostacG(MocG, postacG, MocP, postacP)
            print(f"Moc twojej postaci: {MocG}")
            print(f"Moc postaci przeciwnika: {MocP}")
            MocG, MocP = kontryPrzeciwnika(postacG, postacP, MocP, MocG)
            print(f"Moc postaci przeciwnika: {MocP}")
            print(f"Moc twojej postaci: {MocG}")
            MocG, MocP = kontryGracza(postacG, postacP, MocP, MocG)
            print(f"Moc twojej postaci: {MocG}")
            print(f"Moc postaci przeciwnika: {MocP}")
            for _ in range(1):
                zeton = Zetony.wyborP(poziom, MocP, postacP, MocG, postacG)
                MocG, MocP = zeton
            print(f"Moc postaci przeciwnika: {MocP}")
            print(f"Moc twojej postaci: {MocG}")
            for _ in range(3):
                zeton = Zetony.wyborG(MocG, postacG, MocP, postacP)
                MocG, MocP = zeton
            print(f"Moc twojej postaci: {MocG}")
            print(f"Moc postaci przeciwnika: {MocP}")
            print("Podsumowanie mocy")
            print(f"Moc twojej postaci: {MocG}")
            print(f"Moc postaci przeciwnika: {MocP}")
            if MocG > data["Gracz"]["NajwiekszaMoc"]:
                print("Osiągnięto największą nową moc: {}".format(MocG))
                data["Gracz"]["NajwiekszaMoc"] = MocG
                save_data(data, file_path)
        if MocG > data["Gracz"]["NajwiekszaMoc"]:
            print("Osiągnięto największą nową moc: {}".format(MocG))
            data["Gracz"]["NajwiekszaMoc"] = MocG
            save_data(data, file_path)
        elif MocG < data["Gracz"]["NajmniejszaMoc"]:
            print("Osiągnięto najmniejszą nową moc: {}".format(MocG))
            data["Gracz"]["NajmniejszaMoc"] = MocG
            save_data(data, file_path)

        if MocG > MocP:
            PunktyGracza += 1
            print("Wygrywasz rundę")
        else:
            PunktyPrzeciwnika += 1
            print("Przeciwnik wygrywa rundę")

        print(f"Wynik: Gracz {PunktyGracza} : {PunktyPrzeciwnika} Przeciwnik")

        if PunktyGracza == 2:
            print("Gratulacje! Wygrałeś bitwę!")
            data["Gracz"]["Wygrane"] += 1
            if poziom == "1":
                nagroda = 1000
                print("Wygrałeś {} bazylionów!".format(nagroda))
                data["Gracz"]["Portfel"] += nagroda
                print("Bazyliony dodane na konto. Powrót do menu!")
                save_data(data, file_path)
                Menu()
            elif poziom == "2":
                nagroda = 2500
                print("Wygrałeś {} bazylionów!".format(nagroda))
                data["Gracz"]["Portfel"] += nagroda
                print("Bazyliony dodane na konto. Powrót do menu!")
                save_data(data, file_path)
                Menu()
            elif poziom == "3":
                nagroda = 5000
                print("Wygrałeś {} bazylionów!".format(nagroda))
                data["Gracz"]["Portfel"] += nagroda
                print("Bazyliony dodane na konto. Powrót do menu!")
                save_data(data, file_path)
                Menu()

        elif PunktyPrzeciwnika == 2:
            print("Niestety! Przeciwnik wygrał bitwę!")
            data["Gracz"]["Przegrane"] += 1
            if poziom == "1":
                nagroda = 200
                print("Nagroda pocieszenia:  {} bazylionów!".format(nagroda))
                data["Gracz"]["Portfel"] += nagroda
                print("Bazyliony dodane na konto. Powrót do menu!")
                save_data(data, file_path)
                Menu()
            elif poziom == "2":
                nagroda = 500
                print("Nagroda pocieszenia:  {} bazylionów!".format(nagroda))
                data["Gracz"]["Portfel"] += nagroda
                print("Bazyliony dodane na konto. Powrót do menu!")
                save_data(data, file_path)
                Menu()
            elif poziom == "3":
                nagroda = 1000
                print("Nagroda pocieszenia:  {} bazylionów!".format(nagroda))
                data["Gracz"]["Portfel"] += nagroda
                print("Bazyliony dodane na konto. Powrót do menu!")
                save_data(data, file_path)
                Menu()




def Plecak():
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
    print('''
    Znajdujesz się w plecaku. Co chcesz sprawdzić?:
    1 - Rodzaje żetonów i ich umiejetności 
    2 - Persony gracza i przeciwnika
    3 - Statusy gracza i przeciwnika
    4 - EKRAN STARTOWY
    ''')
    a = str(input("Jaki jest twój wybór? (Wpisz od 1 do 4)"))
    if a == "1":
        print('''
            Dostępne rodzaje twoich zetonów:
            1 - Zetony Mocy
            2 - Zetony Obronny
            3 - Zetony Rozkazu
            4 - PLECAK
            ''')
        b = str(input("Jaki jest twój wybór? (Wpisz od 1 do 4)"))
        if b == "1":
            time.sleep(3)
            listaMoce()
            print('''
                        1 - Powrót do menu plecaka
                        2 - Powrót do ekranu startowego
                        ''')
            x = str(input("Jaki jest twój wybór? (1/2)"))
            if x == "1":
                time.sleep(3)
                Plecak()
            else:
                time.sleep(3)
                Menu()
        elif b == "2":
            time.sleep(3)
            listaObrony()
            print('''
                        1 - Powrót do menu plecaka
                        2 - Powrót do ekranu startowego
                        ''')
            x = str(input("Jaki jest twój wybór? (1/2)"))
            if x == "1":
                time.sleep(3)
                Plecak()
            else:
                time.sleep(3)
                Menu()
        elif b == "3":
            time.sleep(3)
            listaRozkazu()
            print('''
                      1 - Powrót do menu plecaka
                      2 - Powrót do ekranu startowego
                      ''')
            x = str(input("Jaki jest twój wybór? (1/2)"))
            if x == "1":
                time.sleep(3)
                Plecak()
            else:
                time.sleep(3)
                Menu()
        elif b == "4":
            time.sleep(3)
            Plecak()

    elif a == "2":
        print('''Jak działają "Persony"?:
        
        Jeżeli Persona jednego z zawodników to Płomienie, a drugiego to Światło, Mrok lub Las - pierwszy otrzymuje 150 punktów, drugiemu odejmujemy 50 punktów;
        Jeżeli Persona jednego z zawodników to Światło, a drugiego to Płomienie, Mrok lub Las - pierwszy otrzymuje 150 punktów, drugiemu odejmujemy 50 punktów;
        Jeżeli Persona jednego z zawodników to Mrok, a drugiego to Światło, Ocean lub Góra - pierwszy otrzymuje 150 punktów, drugiemu odejmujemy 50 punktów;
        Jeżeli Persona jednego z zawodników to Ocean, a drugiego to Płomienie, Góra lub Las - pierwszy otrzymuje 150 punktów, drugiemu odejmujemy 50 punktów;
        Jeżeli Persona jednego z zawodników to Las, a drugiego to Światło, Ocean lub Góra - pierwszy otrzymuje 150 punktów, drugiemu odejmujemy 50 punktów;
        Jeżeli Persona jednego z zawodników to Góra, a drugiego to Płomienie, Mrok lub Ocean - pierwszy otrzymuje 150 punktów, drugiemu odejmujemy 50 punktów;
        W przeciwnym wypadku każdy otrzymuje po 150 punktów.''')
        print('''
                  1 - Powrót do menu plecaka
                  2 - Powrót do ekranu startowego
                  ''')
        x = str(input("Jaki jest twój wybór? (1/2)"))
        if x == "1":
            time.sleep(3)
            Plecak()
        else:
            time.sleep(3)
            Menu()
    elif a == "3":
        print('''Jak działają "Statusy"?:

        Jeżeli Status jednego z zawodników to Helios, a drugiego to Phoenix lub Posejdon - pierwszy otrzymuje 200 punktów, drugiemu odejmujemy 50 punktów
        Jeżeli Status jednego z zawodników to Lassus, a drugiego to Hekate lub Supterra - pierwszy otrzymuje 200 punktów, drugiemu odejmujemy 50 punktów
        Jeżeli Status jednego z zawodników to Phoenix, a drugiego to Helios lub Posejdon - pierwszy otrzymuje 200 punktów, drugiemu odejmujemy 50 punktów
        Jeżeli Status jednego z zawodników to Hekate, a drugiego to Lassus lub Supterra - pierwszy otrzymuje 200 punktów, drugiemu odejmujemy 50 punktów
        Jeżeli Status jednego z zawodników to Posejdon, a drugiego to Helios lub Phoenix - pierwszy otrzymuje 200 punktów, drugiemu odejmujemy 50 punktów
        Jeżeli Status jednego z zawodników to Supterra, a drugiego to Lassus lub Hekate - pierwszy otrzymuje 200 punktów, drugiemu odejmujemy 50 punktów
        W przeciwnym wypadku każdy otrzymuje po 150 punktów.''')
        print('''
                  1 - Powrót do menu plecaka
                  2 - Powrót do ekranu startowego
                  ''')
        x = str(input("Jaki jest twój wybór? (1/2)"))
        if x == "1":
            time.sleep(3)
            Plecak()
        else:
            time.sleep(3)
            Menu()
    elif a == "4":
        time.sleep(3)
        Menu()
    else:
        print("Podano zły numer!")
        print("Spróbuj ponownie!")
        time.sleep(3)
        return Plecak()


def Sklep():
    def warunekpo():
        print('''Czy chcesz kontynuować zakupy?
    1 - Tak
    2 - Nie''')
        a = str(input("Co wybierasz?"))
        if a == "1":
            time.sleep(3)
            Sklep()
        elif a == "2":
            time.sleep(3)
            Menu()
        else:
            print("Podano zły numer!")
            print("Spróbuj ponownie!")
            time.sleep(3)
            warunekpo()

    kasa = data["Gracz"]["Portfel"]
    print("Stan konta {} bazylionów".format(kasa))
    print("Co chcesz zakupić?")
    print('''
    1 - 10x Żetony mocy na każdego rodzaju - 250 bazylionów
    2 - 10x Żetony obrony na każdego rodzaju - 500 bazylionów
    3 - 10x Żetony Rozkazu na każdego rodzaju - 1000 bazylionów
    4 - Powrót do menu''')
    x = str(input("Jaki jest twój wybór?"))
    if x == "1":
        if kasa >= 250:
            data["Spirala"]["Ilosc"] += 10
            data["Pogromer"]["Ilosc"] += 10
            data["Skrodo"]["Ilosc"] += 10
            data["Synteza"]["Ilosc"] += 10
            data["Dzeus"]["Ilosc"] += 10
            data["Wulkanium"]["Ilosc"] += 10
            data["Istoty"]["Ilosc"] += 10
            print("Żetony dodane do twojego plecaka!")
            print("Bazyliony pobrane z konta")
            data["Gracz"]["Portfel"] -= 250
            save_data(data, file_path)
            warunekpo()
        else:
            print("Nie masz wystarczająco bazylionów")
            warunekpo()
    elif x == "2":
        if kasa >= 500:
            data["MetaGolem"]["Ilosc"] += 10
            data["Tarczownik"]["Ilosc"] += 10
            data["Honor"]["Ilosc"] += 10
            print("Żetony dodane do twojego plecaka!")
            print("Bazyliony pobrane z konta")
            data["Gracz"]["Portfel"] -= 500
            save_data(data, file_path)
            warunekpo()
        else:
            print("Nie masz wystarczająco bazylionów")
            warunekpo()
    elif x == "3":
        if kasa >= 1000:
            data["Dominium"]["Ilosc"] += 10
            data["Przedwieczny"]["Ilosc"] += 10
            data["Prozny"]["Ilosc"] += 10
            print("Żetony dodane do twojego plecaka!")
            print("Bazyliony pobrane z konta")
            data["Gracz"]["Portfel"] -= 1000
            save_data(data, file_path)
            warunekpo()
        else:
            print("Nie masz wystarczająco bazylionów")
            warunekpo()
    elif x == "4":
        print("Wracasz do menu")
        time.sleep(3)
        Menu()
    else:
        print("Podano zły numer!")
        print("Spróbuj ponownie!")
        return


def cooldown(seconds):
    def decorator(func):
        last_called = [0]

        @wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_called[0]
            if elapsed < seconds:
                remaining = seconds - elapsed
                hours, remainder = divmod(remaining, 3600)
                minutes, sec = divmod(remainder, 60)
                print(f"Nagrody możesz odebrać za {int(hours)}h {int(minutes)}m {int(sec)}s .")
                return
            last_called[0] = time.time()
            return func(*args, **kwargs)
        return wrapper
    return decorator

@cooldown(3600)
def maszyna():
    take = str(input("Witaj wojowniku, co byś chciał otrzymać? (1 - dzienna nagroda, 2 - wylosowany zestaw)"))
    if take == "1":
        print("Oto twoja nagroda!")
        print("1000 bazylionów!")
        data["Gracz"]["Portfel"] += 1000
        print('''
        Portfel został uzupełniony!
        Następną nagrodę możesz odebrać za 1h
        Powrót do ekranu startowego
        ''')
        save_data(data, file_path)  # Zapisz zmiany w danych gracza
        time.sleep(3)
        return Menu()
    elif take == "2":
        zestawy = ["Zestaw Synztezy", "Zestaw Żywiołów", "Zetaw Pomiotu"]
        losuj = random.randint(0, 100)
        if losuj < 50:
            print('''Wylosowłeś dziś {} w którym znajduje się:
            - 5x Żeton Spirali
            - 5x Żeton Pogromer
            - 5x Żeton Istoty
            '''.format(zestawy[0]))
            data["Spirala"]["Ilosc"] += 10
            data["Pogromer"]["Ilosc"] += 10
            data["Istoty"]["Ilosc"] += 10
            print('''
            Plecak został uzupełniony!
            Następną nagrodę możesz odebrać za 1h
            Powrót do ekranu startowego
            ''')
            save_data(data, file_path)  # Zapisz zmiany w danych gracza
            time.sleep(3)
            return Menu()
        elif losuj >=50 and losuj <90:
            print('''Wylosowłeś dziś {} w którym znajduje się:
            - 5x Żeton MetaGolema
            - 5x Żeton Tarczownika
            - 5x Żeton Honoru
            '''.format(zestawy[1]))
            data["MetaGolem"]["Ilosc"] += 10
            data["Tarczownik"]["Ilosc"] += 10
            data["Honor"]["Ilosc"] += 10
            print('''
            Plecak został uzupełniony!
            Następną nagrodę możesz odebrać za 1h
            Powrót do ekranu startowego
            ''')
            save_data(data, file_path)  # Zapisz zmiany w danych gracza
            time.sleep(3)
            return Menu()
        else:
            print('''Wylosowłeś dziś {} w którym znajduje się:
            - 5x Żeton Dominium
            - 5x Żeton Przedwieczny
            - 5x Żeton Próżny
            '''.format(zestawy[2]))
            data["Dominium"]["Ilosc"] += 10
            data["Przedwieczny"]["Ilosc"] += 10
            data["Prozny"]["Ilosc"] += 10

            print('''
            Plecak został uzupełniony!
            Następną nagrodę możesz odebrać za 1h
            Powrót do ekranu startowego
            ''')
            save_data(data, file_path)  # Zapisz zmiany w danych gracza
            time.sleep(3)
            return Menu()

def Menu():

    print('''
    Witaj w ekranie startowym BakuGame:
    1 - Plecak
    2 - Przeciwnicy
    3 - Nagrody
    4 - Sklep
    ''')
    x = str(input("Co zamierzasz?"))
    if x == "1":
        time.sleep(1)
        Plecak()
    elif x == "2":
        time.sleep(1)
        wybierz()
    elif x == "3":
        time.sleep(1)
        maszyna()
    elif x == "4":
        time.sleep(1)
        Sklep()
    else:
        print("Podano zły numer!")
        print("Spróbuj ponownie!")
        time.sleep(1)
        return Menu()

    save_data(data, file_path)

Menu()
