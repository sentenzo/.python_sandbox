from uiFactory import UiFactory

class Ui:
    def __init__(self, uiFactory: UiFactory) -> None:
        self.uiFactory = uiFactory
        self.lQuestion = uiFactory.createLabel(
            "Would you like to take a break?")
        self.btnYes = uiFactory.createButton(
            "Yes", lambda: print("\"Yes\" button was pressed"))
        self.btnNo = uiFactory.createButton(
            "No", lambda: print("\"No\" button was pressed"))

    def render(self):
        self.lQuestion.render()
        self.btnYes.render()
        self.btnNo.render()
