#Write a python program to compute the result when two numbers and one operator is given by user

def main():
    print('Simple Calculation')
    print('1.Addition')
    print('2.Subtraction')
    print('3.Multiplication')
    print('4.Division')
    
    choice=input('Enter your choice(1/2/3/4):')
    num1 = float(input('Enter 1st number:'))
    num2 = float(input('Enter 2nd number:'))
    if choice =='1':
        print(num1,'+',num2,'=',num1+num2)
    elif choice =='2':     
        print(num1,'-',num2,'=',num1-num2)
    elif choice == '3':    
        print(num1,'*',num2,'=',num1*num2)
    elif choice == '4':
     if num2!=0:     
        print(num1,'/',num2,'=',num1/num2) 
     else:
        print('Error!Division by zero not possible.')
    else:
        print('Invalid choice')

if __name__=='__main__':        
 main()                