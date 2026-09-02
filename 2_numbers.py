# Python Numbers Tasks

# 1. Format 145 as an octal number
def format_number(number, representation):
    return format(number, representation)

result = format_number(145, 'o')
print("Formatted result:", result)

# Output:
# Formatted result: 221


# 2. Area of a circular pond
radius = 84
pi = 3.14
area = pi * radius ** 2
print("Area of the pond:", area)

# Output:
# Area of the pond: 22166.4

# Bonus: Calculate total water in the pond
water_per_square_meter = 1.4
total_water = area * water_per_square_meter
print("Total water in the pond:", int(total_water))

# Output:
# Total water in the pond: 31032


# 3. Calculate speed in meters per second
distance = 490
time_minutes = 7
time_seconds = time_minutes * 60
speed = distance / time_seconds
print("Speed:", int(speed), "meter/second")

# Output:
# Speed: 1 meter/second
