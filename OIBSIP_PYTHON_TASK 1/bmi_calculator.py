# -----------------------------------------
# BMI CALCULATOR (ACCEPT HEIGHT IN FEET + INCHES)
# -----------------------------------------

def get_float_input(message):
    """
    Safely gets a float input from the user.
    Prevents errors from invalid or negative numbers.
    """
    while True:
        try:
            value = float(input(message))
            if value < 0:
                print("Value must be positive. Please try again.\n")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.\n")


print("----------- BMI CALCULATOR -----------\n")

# Get weight
weight = get_float_input("Enter your weight in kilograms: ")

# Get height in feet + inches
feet = get_float_input("Enter height (feet): ")
inches = get_float_input("Enter remaining inches: ")

# Convert feet + inches → meters
total_inches = (feet * 12) + inches
height_meters = total_inches * 0.0254    # 1 inch = 0.0254 meters

# Avoid division by zero
if height_meters == 0:
    print("\nError: Height cannot be zero.")
    exit()

# Calculate BMI
bmi = weight / (height_meters ** 2)

# Output
print("\nYour height in meters:", round(height_meters, 3))
print("Your BMI is:", round(bmi, 2))

# Classify BMI
if bmi < 18.5:
    category = "Underweight"
elif bmi < 24.9:
    category = "Normal weight"
elif bmi < 29.9:
    category = "Overweight"
else:
    category = "Obese"

print("Category:", category)
print("-----------------------------------------")
