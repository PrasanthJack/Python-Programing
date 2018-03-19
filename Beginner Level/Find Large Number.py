num1=(input("enter the 1 num: "))
 num2=(input("enter the 2 num: "))
 num3=(input("enter the 3 num: "))
 if(num1>num2 and num1>num3):
    largest=num1
 elif(num2>num1 and num2>num3):
    largest=num2
 else:
    largest=num3
    print("the largest number is", largest)
