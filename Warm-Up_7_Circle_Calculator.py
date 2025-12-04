"""
Filename: Warm-Up_7_Circle_Calculator.py
Author: <Carcamo, Fredys>
Created: <12/04/2025>
Instructor: Holtslander
"""

def circle_calculator():
    """
    Calculates the area and circumference of a circle.
    Asks the user to enter the radius of the circle.
    Uses the formulas
    A = pi*r**2
    C = 2*pi*r
    :return: None
    """
    ### YOUR CODE GOES HERE ###
    a = input("Enter the radius of your circle:")
    a = float(a)
    Area = 3.14 * a **2
    Circumference = 2 * 3.14 * a

    print(f"The area of your radius is {Area}, and your circuference is {Circumference}")
    


### YOU SHOULD NOT NEED TO CHANGE ANYTHING HERE ###
if __name__ == '__main__':
    circle_calculator()