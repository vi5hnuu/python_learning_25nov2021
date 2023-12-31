def pascal_triangle(n):
    row=[1]
    z=[0]
    for x in range(n):
        print(row)
        row=[i+r for i,r in zip(row+z,z+row)]

pascal_triangle(5)