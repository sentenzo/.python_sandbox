from abc import ABC, abstractmethod
from outer_world import OuterWorld as out

class Alarmable(ABC):
    @abstractmethod
    def raise_alarm(self) -> None: pass

class AlarmSignal(Alarmable):
    def __init__(self, trackName: str) -> None:
        super().__init__()
        self.trackName = trackName

    def raise_alarm(self) -> None:
        out.do(f"Play - \"{self.trackName}\"")
        return