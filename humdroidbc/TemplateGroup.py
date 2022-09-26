import os

class TemplateGroup:
    """ 
        Groups up template images to make them easier to pass onto
        humdroid.
    """

    def __init__(self, group : int):
        self.group = group
        self.images = {}

    def __getitem__(self, key):
        return self.GetByName(key)

    def _GetName(self, fullpath : str):
        """
            Given a path to a file, return the name of that file without the
            extension.
        """

        if not os.path.isfile(fullpath):
            raise Exception(fullpath + " is not a path to a file.")

        basename = os.path.basename(fullpath)
        name = basename.split(".")[0]

        return name


    def AddTemplate(self, fullpath : str):
        """
            Takes in the absolute path to a template image and adds it to the
            table. If the path is not an absolute path, an exception is thrown.
        """

        if not os.path.isabs(fullpath):
            raise Exception(fullpath + " is not an absolute path.")

        name = self._GetName(fullpath)
        self.images[name] = fullpath


    def GetByName(self, name : str):
        """
            Tries to return the full path of a template by its filename. For
            example, the name of "/home/user/image_2.png" would just be
            "image_2".

            If the corresponding image is not found, return None.
        """

        if name in self.images:
            return self.images[name]

        return None

    def GetGroup(self) -> int:
        return self.group

    def GetTemplates(self):
        """
            Returns a list of the full template paths.
        """

        templates = []
        for key in self.images:
                templates.append(self.images[key])

        return templates




