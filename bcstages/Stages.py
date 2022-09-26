import time

def lionCheese(matches, cats, humbc):
    clickCount = 0
    while clickCount < 50:
        for m in matches:
            if m["id"] == humbc.HashID(cats["maniclion"]):
                humbc.Touch(m["x"], m["y"])
                clickCount += 1

        time.sleep(0.2)

def xpStageInsane(matches, cats, humbc):
    time.sleep(20)

    for i in range(12):
        print("First half of battle, step " + str(i))
        for m in matches:
            if m["id"] == humbc.HashID(cats["ramen"]):
                humbc.Touch(m["x"], m["y"])
                time.sleep(0.3)

            elif m["id"] == humbc.HashID(cats["pogocat"]):
                humbc.Touch(m["x"], m["y"])
                time.sleep(0.3)
                
            elif m["id"] == humbc.HashID(cats["crazederaser"]):
                humbc.Touch(m["x"], m["y"])
                time.sleep(0.3)
                
            elif m["id"] == humbc.HashID(cats["jizo"]):
                humbc.Touch(m["x"], m["y"])
                time.sleep(0.3)
            

        time.sleep(0.3)


    for i in range(12):
        print("Second half of battle, step " + str(i))
        for m in matches:
            if m["id"] == humbc.HashID(cats["ramen"]):
                humbc.Touch(m["x"], m["y"])
                time.sleep(0.3)

            elif m["id"] == humbc.HashID(cats["pogocat"]):
                humbc.Touch(m["x"], m["y"])
                time.sleep(0.3)
                
            elif m["id"] == humbc.HashID(cats["crazederaser"]):
                humbc.Touch(m["x"], m["y"])
                time.sleep(0.3)
                
            elif m["id"] == humbc.HashID(cats["jizo"]):
                humbc.Touch(m["x"], m["y"])
                time.sleep(0.3)
            
            elif m["id"] == humbc.HashID(cats["eaglelegend"]):
                humbc.Touch(m["x"], m["y"])
                time.sleep(0.3)
            
            elif m["id"] == humbc.HashID(cats["crazedbahamut"]):
                humbc.Touch(m["x"], m["y"])
                time.sleep(0.3)
            

        time.sleep(0.3)

    print("Battle done.")


