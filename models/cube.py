
points = [
    [ 1, -35, -35, -35 ],
    [ 2, -35, 35, -35 ],
    [ 3, 35, 35, -35 ],
    [ 4, 35, -35, -35 ],
    [ 5, -35, -35, 35 ],
    [ 6, -35, 35, 35 ],
    [ 7, 35, 35, 35 ],
    [ 8, 35, -35, 35 ]
]

edges = [
    [ 1, 2 ],
    [ 2, 3 ],
    [ 3, 4 ],
    [ 4, 1 ],
    [ 1, 5 ],
    [ 2, 6 ],
    [ 3, 7 ],
    [ 4, 8 ],
    [ 5, 6 ],
    [ 6, 7 ],
    [ 7, 8 ],
    [ 8, 5 ]
]
    
triangles = [
    [ 1, 2, 3 ],
    [ 1, 3, 4 ],    
    [ 1, 2, 5 ],
    [ 2, 5, 6 ],
    [ 2, 3, 6 ],
    [ 3, 6, 7 ],    
    [ 3, 4, 8 ],
    [ 3, 7, 8 ],
    [ 6, 7, 8 ],
    [ 5, 6, 8 ],
    [ 1, 4, 5 ],
    [ 4, 5, 8 ]
]

n_triangles = [
    [[10, 10, 10], [10, 20, 10], [20, 10, 10]],
    [[10, 10, 10], [10, 20, 10], [30, 20, 10]],
    [[10, 10, 10], [10, 30, 30], [20, 10, 10]],        
]
