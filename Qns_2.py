# Define a function to determine the type of triangle based on its angles
def triangle_type(angle1, angle2, angle3):
    if angle1 == angle2 == angle3:
        return "equilateral"  # If all angles are equal, it's an equilateral triangle
    elif angle1 == angle2 or angle1 == angle3 or angle2 == angle3:
        return "isosceles"    # If at least two angles are equal, it's an isosceles triangle
    else:
        return "simple"       # Otherwise, it's a simple (scalene) triangle

try:
    # Prompt the user to input the three angles of the triangle as floating-point numbers
    angle1 = float(input("Enter the first angle of the triangle: "))
    angle2 = float(input("Enter the second angle of the triangle: "))
    angle3 = float(input("Enter the third angle of the triangle: "))

    # Check if the sum of angles is 180 degrees (valid for a triangle)
    if angle1 + angle2 + angle3 == 180:
        # Call the 'triangle_type' function to determine the type of triangle
        triangle = triangle_type(angle1, angle2, angle3)
        # Print the result
        print(f"The triangle is {triangle}.")
    else:
        # If the sum of angles is not 180 degrees, it's not a valid triangle
        print("The angles do not form a valid triangle (sum of angles should be 180 degrees).")
except ValueError:
    # Handle the case where the user enters invalid input (non-numeric angles)
    print("Invalid input. Please enter valid numeric angles.")
