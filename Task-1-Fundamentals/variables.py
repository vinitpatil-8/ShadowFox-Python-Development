# 1. Create a variable named pi and store the value 22/7 in it. Now check the data type of this variable.

pi = 22/7
print(type(pi)) # float


# 2. Create a variable called for and assign it a value 4. See what happens and find out the reason behind the behavior that you see.

# for = 4
# This line returns an error as 'for' is a keyword and it can't be used as an variable name

# 3. Store the principal amount, rate of interest, and time in different variables and then calculate the Simple Interest for 3 years.
# Formula: Simple Interest = P x R x T / 100

principal = int(input("Enter Principal Amount: "))
roi = int(input("Enter Rate of Interest: "))
time = 3

simple_interest = principal*roi*(time/100)
print(f"The simple interest for 3 years is {simple_interest}")