from appJar import gui

from PartExporter import purePartExporter
from PdfExporter import pdfExporter
from Shifter import shifter


def createGui():
    def press(button):
        if button == "Enter":
            name = app.getEntry("Score Name")
            file = app.getEntry("New File Name")
            row = int(app.getEntry("Row To Change")) - 1
            shift = int(app.getEntry("Amount To Shift Down By"))
            print(name, file, row, shift)
            shifter(name, file, row, shift)

        if button == "Export PDFs":
            name = app.getEntry("Score Name")
            file = app.getEntry("New File Name")
            parts = app.getEntry("Part Names").split(", ")
            pdfExporter(name, file, parts)

        if button == "Export Single Piano":
            name = app.getEntry("Score Name")
            file = app.getEntry("New File Name")
            parts = app.getEntry("Part Names").split(", ")
            purePartExporter(name, file, parts)

    app = gui("MusicShifter", "600x300")
    app.addLabel("title", "MusicShifter")
    app.addLabelEntry("Score Name")
    app.addLabelEntry("New File Name")
    app.addLabelNumericEntry("Row To Change")
    app.addLabelNumericEntry("Amount To Shift Down By")
    app.addLabelEntry("Part Names")
    app.addButtons(["Enter", "Export PDFs", "Export Single Piano"], press)
    app.go()


if __name__ == "__main__":
    createGui()
