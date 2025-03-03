#10.Write a Python function to find the sum of all numbers between 100 and 500 which are divisible by 2.

lt = []
for i in range(100,501):
    if i%2==0:
        lt.append(i)
print(sum(lt))
