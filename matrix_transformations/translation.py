import numpy as np

def translate(verticies, tx, ty, tz): # tx, ty, tz translation factors

    arr = np.array([tx,ty,tz])
    aux = []

    for vertex in verticies:
        aux.append(np.array(vertex) + arr)

    return aux