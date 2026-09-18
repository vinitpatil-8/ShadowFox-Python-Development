height = float(input("Enter height in meters:"))
weight = float(input("Enter weight in kilograms:"))
bmi = weight/(height*height)

if bmi >= 30:
    print("Obesity")
elif bmi <= 29 and bmi > 25:
    print("Overweight") 
elif bmi <=25 and bmi >= 18.5:
    print("Normal")
else:
    print("Underweight")