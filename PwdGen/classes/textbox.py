"""
@Author  : GUETTE Steven
@Class   : TextBox
@Version : 1.0.0
@Since   : 2023
"""

from classes.whiteshield import WShield


class TextBox:
    (CornerChar, VLineChar, HLineChar) = ("+", "|", "-")

    def __init__(self, content, title=""):
        self.Box = ""
        self.Title = title
        self.MaxLength = 0
        self.Content = list()

        if WShield.IsList(content):
            if WShield.IsString(self.Title):
                self.Title = f"| {title.capitalize()} |"
            self.Content = content

            self.SetMaxLength()
            self.GenerateBox()

            # region METHODS

    def GenerateBox(self):
        textBlock = self.GetContent()

        if not WShield.IsString(self.Title):
            self.Title = TextBox.HLineChar * (self.MaxLength + 2)

        self.Box = "\n" + " " * 4 + TextBox.CornerChar + TextBox.HLineChar * (len(self.Title) - 2) + TextBox.CornerChar
        self.Box += "\n" + TextBox.CornerChar + TextBox.HLineChar * 3 + self.Title + TextBox.HLineChar * (
                    self.MaxLength - len(self.Title) - 1) + TextBox.CornerChar
        self.Box += "\n" + TextBox.VLineChar + " " * 3 + TextBox.CornerChar + TextBox.HLineChar * (
                    len(self.Title) - 2) + TextBox.CornerChar + " " * (
                                self.MaxLength - len(self.Title) - 1) + TextBox.VLineChar + "\n"

        for line in textBlock:
            self.Box += TextBox.VLineChar + line + TextBox.VLineChar + "\n"

        self.Box += TextBox.CornerChar + TextBox.HLineChar * (self.MaxLength + 2) + TextBox.CornerChar

    # endregion

    # region SETTERS

    def SetMaxLength(self):
        maxLength = 0

        for line in self.Content:
            if len(line) > maxLength:
                maxLength = len(line)

        if len(self.Title) > maxLength:
            self.MaxLength = len(self.Title) + 1
        else:
            self.MaxLength = maxLength + 1

    # endregion

    # region GETTERS

    def GetContent(self):
        lines = list()

        for line in self.Content:
            lines.append(" " + line + (" " * (self.MaxLength - len(line) + 1)))

        return lines

    def GetBox(self):
        return self.Box

    # endregion
