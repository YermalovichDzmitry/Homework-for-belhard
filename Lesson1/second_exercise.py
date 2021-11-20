a = float(input("Enter a = "))
b = float(input("Enter b = "))
c = float(input("Enter c = "))
right_part = (a ** 2 + b ** 2) / (3 * b - 4)
left_part = 4 * c ** 5 / 6
print(
    f"Integer part of number = {int(right_part / left_part)}\n"
    f"Remainder of the division = {int(right_part % left_part)}")
