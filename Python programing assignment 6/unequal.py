#2.Write a python program to input three unequal no and dsiplay the greatest and the smallest number

def find_greatest_smallest ():
  list=[]
  count =0 
  while count <3:
   num = int(input(f'Enter numbers {count}: '))
   if num not in list:
    list.append(num)
    count+=1
  print("Greatest number:",max(list))
  print("Smallest number:",min(list))

find_greatest_smallest()