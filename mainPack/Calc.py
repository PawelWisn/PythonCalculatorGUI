from tkinter import *
from RPN import *


class App():
    def __init__(self):
        self.font = ""
        self.fontS = 11
        self.window = Tk()
        self.window.title("Calculator")
        self.window.config(width=600, height=800)
        self.window.resizable(False, False)
        self.buttons = []
        self.display = None
        self.displayVar = None
        self.buttonVars = []
        self.__generateButtons()
        self.__buildGUI()

    def __pushToDisplay(self, chr=None):
        this = self

        def x():
            input = this.displayVar.get()
            if len(input) >= 2 and isNumber(input[len(input) - 1]) and isNumber(chr):
                this.displayVar.set(input + chr)
            elif input[-1:] != '.' and chr != '.':
                this.displayVar.set(input + ' ' + chr)
            else:
                self.displayVar.set(input + chr)

        return x

    def __popFromDisplay(self):
        self.displayVar.set(self.displayVar.get()[:-1])

    def __evalDisplay(self):
        result = self.displayVar.get().strip()
        result = convertToRNP(result)
        result = evaluateRNP(result)
        self.displayVar.set(round(result, 6))

    def __generateButtons(self):
        butValues = ['7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', '*', '0', '(', ')', '/', '.', '^']
        for i in range(len(butValues)):
            updateFunc = self.__pushToDisplay(chr=butValues[i])
            self.buttons.append(Button(self.window, text=butValues[i], command=updateFunc, height=1, width=1))
        self.buttons.append(Button(self.window, text='D', command=self.__popFromDisplay, height=1, width=1))
        self.buttons.append(Button(self.window, text='=', command=self.__evalDisplay, height=1, width=1))

    def __buildGUI(self):
        self.displayVar = StringVar()
        self.display = Entry(self.window, textvariable=self.displayVar, justify=RIGHT)
        self.display.grid(row=0, column=0, columnspan=4)
        buttonsIter = iter(self.buttons)
        for x in range(5):
            for y in range(4):
                next(buttonsIter).grid(row=x + 1, column=y)

    def run(self):
        self.window.mainloop()


a = App()
a.run()
