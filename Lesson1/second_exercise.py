a = float(input("Enter a = "))
b = float(input("Enter b = "))
c = float(input("Enter c = "))
left_part = (a ** 2 + b ** 2) / (3 * b - 4)
right_part = 4 * c ** 5 / 6
print(
    f"Integer part of result = {int(left_part / right_part)}\n"
    f"Remainder of the division = {left_part % right_part}")
