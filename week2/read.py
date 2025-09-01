# read_example.py
with open("names.txt", "r", encoding="utf-8") as f:
    data = f.read()
print("File content:")
print(data)
# read_lines_
with open("names.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
print("Raw lines:", lines)                   # contains '\n'
names = [line.strip() for line in lines]
print("Clean names:", names)
print("Count:", len(names))
# append_example.py
with open("names.txt", "a", encoding="utf-8") as f:
    f.write("Sana\n")
print("Appended Sana to names.txt")
