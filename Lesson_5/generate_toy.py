from enum import Enum
import random


class NewYearToys(Enum):
    toy_1 = "Red ball"
    toy_2 = "Purple angel"
    toy_3 = "Candle"
    toy_4 = "Teddy bear"
    toy_5 = "Transformer"
    toy_6 = "Car"


def get_random_toy() -> bool:
    toy = random.choice(list(NewYearToys))
    print(toy.value)
    return 0
