from Postac import PostacG, PostacP

postacG = PostacG()
postacP = PostacP()

def StatusPostacG(MocG, postacG, MocP, postacP):
    if postacG["Status"] == "Helios" and (postacP["Status"] == "Phoenix" or postacP["Status"] == "Posejdon"):
        MocG += 200
        MocP -= 50
        print("Status Helios aktywacja - Boost mocy Gracza - 200 punktów! Moc Przeciwnika zmniejszona - 50 punktów!")
    elif postacG["Status"] == "Lassus" and (postacP["Status"] == "Hekate" or postacP["Status"] == "Supterra"):
        MocG += 200
        MocP -= 50
        print("Status Lassus aktywacja - Boost mocy Gracza - 200 punktów! Moc Przeciwnika zmniejszona - 50 punktów!")
    elif postacG["Status"] == "Phoenix" and (postacP["Status"] == "Helios" or postacP["Status"] == "Posejdon"):
        MocG += 200
        MocP -= 50
        print("Status Phoenix aktywacja - Boost mocy Gracza - 200 punktów! Moc Przeciwnika zmniejszona - 50 punktów!")
    elif postacG["Status"] == "Hekate" and (postacP["Status"] == "Lassus" or postacP["Status"] == "Supterra"):
        MocG += 200
        MocP -= 50
        print("Status Hekate aktywacja - Boost mocy Gracza - 200 punktów! Moc Przeciwnika zmniejszona - 50 punktów!")
    elif postacG["Status"] == "Posejdon" and (postacP["Status"] == "Helios" or postacP["Status"] == "Phoenix"):
        MocG += 200
        MocP -= 50
        print("Status Posejdon aktywacja - Boost mocy Gracza - 200 punktów! Moc Przeciwnika zmniejszona - 50 punktów!")
    elif postacG["Status"] == "Supterra" and (postacP["Status"] == "Lassus" or postacP["Status"] == "Hekate"):
        MocG += 200
        MocP -= 50
        print("Status Supterra aktywacja - Boost mocy Gracza - 200 punktów! Moc Przeciwnika zmniejszona - 50 punktów!")
    else:
        MocG += 150
        print("Status Mocy aktywacja - Boost mocy Gracza - 150 punktów!")
    return MocG, MocP

def StatusPostacP(MocP, postacP, MocG, postacG):
    if postacP["Status"] == "Helios" and (postacG["Status"] == "Phoenix" or postacG["Status"] == "Posejdon"):
        MocP += 200
        MocG -= 50
        print("Status Helios aktywacja - Boost mocy Przeciwnika - 200 punktów! Moc Gracza zmniejszona - 50 punktów!")
    elif postacP["Status"] == "Lassus" and (postacG["Status"] == "Hekate" or postacG["Status"] == "Supterra"):
        MocP += 200
        MocG -= 50
        print("Status Lassus aktywacja - Boost mocy Przeciwnika - 200 punktów! Moc Gracza zmniejszona - 50 punktów!")
    elif postacP["Status"] == "Phoenix" and (postacG["Status"] == "Helios" or postacG["Status"] == "Posejdon"):
        MocP += 200
        MocG -= 50
        print("Status Phoenix aktywacja - Boost mocy Przeciwnika - 200 punktów! Moc Gracza zmniejszona - 50 punktów!")
    elif postacP["Status"] == "Hekate" and (postacG["Status"] == "Lassus" or postacG["Status"] == "Supterra"):
        MocP += 200
        MocG -= 50
        print("Status Hekate aktywacja - Boost mocy Przeciwnika - 200 punktów! Moc Gracza zmniejszona - 50 punktów!")
    elif postacP["Status"] == "Posejdon" and (postacG["Status"] == "Helios" or postacG["Status"] == "Phoenix"):
        MocP += 200
        MocG -= 50
        print("Status Posejdon aktywacja - Boost mocy Przeciwnika - 200 punktów! Moc Gracza zmniejszona - 50 punktów!")
    elif postacP["Status"] == "Supterra" and (postacG["Status"] == "Lassus" or postacG["Status"] == "Hekate"):
        MocP += 200
        MocG -= 50
        print("Status Supterra aktywacja - Boost mocy Przeciwnika - 200 punktów! Moc Gracza zmniejszona - 50 punktów!")
    else:
        MocP += 150
        print("Status Mocy aktywacja - Boost mocy Przeciwnika - 150 punktów!")
    return MocP, MocG