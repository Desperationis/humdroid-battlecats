import time

def lionCheese(matches, cats, GetID, scrcpyClient):
    clickCount = 0
    while clickCount < 50:
        for m in matches:
            if m["id"] == GetID(cats, "maniclion"):
                scrcpyClient.Touch(m["x"], m["y"])
                clickCount += 1

        time.sleep(0.2)

def xpStageInsane(matches, cats, GetID, scrcpyClient):
    time.sleep(20)

    for i in range(12):
        print("First half of battle, step " + str(i))
        for m in matches:
            if m["id"] == GetID(cats, "ramen"):
                scrcpyClient.Touch(m["x"], m["y"])
                time.sleep(0.3)

            elif m["id"] == GetID(cats, "pogocat"):
                scrcpyClient.Touch(m["x"], m["y"])
                time.sleep(0.3)
                
            elif m["id"] == GetID(cats, "crazederaser"):
                scrcpyClient.Touch(m["x"], m["y"])
                time.sleep(0.3)
                
            elif m["id"] == GetID(cats, "jizo"):
                scrcpyClient.Touch(m["x"], m["y"])
                time.sleep(0.3)
            

        time.sleep(0.3)


    for i in range(12):
        print("Second half of battle, step " + str(i))
        for m in matches:
            if m["id"] == GetID(cats, "ramen"):
                scrcpyClient.Touch(m["x"], m["y"])
                time.sleep(0.3)

            elif m["id"] == GetID(cats, "pogocat"):
                scrcpyClient.Touch(m["x"], m["y"])
                time.sleep(0.3)
                
            elif m["id"] == GetID(cats, "crazederaser"):
                scrcpyClient.Touch(m["x"], m["y"])
                time.sleep(0.3)
                
            elif m["id"] == GetID(cats, "jizo"):
                scrcpyClient.Touch(m["x"], m["y"])
                time.sleep(0.3)
            
            elif m["id"] == GetID(cats, "eaglelegend"):
                scrcpyClient.Touch(m["x"], m["y"])
                time.sleep(0.3)
            
            elif m["id"] == GetID(cats, "crazedbahamut"):
                scrcpyClient.Touch(m["x"], m["y"])
                time.sleep(0.3)
            

        time.sleep(0.3)

    print("Battle done.")


