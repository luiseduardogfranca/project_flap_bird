# Define vertices and Edges of the object (A cube in this case)

bird_verticies = (
    (0.1, -0.1, -0.1),          # Vertice 1
    (0.1, 0.1, -0.1),           # Vertice 2
    (-0.1, 0.1, -0.1),           # Vertice 3
    (-0.1, -0.1, -0.1),         # Vertice 4    -> See the image in the directory to understand the positions
    (0.1, -0.1, 0.1),           # Vertice 5
    (0.1 , 0.1, 0.1),           # Vertice 6
    (-0.1, -0.1, 0.1),          # Vertice 7
    (-0.1, 0.1, 0.1),           # Vertice 8
)

bird_edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7),
)

bird_surfaces = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6),
)

bird_colors = (
    (1,0,0),
)