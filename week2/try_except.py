try:
    with open("names.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("File nahi mili, pehle create kar lo ya check karo filename.")
