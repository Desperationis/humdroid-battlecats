import time
import os
import signal
import sys

from humdroid.wrappers.ScrcpyWrapper import scrcpy
from humdroidbc.HumdroidBC import HumdroidBC
from humdroidbc.TemplateGroup import TemplateGroup
import bcstages


humbc = HumdroidBC()

# Launch Battlecats first to force screen orientation change so the
# scrcpy stream doesn't freak out
humbc.RestartBC()
time.sleep(2)
humbc.Start()

def signal_handler(signal, frame):
    humbc.Close()
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)



HOME = os.path.expanduser("~")
titleGroup = TemplateGroup(0)
titleGroup.AddTemplate(HOME + "/humdroid_images/titlescreen/skip.png")
titleGroup.AddTemplate(HOME + "/humdroid_images/titlescreen/play.png")
titleGroup.AddTemplate(HOME + "/humdroid_images/titlescreen/legend.png")
titleGroup.AddTemplate(HOME + "/humdroid_images/titlescreen/oklegend.png")
titleGroup.AddTemplate(HOME + "/humdroid_images/titlescreen/upgrade.png")

stageGroup = TemplateGroup(1)
stageGroup.AddTemplate(HOME + "/humdroid_images/eventselect/start.png")
stageGroup.AddTemplate(HOME + "/humdroid_images/eventselect/stages/weekend_stage.png")
stageGroup.AddTemplate(HOME + "/humdroid_images/eventselect/stages/monday_stage.png")
stageGroup.AddTemplate(HOME + "/humdroid_images/eventselect/equip.png")
stageGroup.AddTemplate(HOME + "/humdroid_images/eventselect/formation.png")
stageGroup.AddTemplate(HOME + "/humdroid_images/eventselect/leadershipYes.png")
stageGroup.AddTemplate(HOME + "/humdroid_images/eventselect/attack.png")

catGroup = TemplateGroup(2)
# Auto load all cats in directory
CATSPATH = HOME + "/humdroid_images/cats"
for (dirpath, dirnames, filenames) in os.walk(CATSPATH):
    for file in filenames:
        if ".png" in file:
            catFile = os.path.join(CATSPATH, file)
            catGroup.AddTemplate(catFile)
            print("Loaded " + catFile + " as a cat.")

battleGroup = TemplateGroup(3)
battleGroup.AddTemplate(HOME + "/humdroid_images/battle/dropreward.png") 
battleGroup.AddTemplate(HOME + "/humdroid_images/battle/battleok.png") 

humbc.LoadTemplateGroup(titleGroup)
humbc.LoadTemplateGroup(stageGroup)
humbc.LoadTemplateGroup(catGroup)
humbc.LoadTemplateGroup(battleGroup)


# Go to main page
while True:
    humbc.Screenshot()
   
    matches = humbc.CompareGroup(titleGroup.GetGroup())
    if len(matches) != 0:
        m = matches[0]
        if m["id"] == humbc.HashID(titleGroup["upgrade"]):
            break
        else:
            humbc.Touch(m["x"], m["y"])




def waitUntilClicked(ID : int, duration=-1.0):
    while True:
        humbc.Screenshot()

        matches = humbc.CompareID(ID)
        for m in matches:
            if m["id"] == ID:
                humbc.Touch(m["x"], m["y"], duration)
                return


def GoToStage(stage):
    print("Trying to click start...")
    startID = humbc.HashID(stageGroup["start"])
    waitUntilClicked(startID, 0.2)
    time.sleep(3) # Transition
    print("Clicked start")

    while True:
        stageID = humbc.HashID(stageGroup[stage])
        humbc.Screenshot()
        touched = False
        matches = humbc.CompareID(stageID, 0.8)
        for m in matches:
            if m["id"] == stageID:
                humbc.Touch(m["x"], m["y"], 0.5)
                touched = True

        if touched:
            print("Found stage, clicked it.")
            break


        print("Did not find stage. Scrolling...")
        screenSize = humbc.GetScreenDimensions()
        swipeX = screenSize[0] / 2
        swipeYtop = screenSize[1] / 6 * 2
        swipeYbottom = (screenSize[1] / 6) * 4
        humbc.Swipe(swipeX, swipeYbottom, swipeX, swipeYtop, 5, 0.02)
        time.sleep(1)


def Equip():
    equipID = humbc.HashID(stageGroup["equip"])
    formationID = humbc.HashID(stageGroup["formation"])
    waitUntilClicked(equipID, 2)
    waitUntilClicked(formationID)

def Battle():
    attackID = humbc.HashID(stageGroup["attack"])
    leadershipID = humbc.HashID(stageGroup["leadershipYes"])

    waitUntilClicked(attackID)
    time.sleep(3)
    while True:
        humbc.Screenshot()
        matches = humbc.CompareGroup(stageGroup.GetGroup())
        print("Finding any potential prompts after pressing attack...")

        done = False
        for m in matches:
            if m["id"] == attackID:
                print("Clicked attack prompt once more")
                humbc.Touch(m["x"], m["y"])
                done = True
            if m["id"] == leadershipID:
                print("Clicked leadership prompt.")
                humbc.Touch(m["x"], m["y"])
                time.sleep(3)

        if done or len(matches) == 0:
            print("Did not find leadership prompt. Going on to battle!")
            break

    # Wait for any cat combo's to fade away
    time.sleep(5)
    matches = []
    while True:
        humbc.Screenshot()
        matches = humbc.CompareGroup(catGroup.GetGroup(), 0.7)
        if len(matches) > 0:
            break


    #bcstages.xpStageInsane(matches, catGroup, humbc)
    bcstages.mondayStage(matches, catGroup, humbc)
        
    print("Searching for battleok")
    done = False
    while not done:
        humbc.Screenshot()
        matches = humbc.CompareGroup(battleGroup.GetGroup(), 0.8)

        print(matches)
        for m in matches:
            humbc.Touch(m["x"], m["y"])
            if m["id"] == humbc.HashID(battleGroup["battleok"]):
                print("Pressed battle OK. Should be heading to menu now.")
                done = True

    time.sleep(2) # Wait for transition

for i in range(15):
    GoToStage("monday_stage")
    Equip()
    Battle()
    print("looping again")


humbc.Close()
