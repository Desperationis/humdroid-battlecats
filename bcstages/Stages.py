import time

######################### DEBUG ############################
def printIDs(cats, humbc):
    for i in cats.GetTemplates():
        print("Cat " + i + " has ID " + str(humbc.HashID(i)))
######################### DEBUG ############################

def mondayStage(matches, cats, humbc):
    # Spam tactic
    units = ["ramen", "pogocat", "maniclion"]
    units = [ humbc.HashID(cats[unit]) for unit in units ]

    printIDs(cats, humbc)
    print("Units: " + str(units))
    print("Matches: " + str(matches))

    for i in range(15):
        for m in matches:
            if m["id"] in units:
                humbc.Touch(m["x"], m["y"])
                time.sleep(0.3)

def tuesdayStage(matches, cats, humbc):
    # Spam lion tactic
    units = [ "crazedbahamut", "maniclion", "lion" ]
    units = [ humbc.HashID(cats[unit]) for unit in units ]

    printIDs(cats, humbc)
    print("Units: " + str(units))
    print("Matches: " + str(matches))

    for i in range(13):
        for m in matches:
            if m["id"] in units:
                humbc.Touch(m["x"], m["y"])
                time.sleep(0.2)

def wednesdayStage(matches, cats, humbc):
    # Spam lion tactic
    units = [ "maniclion", "ramen" ]
    units = [ humbc.HashID(cats[unit]) for unit in units ]

    printIDs(cats, humbc)
    print("Units: " + str(units))
    print("Matches: " + str(matches))

    for i in range(30):
        for m in matches:
            if m["id"] in units:
                humbc.Touch(m["x"], m["y"])
                time.sleep(0.3)

def growingBlue(matches, cats, humbc):
    units = [ "ramen", "paris" ]
    units = [ humbc.HashID(cats[unit]) for unit in units ]

    printIDs(cats, humbc)
    print("Units: " + str(units))
    print("Matches: " + str(matches))

    time.sleep(8)

    for i in range(30):
        for m in matches:
            if m["id"] in units:
                humbc.Touch(m["x"], m["y"])
                time.sleep(0.3)

    units = [ "ramen", "paris", "psychomaniac", "eaglelegend", "axe_uber" ]
    units = [ humbc.HashID(cats[unit]) for unit in units ]

    printIDs(cats, humbc)
    print("Units: " + str(units))
    print("Matches: " + str(matches))

    time.sleep(8)

    for i in range(20):
        for m in matches:
            if m["id"] in units:
                humbc.Touch(m["x"], m["y"])
                time.sleep(0.3)

def growingYellow(matches, cats, humbc):
    units = [ "ramen", "paris", "jizo" ]
    units = [ humbc.HashID(cats[unit]) for unit in units ]

    printIDs(cats, humbc)
    print("Units: " + str(units))
    print("Matches: " + str(matches))

    time.sleep(8)

    for i in range(45):
        for m in matches:
            if m["id"] in units:
                humbc.Touch(m["x"], m["y"])
                time.sleep(0.3)

