from alarm_signal import Alarmable, AlarmSignal
from outer_world import OuterWorld as out

class AlarmDecorator(Alarmable):
    def __init__(self, alarm: Alarmable) -> None:
        super().__init__()
        self.alarm = alarm

    def raise_alarm(self) -> None:
        return self.alarm.raise_alarm()

class LightsOn(AlarmDecorator):
    def raise_alarm(self) -> None:
        out.do("Lights - ON")
        super().raise_alarm()
