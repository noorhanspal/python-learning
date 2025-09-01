marks=[2,8,6,7]
print(marks)
print(type(marks))
print(marks[3])
marks[2]=7
print(marks)
marks.append(60)
marks.remove(2)
print(marks)
#average
average= sum(marks)/len(marks)
print("average marks: ",average)