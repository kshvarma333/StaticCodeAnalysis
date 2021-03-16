"""
    The following code is about classifying the type of
    triangle based on the input and testing the function.
"""
def classify_triangle(side_a: int, side_b: int, side_c: int) -> str:
    """ Classifying the type of triangle depending on the values given to a,b,c """
    if (not(isinstance(side_a,int) or isinstance(side_b,int) or isinstance(side_c,int))
        or int(side_a) <= 0 or int(side_b) <= 0 or int(side_c) <= 0):
        raise ValueError("All values should be integers greater than zero")
    if side_a+side_b >= side_c and side_b+side_c >= side_a and side_c+side_a >= side_b:
        if side_a == side_b == side_c:
            return "Equilateral triangle"
        elif side_a == side_b or side_b == side_c or side_c == side_a:
            return "Isosceles triangle"
        elif (side_a**2 == side_b**2 + side_c**2
             or side_b**2 == side_c**2 + side_a**2 or side_c**2 == side_a**2 + side_b**2):
            return "Right angle triangle"
        else:
            return "Scalen triangle"
    else:
        return "Not a triangle"
        