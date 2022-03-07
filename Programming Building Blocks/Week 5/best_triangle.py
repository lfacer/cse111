def compute_triangle_area(base, height):
    """
    Computes the area of a triangle
    """
    return base * height / 2

base = float(input("Please enter triangle base: "))

result = compute_triangle_area(base,6)
print(result)

