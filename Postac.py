import random

def PostacG():
    persona = random.choice(["Persona Płomieni", "Persona Światła", "Persona Mroku", "Persona Oceanu", "Persona Lasu", "Persona Gór"])
    moc = random.randint(250, 350)
    status = random.choice(["Phoenix", "Helios", "Hekate", "Posejdon", "Lassus", "Supterra"])
    nazw = random.choice(["Pyrus", "Haos", "Drake", "Tryton", "Forres", "Mountras"])
    pNazw = status + " " + nazw

    PostacG = {
        "Nazwa Postaci Gracza": str(pNazw),
        "Persona": str(persona),
        "Moc": moc,
        "Status": str(status)
    }

    return PostacG

def PostacP():
    persona = random.choice(["Persona Płomieni", "Persona Światła", "Persona Mroku", "Persona Oceanu", "Persona Lasu", "Persona Gór"])
    moc = random.randint(200, 300)
    status = random.choice(["Phoenix", "Helios", "Hekate", "Posejdon", "Lassus", "Supterra"])
    nazw = random.choice(["Pyrus", "Haos", "Drake", "Tryton", "Forres", "Mountras"])
    pNazw = status + " " + nazw


    PostacP = {
        "Nazwa Postaci Przeciwnika": str(pNazw),
        "Persona": str(persona),
        "Moc": moc,
        "Status": str(status),
    }

    return PostacP

































