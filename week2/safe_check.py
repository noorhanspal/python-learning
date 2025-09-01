# safe_check.py
import os

if os.path.exists("names.txt"):
    with open("names.txt", "r", encoding="utf-8") as f:
        print("notes.txt content:")
        print(f.read())
else:
    print("names.txt not found — creating it now.")
    with open("names.txt", "w", encoding="utf-8") as f:
        f.write("This is a new file.\n")
    print("namess.txt created.")
