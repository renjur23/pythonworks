# # # name="renju"


# # # place="angamaly"


# # # print(f"i am {name} from {place}")


# # # # swap case
# # # num1=100

# # # num2=200

# # # num1,num2=num2,num1

# # # print(num1,num2)


# # # # swap method

# # # num3=100

# # # num4=200

# # # print(f"numbers before swap num3 is {num3},num4 is {num4}")

# # # num4=num3 +num4

# # # num3=num4 -num3

# # # num4=num4 -num3

# # # print(f"numbers after swap num3 is {num3},num4 is {num4}")


# # # convertion

# # # task 1 : To convert Celsius to Fahrenheit, we use the C to F formula which is °F = (9/5) °C+32.

# # c=int(input("enter the temperature in celsius : "))


# # f=(9/5)*c+32

# # print(f"the temperature in fahrenheit is {f}")

# # # task 2 : To convert Fahrenheit to Celsius, we use the F to C formula which is °C = (5/9) (°F – 32).

# # f=int(input("enter the temperature in fahrenheit : "))


# # c=(5/9)*(f-32)

# # print(f"the temperature in celsius is {c}")

# # # task 3: to convert cm into meter

# # cm=int(input("enter the cm : "))

# # m=cm/100

# # print(f"the meter is {m}")

# # # task 4: to convert meter into cm

# # m=int(input("enter the meter : "))

# # cm=m*100

# # print(f"the cm is {cm}")


# # # task 5 : to convert inch to cm

# # inch=int(input("enter the inch : "))

# # cm=inch*2.54

# # print(f"the cm is {cm}")


# # bmi calculator

weight=int(input("enter the weight  in kg: "))

height=int(input("enter the height in cm: "))

height_in_meter=height/100

bmi=weight/(height_in_meter**2)

bmi=round(bmi,1)

print(f"the bmi is {bmi}")

if bmi<19:
    
    print("under weight")
    
elif 19<=bmi<24:
    
    print("normal weight")
    
elif 24<=bmi<29:
    
    print("over weight")
    
elif 29<=bmi<34:
    
    print("obese")
    
else:
    
    print("extreme obese")



# # even  num

# # num=int(input("enter the number : "))

# # rem=num%2

# # print(rem==0)


# # # odd num

# # num=int(input("enter the number : "))

# # rem=num%2

# # print(rem!=0)


# # # last digit

# # num=int(input("enter the number : "))

# # last_digit=num%10

# # print(last_digit)

# # last digit  even

# num=int(input("enter the number : "))

# last_digit=num%10

# print(last_digit%2==0)


# # logical operator

# num1=int(input("enter the number : "))

# is_positive=num1>0 and num1!=0

# print(f"the number is  {is_positive}is_positive ")


# positive or negative

# num2=int(input("enter the number : "))

# if num2 > 0:
#     print(f" {num2} is positive")
# else:
#     print(f" {num2} is negative")

# vote age

# age=int(input("enter the age : "))

# if age >= 18:
#     print("you can vote")
# else:
#     print("you can not vote")

# odd or even

# num=int(input("enter the number : "))

# if num%2==0:
    
#     print(f"{num} is even")
    
# else:
    
#     print(f"{num} is odd")


# divisible by 4

# num=int(input("enter the number : "))

# if num%4==0:
    
#     print(f"{num} is divisible by 4")
    
# else:
    
#     print(f"{num} is not divisible by 4")

# if else

num=int(input("enter the number : "))

if num%3==0:
    
    print("fizz")
    
elif num%5==0:
    
    print("buzz")
    
elif num%15==0:
    
    print("fizzbuzz")
    
else:
    
    print("invalid")