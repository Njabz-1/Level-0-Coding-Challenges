def Area_of_triangle(a,b,c):
    sp = (a+b+c) / 2
    area = (sp * (sp - a) * (sp - b) * (sp - c)) ** 0.5
    return area

Area_of_triangle(3,4,5)