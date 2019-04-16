from brain import think
import enum

class Colors(enum.Enum):
    Red = 1
    Orange = 2
    Yellow = 3
    Green = 4
    Cyan = 5
    Blue = 6
    Purple = 7
    White = 8
    Black = 9

def colorDecision(color):
    b = think()

    r = b.predict([color])

    return Colors(r[0]).name
