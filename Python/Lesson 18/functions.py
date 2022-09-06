"""
"""


def quadratic_equation(a, b, c):
    if a == 0:
        raise ValueError
    d = (b**2) - (4 * a * c)
    if d == 0:
        return float(-b-(d)**(1/2))/(2*a)
    elif d > 0:
        return float(-b+(d)**(1/2))/(2*a), float(-b-(d)**(1/2))/(2*a)
    else:
        return None

if __name__ == "__main__":
    print(quadratic_equation(2,1,1)) # None   
    print(quadratic_equation(2,1,-1)) # (0.5, -1.0)
    print(quadratic_equation(1,-4, 4)) # 2.0
