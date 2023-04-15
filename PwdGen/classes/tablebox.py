"""
@Author  : GUETTE Steven
@Class   : TableBox
@Version : 1.0.0
@Since   : 2023
"""

from classes.whiteshield import WShield
from classes.textbox import TextBox


class TableBox(TextBox):
    BoxWidth = 1
    ColumnsWidth = {}

    def __init__(self, anList, title=""):
        super().__init__("", title)

        if WShield.IsList(anList):
            TableBox.SetWidths(anList)
            self.SetTableBox(anList)

    def SetTableBox(self, content):
        self.Box = TableBox.GetTitleFormatted(self.Title)
        self.Box += TableBox.GetHeader(content[0])

        for dictionnary in content:
            for key in dictionnary:
                self.Box += TableBox.VLineChar + f" {dictionnary[key]}"
                self.Box += " " * (TableBox.ColumnsWidth[key] - len(dictionnary[key]) - 1)
            self.Box += "{}\n".format(TableBox.VLineChar)

        for element in TableBox.GetHeaderElements(content[0]):
            self.Box += TableBox.CornerChar + TableBox.HLineChar * (TableBox.ColumnsWidth[element])
        self.Box += "{}\n".format(TableBox.CornerChar)

    def SetWidths(cls, content):
        for line in content:
            for element in line:
                if element not in TableBox.ColumnsWidth:
                    TableBox.ColumnsWidth[element] = len(line[element]) + 2
                else:
                    if (len(line[element]) + 2) > TableBox.ColumnsWidth[element]:
                        TableBox.ColumnsWidth[element] = len(line[element]) + 2

        for column in TableBox.ColumnsWidth:
            TableBox.BoxWidth += (TableBox.ColumnsWidth[column] + 1)

    SetWidths = classmethod(SetWidths)

    def GetHeaderElements(cls, firstLine):
        headerElements = list()

        for key in firstLine:
            headerElements.append(key)

        return headerElements

    GetHeaderElements = classmethod(GetHeaderElements)

    def GetHeader(cls, firstLine):
        headerElements = TableBox.GetHeaderElements(firstLine)
        header = ""

        for element in headerElements:
            header += cls.CornerChar + cls.HLineChar * (cls.ColumnsWidth[element])
        header += cls.CornerChar + "\n"

        for element in headerElements:
            width = cls.ColumnsWidth[element]
            element = element.capitalize()

            header += cls.VLineChar + element.center(width)
        header += cls.VLineChar + "\n"

        for element in headerElements:
            header += cls.CornerChar + cls.HLineChar * (cls.ColumnsWidth[element])
        header += cls.CornerChar + "\n"

        return header

    GetHeader = classmethod(GetHeader)

    def GetTitleFormatted(cls, title):
        titleLine = ""

        if WShield.IsString(title):
            titleLine = cls.CornerChar + cls.HLineChar * (cls.BoxWidth - 2) + cls.CornerChar
            titleLine += "\n" + cls.VLineChar + title.center(cls.BoxWidth - 2) + cls.VLineChar + "\n"

        return titleLine

    GetTitleFormatted = classmethod(GetTitleFormatted)
