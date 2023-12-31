import math
pi=3.14
sin_table={ang:math.sin(ang*pi/180) for ang in range(0,360,90)}
cos_table={ang:math.cos(ang*pi/180) for ang in range(0,360,90)}
tan_table={ang:math.tan(ang*pi/180) for ang in range(0,360,90)}
print(sin_table)
print(cos_table)
print(tan_table)
maxsin=max((math.sin(ang*pi/180)) for ang in range(0,360,90))
maxcos=max((math.cos(ang*pi/180)) for ang in range(0,360,90))
print(maxsin)
print(maxcos)