from enum import Enum
import random


class NewYearToys(Enum):
    toy_1 = "Ball"
    toy_2 = "Angel"
    toy_3 = "Candle"
    toy_4 = "Teddy bear"
    toy_5 = "Transformer"
    toy_6 = "Car"


class Color(Enum):
    color_1 = "Red"
    color_2 = "Blue"
    color_3 = "Yellow"
    color_4 = "Green"
    color_5 = "Purple"


def get_random_toy() -> int:
    toy = random.choice(list(NewYearToys))
    color = random.choice(list(Color))
    print(f"{color.value} {toy.value}")
    return 0
