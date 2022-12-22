from button import *
from textBox import *
from abc import ABC, abstractmethod

from enum import Enum, auto


class BTN_TYPE(Enum):
    YES = auto()
    NO = auto()


class Dialog(ABC):
    def __init__(self, questionText: str):
        self.tbQuestion = self.createTextBox(questionText)
        self.btnYes = self.createButton(BTN_TYPE.YES)
        self.btnNo = self.createButton(BTN_TYPE.NO)

    @abstractmethod
    def createButton(self, btn_type: BTN_TYPE) -> Button: pass

    @abstractmethod
    def createTextBox(self, text: str) -> TextBox: pass

    def render(self):
        self.tbQuestion.render()
        self.btnYes.render()
        self.btnNo.render()


class WindowsDialog(Dialog):
    def createButton(self, btn_type: BTN_TYPE) -> Button:
        if btn_type == BTN_TYPE.YES:
            return WindowsButton("Yes", lambda: print("\"Yes\" button was pressed"))
        elif btn_type == BTN_TYPE.NO:
            return WindowsButton("No", lambda: print("\"No\" button was pressed"))

    def createTextBox(self, text: str) -> TextBox:
        return WindowsTextBox(text)


class WebDialog(Dialog):
    def createButton(self, btn_type: BTN_TYPE) -> Button:
        if btn_type == BTN_TYPE.YES:
            return WebButton("Yes", lambda: print("\"Yes\" button was pressed"))
        elif btn_type == BTN_TYPE.NO:
            return WebButton("No", lambda: print("\"No\" button was pressed"))

    def createTextBox(self, text: str) -> TextBox:
        return WebTextBox(text)


class MacDialog(Dialog):                                                          # ++
    def createButton(self, btn_type: BTN_TYPE) -> Button:                         # ++
        if btn_type == BTN_TYPE.YES:                                              # ++
            return MacButton("Yes", lambda: print("\"Yes\" button was pressed"))  # ++
        elif btn_type == BTN_TYPE.NO:                                             # ++
            return MacButton("No", lambda: print("\"No\" button was pressed"))    # ++

    def createTextBox(self, text: str) -> TextBox:                                # ++
        return MacTextBox(text)                                                   # ++
