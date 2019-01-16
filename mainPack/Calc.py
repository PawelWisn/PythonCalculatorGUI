from tkinter import *
from RPN import *
import inspect


def lineno():
    return inspect.currentframe().f_back.f_lineno


class App():
    def __init__(self):
        self.font = "DejaVu Sans Mono"
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
            input = this.displayVar.get().strip()
            if len(input) >= 1 and isNum(input[len(input) - 1]) and isNum(chr):
                this.displayVar.set(input + chr)
            elif (len(input) == 1 and input[-1] == '-' and isNum(chr)) or (len(input) >= 3 and not isNum(input[-3]) and input[-1] == '-'):
                self.displayVar.set(input + chr)
            elif input[-1:] != '.' and chr != '.':
                this.displayVar.set(input + ' ' + chr)
            else:
                self.displayVar.set(input + chr)

        return x

    def __popFromDisplay(self):
        self.displayVar.set(self.displayVar.get()[:-1])

    def __evalDisplay(self):
        result = self.displayVar.get().strip()
        try:
            result = convertToRNP(result)
            result = evaluateRNP(result)
        except IndexError:
            print("Invalid input <line", lineno(), "> :", self.displayVar.get(), file=sys.stderr)
        except ZeroDivisionError:
            print("Division by zero <line", lineno(), "> :", self.displayVar.get(), file=sys.stderr)
        try:
            self.displayVar.set(round(float(result), 6))
        except ValueError:
            print("Invalid input <line", lineno(), "> :", self.displayVar.get(), file=sys.stderr)

    def __generateButtons(self):
        butValues = ['7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', '*', '0', '(', ')', '/', '.', '^']
        for i in range(len(butValues)):
            updateFunc = self.__pushToDisplay(chr=butValues[i])
            self.buttons.append(Button(self.window, text=butValues[i], command=updateFunc, height=1, width=1))
        self.buttons.append(Button(self.window, text='D', command=self.__popFromDisplay, height=1, width=1))
        self.buttons.append(Button(self.window, text='=', command=self.__evalDisplay, height=1, width=1))
        for button in self.buttons:
            button.config(font=(self.font, self.fontS))

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
