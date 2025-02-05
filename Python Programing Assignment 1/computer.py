import statistics
def calculate(marks):
    mean= sum(marks) / len(marks)
    median=statistics.median(marks)
    mode=statistics.mode(marks)

    return mean, median, mode

n = int(input("Length: "))

marks = []

for i in range(n):
    mark = float(input("Enter the marks of student: "))
    marks.append(mark)

mean, median, mode = calculate(marks)

print("mean: ", mean)
print("median: ", median)
print("mode: ", mode)
