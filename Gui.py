from appJar import gui
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

    app = gui("MusicShifter", "600x300")
    app.addLabel("title", "MusicShifter")
    app.addLabelEntry("Score Name")
    app.addLabelEntry("New File Name")
    app.addLabelNumericEntry("Row To Change")
    app.addLabelNumericEntry("Amount To Shift Down By")
    app.addButton("Enter", press)
    app.go()



if __name__ == "__main__":
    createGui()
