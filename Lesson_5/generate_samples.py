from pathlib import Path
from random import randint


def generate_sample(directory: str) -> None:
    Path(directory).mkdir(exist_ok=True)

    for i in range(10):
        Path(f'{directory}\\'
             f'{randint(2020, 2022)}-'
             f'{randint(1, 12)}-'
             f'{randint(1, 31)}.txt'
             ).touch()
