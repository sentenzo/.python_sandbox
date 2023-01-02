from alarm_signal import AlarmSignal
from alarm_decorator import LightsOn

def main():
    alarm = AlarmSignal("Rick Astley - Never Gonna Give You Up.mp3")
    alarm = LightsOn(alarm)
    alarm.raise_alarm()

if __name__ == "__main__":
    main()
# >> [Outer World]: Lights - ON
# >> [Outer World]: Play - "Never Gonna Give You Up.mp3"