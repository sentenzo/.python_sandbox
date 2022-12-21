from uiFactory import UiFactory
from ui import Ui
from enum import Enum, auto

class AppEnvironment(Enum):
    Windows = auto()
    Web = auto()
    Mac = auto()

def defineAppEnvironment() -> AppEnvironment:
    return AppEnvironment.Mac

def getUiFactory() -> UiFactory:
    appEnvironment = defineAppEnvironment()
    return {
        AppEnvironment.Windows: UiFactory.UiFactory_Windows,
        AppEnvironment.Web: UiFactory.UiFactory_Web,
        AppEnvironment.Mac: UiFactory.UiFactory_Mac,
    }[appEnvironment]()

def main():
    ui: Ui.Ui = Ui(getUiFactory())
    ui.render()

if __name__ == "__main__":
    main()