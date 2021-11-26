import math

first_line_of_legs = "16 15 7 12"
second_line_of_legs = "30 20 24 5"
first_legs = first_line_of_legs.split()
second_legs = second_line_of_legs.split()

first_second_legs = [(int(first_legs[i]), int(second_legs[i])) for i in range(len(first_legs))]


def output(tuple_legs):
    for index, item in enumerate(tuple_legs, 1):
        a = item[0]
        b = item[1]
        S = a * b * 0.5
        c = math.sqrt(a ** 2 + b ** 2)
        print(
            f"Triangle {index} with legs {a} and {b} has area S = {S} and hypotenuse c = {c}")
    return 0


output(first_second_legs)

print(100 * "=")
third_line_of_legs = "16 30 15 20 7 24 12 5"
third_legs = third_line_of_legs.split()
tuple_third_legs = [(int(third_legs[i - 2]), int(third_legs[i - 1])) for i in range(2, len(third_legs) + 2, 2)]
output(tuple_third_legs)
