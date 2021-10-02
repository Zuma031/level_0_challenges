def triangle():
    e = 9
    f = 10
    g = 11
    s = (e + f + g) / 2
    area = (s*(s-e)*(s-f)*(s-g)) ** 0.5
    print("Area of a triangle is %0.2f" %area)

triangle()