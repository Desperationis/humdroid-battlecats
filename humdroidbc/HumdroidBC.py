import os
import subprocess
import time
from humdroid.IPC import CVRequester
from humdroid.IPC import CVServer
from humdroid.wrappers import ScrcpyWrapper
from .TemplateGroup import TemplateGroup


class HumdroidBC:
    """
        Uses humdroid to control battlecats.
    """

    def __init__(self):
        # Setup environment
        self.SCREEN_DIR = "/tmp/humdroidbc"
        self.SCREEN_PATH = self.SCREEN_DIR + "/capture.png"
        if not os.path.exists(self.SCREEN_DIR):
            os.makedirs(self.SCREEN_DIR)

        self.server = CVServer()
        # TODO: Modify humdroid to allow requester to be Start()


        # Set the resolution and bitrate to be low for extreme speed. humdroid
        # doesn't need a super high resolution image to be able to make out BC
        # UI. This allows humdroidbc to be run on embedded devices.
        self.scrcpyClient = ScrcpyWrapper(500, 2000000)

    def Start(self):
        # Start up OpenCV server, then sockets.
        self.server.Start()
        time.sleep(2)
        self.requester = CVRequester()

    def Close(self):
        # Close sockets first to prevent kernel from blocking port for a few
        # minutes
        self.requester.Close()
        self.server.Close()

    def CompareGroup(self, group : int, minConfidence = 0.95):
        """ Checks if any images in a template group are in latest taken
            screenshot. Returns a list of dict's detailing any matches.
        """

        matches = self.requester.CompareGroup(self.SCREEN_PATH, group, minConfidence)["matches"]

        return matches

    def CompareID(self, ID : int, minConfidence = 0.95):
        """
            Checks if a certain template is in the latest taken screenshot.
            Returns a list of dict's detailing any matches.
        """

        matches = self.requester.CompareID(self.SCREEN_PATH, ID, minConfidence)["matches"]

        return matches

    def HashID(self, fullpath):
        """
            Given a full path to a template, return the associated ID that is used to identify with it with humdroid.
        """

        return self.requester.GetIDHash(fullpath)



    def LoadTemplateGroup(self, templateGroup : TemplateGroup):
        # Load all images in a TemplateGroup to humdroid.
        templates = templateGroup.GetTemplates()
        for template in templates:
            self.requester.LoadImage(template, templateGroup.GetGroup())


    def Touch(self, x : int, y : int, duration = -1.0):
        """ Touches screen at x, y """
        self.scrcpyClient.Touch(x, y, duration)

    def Swipe(self, start_x: int, start_y: int, end_x: int, end_y: int, move_step_length: int = 5, move_steps_delay: float = 0.005):
         self.scrcpyClient.Swipe(start_x, start_y, end_x, end_y, move_step_length, move_steps_delay)

    def GetScreenDimensions(self):
        return self.scrcpyClient.GetResolution()

    def RestartBC(self):
        self.ADBApi("restartBattleCats")

    def Screenshot(self):
        screenshot = self.scrcpyClient.LastFrame()
        screenshot.save(self.SCREEN_PATH)



    def ADBApi(self, command : str):
        """
            Runs a command from adbAPI.bash and returns status code.
        """
        return subprocess.run("source adbAPI.bash; " + command, shell=True, executable='/bin/bash')
