#10.Write a Python program to create a list using for loop which consist. ['a','bb','ccc','dddd',....] that ends with 26 copies of the letter z.

lt=[]
for i in range (97,123):
    lt.append(chr(i) * (i - 96))
print(lt)