# write_list_and_read.py
tasks = ["Buy milk", "Study Python", "Call mom"]
with open("todo.txt", "w", encoding="utf-8") as f:
    for t in tasks:
        f.write(t + "\n")
print("Wrote tasks to todo.txt")

with open("todo.txt", "r", encoding="utf-8") as f:
    tasks2 = [line.strip() for line in f]
print("Read back tasks:", tasks2)
