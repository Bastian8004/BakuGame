from Postac import PostacP, PostacG


postacG = PostacG()
postacP = PostacP()

def kontryGracza(postacG, postacP, MocP, MocG):
    if postacG["Persona"] == "Persona Płomieni" and (postacP["Persona"] == "Persona Światła" or postacP["Persona"] == "Persona Mroku" or postacP["Persona"] == "Persona Lasu"):
        MocG += 150
        MocP -= 50
        print(postacG["Persona"], "- Boost mocy Gracza - 150 punktów! Moc Przeciwnika zmniejszona - 50 punktów!")
    elif postacG["Persona"] == "Persona Światła" and (postacP["Persona"] == "Persona Płomieni" or postacP["Persona"] == "Persona Mroku" or postacP["Persona"] == "Persona Lasu"):
        MocG += 150
        MocP -= 50
        print(postacG["Persona"], "- Boost mocy Gracza - 150 punktów! Moc Przeciwnika zmniejszona - 50 punktów!")
    elif postacG["Persona"] == "Persona Mroku" and (postacP["Persona"] == "Persona Światła" or postacP["Persona"] == "Persona Oceanu" or postacP["Persona"] == "Persona Gór"):
        MocG += 150
        MocP -= 50
        print(postacG["Persona"], "- Boost mocy Gracza - 150 punktów! Moc Przeciwnika zmniejszona - 50 punktów!")
    elif postacG["Persona"] == "Persona Oceanu" and (postacP["Persona"] == "Persona Płomieni" or postacP["Persona"] == "Persona Lasu" or postacP["Persona"] == "Persona Gór"):
        MocG += 150
        MocP -= 50
        print(postacG["Persona"], "- Boost mocy Gracza - 150 punktów! Moc Przeciwnika zmniejszona - 50 punktów!")
    elif postacG["Persona"] == "Persona Lasu" and (postacP["Persona"] == "Persona Światła" or postacP["Persona"] == "Persona Oceanu" or postacP["Persona"] == "Persona Gór"):
        MocG += 150
        MocP -= 50
        print(postacG["Persona"], "- Boost mocy Gracza - 150 punktów! Moc Przeciwnika zmniejszona - 50 punktów!")
    elif postacG["Persona"] == "Persona Gór" and (postacP["Persona"] == "Persona Płomieni" or postacP["Persona"] == "Persona Mroku" or postacP["Persona"] == "Persona Oceanu"):
        MocG += 150
        MocP -= 50
        print(postacG["Persona"], "- Boost mocy Gracza - 150 punktów! Moc Przeciwnika zmniejszona - 50 punktów!")
    else:
        MocG += 150
        print(postacG["Persona"], "- Boost mocy Gracza - 150 punktów!")
    return MocG, MocP

def kontryPrzeciwnika(postacG, postacP, MocP, MocG):
    if postacP["Persona"] == "Persona Płomieni" and (postacG["Persona"] == "Persona Światła" or postacG["Persona"] == "Persona Mroku" or postacG["Persona"] == "Persona Lasu"):
        MocP += 150
        MocG -= 50
        print(postacP["Persona"], "- Boost mocy Przeciwnika - 150 punktów! Moc Gracza zmniejszona - 50 punktów!")
    elif postacP["Persona"] == "Persona Światła" and (postacG["Persona"] == "Persona Płomieni" or postacG["Persona"] == "Persona Mroku" or postacG["Persona"] == "Persona Lasu"):
        MocP += 150
        MocG -= 50
        print(postacP["Persona"], "- Boost mocy Przeciwnika - 150 punktów! Moc Gracza zmniejszona - 50 punktów!")
    elif postacP["Persona"] == "Persona Mroku" and (postacG["Persona"] == "Persona Światła" or postacG["Persona"] == "Persona Oceanu" or postacG["Persona"] == "Persona Gór"):
        MocP += 150
        MocG -= 50
        print(postacP["Persona"], "- Boost mocy Przeciwnika - 150 punktów! Moc Gracza zmniejszona - 50 punktów!")
    elif postacP["Persona"] == "Persona Oceanu" and (postacG["Persona"] == "Persona Płomieni" or postacG["Persona"] == "Persona Lasu" or postacG["Persona"] == "Persona Gór"):
        MocP += 150
        MocG -= 50
        print(postacP["Persona"], "- Boost mocy Przeciwnika - 150 punktów! Moc Gracza zmniejszona - 50 punktów!")
    elif postacP["Persona"] == "Persona Lasu" and (postacG["Persona"] == "Persona Światła" or postacG["Persona"] == "Persona Oceanu" or postacG["Persona"] == "Persona Gór"):
        MocP += 150
        MocG -= 50
        print(postacP["Persona"], "- Boost mocy Przeciwnika - 150 punktów! Moc Gracza zmniejszona - 50 punktów!")
    elif postacP["Persona"] == "Persona Gór" and (postacG["Persona"] == "Persona Płomieni" or postacG["Persona"] == "Persona Mroku" or postacG["Persona"] == "Persona Oceanu"):
        MocP += 150
        MocG -= 50
        print(postacP["Persona"], "- Boost mocy Przeciwnika - 150 punktów! Moc Gracza zmniejszona - 50 punktów!")
    else:
        MocP += 150
        print(postacP["Persona"], "- Boost mocy Przeciwnika - 150 punktów!")
    return MocG, MocP


