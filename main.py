import numpy as np
import tricolor
n = 10
x = np.array ( [ 8.0,  7.0,  6.0,  5.0,  4.0,  3.0,  2.0,  1.0,  0.0,  4.0 ] )
y = np.array ( [ 0.0, 10.0,  0.0, 10.0,  0.0, 10.0,  0.0, 10.0,  0.0, -2.0 ] )
#color the vertices
print(tricolor.tricolorize(n,x,y))
#print all the triangles with their vertices colored (makes it easy to check if code worked)
print(tricolor.coloredtriangles(n,x,y))
#using the tricolor algorithm to find lowest number of guards needed 
print(tricolor.minguards(n, x, y))

#using the i18 polygon
x = np.array ( [0.0,  10.0,  12.0,  20.0,  13.0,  10.0,  12.0,  14.0,  8.0,  6.0,10.0,7.0, 0.0, 1.0,3.0,5.0, -2.0,5.0])
y = np.array ( [ 0.0, 7.0,3.0,8.0,17.0,12.0,14.0,9.0,10.0,14.0,15.0,18.0,16.0,13.0,15.0,8.0,9.0,5.0])
n = 18
#color the vertices
print(tricolor.tricolorize(n,x,y))
#print all the triangles with their vertices colored (makes it easy to check if code worked)
print(tricolor.coloredtriangles(n,x,y))
#using the tricolor algorithm to find lowest number of guards needed 
print(tricolor.minguards(n, x, y))
