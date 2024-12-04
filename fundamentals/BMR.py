age = int(input("Enter the age: "))

height = int(input("Enter the height in cm: "))

weight = int(input("Enter the weight in kg: "))

gender = input("Enter the gender (male or female): ").lower()  

if gender == "male":
    
    BMR = 10 * weight + 6.25 * height - 5 * age + 5
    
elif gender == "female":
    
    BMR = 10 * weight + 6.25 * height - 5 * age - 161
    
else:
    
    print("Invalid gender")
    
print(f"Your BMR is: {BMR}")

   
    
activity_level = int(input(
        
        """Select activity level:
        
        1. Sedentary (little or no exercise)
        
        2. Lightly active (light exercise or sports 1-3 days/week)
        
        3. Moderately active (moderate exercise or sports 3-5 days/week)
        
        4. Very active (hard exercise or sports 6-7 days a week)
        
        5. Extra active (very hard exercise, physical job, or training twice a day)
        
        Enter the number corresponding to your activity level: """
    ))

   
if activity_level == 1:
        
        calorie = BMR * 1.2
        
elif activity_level == 2:
        
        calorie = BMR * 1.375
        
elif activity_level == 3:
        
        calorie = BMR * 1.55
        
elif activity_level == 4:
        
        calorie = BMR * 1.725
        
elif activity_level == 5:
        
        calorie = BMR * 1.9
        
else:
        
        print("Invalid activity level")

  

print(f"Total number of calories you need to maintain your weight is {calorie}")

target_weight=int(input("Enter the  weight to reduce  in kg: "))


duration=int(input("Enter the duration in weeks: "))

calorie_deficit=target_weight*7700

days=duration*7

daily_calorie_deficit= calorie_deficit/days

print(f"Calorie deficit per day is {daily_calorie_deficit}")
