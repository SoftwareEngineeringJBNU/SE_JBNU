import winsound
import time
from datetime import datetime, timedelta

# 크리스마스 이스터에그
EASTEREGG_TRIGGER_CHRISTMAS = "1225" # 이스터에그가 발생하는 조건 값(숫자여야함)

# 음계와 박자를 정의합니다.
# 높은 음은 더 큰 숫자로, 음의 길이는 더 작은 숫자로 나타냅니다.
notes = {
    "C4": 261.63,
    "D4": 293.66,
    "E4": 329.63,
    "F4": 349.23,
    "G4": 392.00,
    "A4": 440.00,
    "B4": 493.88,
}

# 크리스마스 캐롤 'Jingle Bells'의 악보를 정의합니다.
jingle_bells = [
    ("E4", 250),
    ("E4", 250),
    ("E4", 500),
    # 미미미
    ("E4", 250),
    ("E4", 250),
    ("E4", 500),
    # 미미미
    ("E4", 250),
    ("G4", 250),
    ("C4", 250),
    ("D4", 250),
    ("E4", 1000),
    # 미솔도레미
    ("F4", 250),
    ("F4", 250),
    ("F4", 500),
    ("F4", 250),
    ("E4", 250),
    ("E4", 250),
    ("E4", 250),
    ("E4", 250),
    ("D4", 250),
    ("D4", 250),
    ("E4", 250),
    ("D4", 500),
    ("G4", 500),
    # 파파파 파미미미 미레레미레 솔
    ("E4", 250),
    ("E4", 250),
    ("E4", 500),
    # 미미미
    ("E4", 250),
    ("E4", 250),
    ("E4", 500),
    # 미미미
    ("E4", 250),
    ("G4", 250),
    ("C4", 250),
    ("D4", 250),
    ("E4", 750),
    #미솔도레미~
    ("F4", 250),
    ("F4", 250),
    ("F4", 250),
    ("F4", 250),
    ("F4", 250),
    ("E4", 250),
    ("E4", 250),
    ("E4", 250),
    ("G4", 250),
    ("G4", 250),
    ("F4", 250),
    ("D4", 250),
    ("C4", 1250)
]


def easterEgg_Chirstmas():
    height = 10
    for note, duration in jingle_bells:
        winsound.Beep(int(notes[note]), duration)
        time.sleep(duration/1000)

    for i in range(1, height + 1):
        space = height - i
        star = 2 * i - 1
        print(" " * space + "*" * star)
    bridge = height - 2
    print(" " * bridge + "|||")


# 새해 이스터애그

def easterEgg_NewYear():
    current_datetime = datetime.now()

    EASTEREGG_TRIGGER_NEWYEAR = (current_datetime + timedelta(days=365)).strftime("%Y")

    newyear_datetime = datetime(int(EASTEREGG_TRIGGER_NEWYEAR), 1, 1)

    remaining_time = newyear_datetime - current_datetime

    print(f"remaining days until 2024 : D-{remaining_time.days + 1}")