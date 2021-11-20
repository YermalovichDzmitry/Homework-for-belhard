# first_line = input("Enter first line = ")
# second_line = input("Enter second line = ")
first_line = "Hello"
second_line = "Hi, Hello world"
print(f"You have entered \"{first_line}\" and \"{second_line}\".")
print(f"Their length is {len(first_line)} and {len(second_line)} ")
print(f"First symbol in first line = {first_line[0]}")
print(f"Last symbol in second line = {second_line[-1]}")
print(f"Is \"{first_line}\" equal to \"{second_line}\" : {first_line == second_line}")
print(f"Does \"{second_line}\" contain  \"{first_line}\" : {first_line in second_line}")
print(f"Does \"{first_line}\" contain  \"{second_line}\" : {second_line in first_line}"