import polygon_triangulate as pt
import numpy as np
#this uses a greedy algorithm to tricolor the triangulation
#since a triangulation is by definition chordal and greedy algorithms are able to find the optimal coloring on chordal graphs
#i am guessing this would work
def tricolorize(n, x, y):
    triangles = pt.polygon_triangulate ( n, x, y )
    vertices = {}
    #goes in reverse order of the orden in which the triangles were found i.e. from the inside out
    for  j in reversed(range(len(triangles))):
        t= triangles[j]
        for i in range(0,3):
            p = t[i]
            if not (p in vertices.keys()):
                #feel kind of proud of this, using mod 3 to get all 3 points regardless of which we are looking at
                if not((vertices.get(t[(i-1)%3])==0) or (vertices.get(t[(i+1)%3])==0)):
                    vertices[p]=0
                elif not((vertices.get(t[(i-1)%3])==1) or (vertices.get(t[(i+1)%3])==1)):
                    vertices[p]=1
                else:
                    vertices[p]=2

    return vertices
#alternate funtion, used to tricolor the triangulation than list out the colors for each triangle
#used to test code output
def coloredtriangles(n, x, y):
    triangles = pt.polygon_triangulate ( n, x, y )
    vertices =  tricolorize(n, x, y)
    l1= []
    for t in triangles:
        l2=[]    
        for p in t:
            l2.append(vertices.get(p))
        l1.append(l2) 
    return l1
#find the minimum amount of guards using the coloration. pretty simple
def minguards(n, x, y):
    vertices=tricolorize(n,x,y)
    colors = {0:0, 1:0, 2:0}
    for k in vertices:
        colors[vertices[k]]=colors[vertices[k]]+1
    return min(list(colors.values()))

    


