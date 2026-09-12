# 1 - String Formatting
def format_number(val, fmt):
    return format(val, fmt)

result = format_number(145, "o")
print("1. Formatted Result:", result)
# Representation used: Octal (base-8) representation.

# 2 - Total amount of water in pond
radius = 84 # meters
area = 3.14 * (radius ** 2) # meter square
water = int(area * 1.4) # litres
print(f'The pond has {water} litres of water')

# 3 - Calculate Speed
distance = 490 # meters
time = 7 # minutes
speed = round(distance/(time*60))
print(f'The speed is {speed} meters per second')