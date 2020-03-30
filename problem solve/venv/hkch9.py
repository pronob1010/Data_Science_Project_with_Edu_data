student_marks = {}
for i in range(int(input())):
    n = input().split()
    scores = list(map(float, n[1:]))
    student_marks[n[0]] = sum(scores)/float(len(scores))

print("%.2f"%student_marks[input()])