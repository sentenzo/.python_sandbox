from dialog import Dialog
from enum import Enum, auto


class AppEnvironment(Enum):
    Windows = auto()
    Web = auto()
    Mac = auto()  # ++

def main():
    outer_parameters = {"AppEnvironment": AppEnvironment.Mac}

    dialog: Dialog = None
    questionText: str = "Would you like to take a break?"

    if outer_parameters["AppEnvironment"] == AppEnvironment.Windows:
        dialog = Dialog.WindowsDialog(questionText)
    elif outer_parameters["AppEnvironment"] == AppEnvironment.Web:
        dialog = Dialog.WebDialog(questionText)
    elif outer_parameters["AppEnvironment"] == AppEnvironment.Mac:  # ++
        dialog = Dialog.MacDialog(questionText)                     # ++
    else:
        raise AttributeError("The AppEnvironment parameter is undefined")

    dialog.render()


if __name__ == "__main__":
    main()