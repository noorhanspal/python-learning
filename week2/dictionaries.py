student = {"name": "Noor", "roll": 12, "marks": [90, 85, 75]}
print(student["name"])
student["marks"].append(95)   # naye marks add kiye
student["year"] = 4           # ek nayi key add
print(student)
for k, v in student.items():
    print(k, "=>", v)
    # find average marks of each student using a loop
marks = {
    1: [90, 80, 70],
    2: [75, 85, 95],
    3: [88, 77, 66],
    4: [95, 85, 75],
    5: [70, 80, 90]
}

for roll, score_list in marks.items():
    avg = sum(score_list) / len(score_list)
    print("Roll", roll, "=> Average Marks:", avg)

