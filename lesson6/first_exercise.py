with open("text.txt", "w") as f:
    f.write("Hello World")
with open("text.txt", "r") as f:
    line = f.readline()
print(line)
