# 1. Write a program to determine the BMI Category based on user input.

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

# 2. Write a program to determine which country a city belongs to.
country_cities = {
    "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth"],
    "UAE": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
    "India": ["Mumbai", "Bangalore", "Chennai", "Delhi"]
}

user_input = input("Enter a city name: ").strip()

found = False

for country, cities in country_cities.items():
    if user_input.lower() in [city.lower() for city in cities]:
        exact_city_name = [c for c in cities if c.lower() == user_input.lower()][0]
        print(f'"{exact_city_name} is in {country}"')
        found = True
        break

# 3. Write a program to check if two cities belong to the same country
def get_country(city_name):
    for country, cities in country_cities.items():
        if city_name.lower() in [c.lower() for c in cities]:
            return country
    return None

city1 = input("Enter the first city: ").strip()
city2 = input("Enter the second city: ").strip()

country1 = get_country(city1)
country2 = get_country(city2)

if country1 == country2:
    print(f'"Both cities are in {country1}"')
else:
    print("They don't belong to the same country")