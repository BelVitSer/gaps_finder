from gap_finder.coordinate import Coordinate
from gap_finder.generation import (
    generate_plane_by_three_coordinates,
    build_surface,
    get_all_coordinates_triplets,
    PLOT,
    AXES
)

"""
Песочница для каких-либо quick-check-пук-штук
"""

DOTS_COUNT = 2

# GapFinderTestCase().run()
cord1 = Coordinate(x=0, y=0, z=1)
cord2 = Coordinate(x=0, y=1, z=1)
cord3 = Coordinate(x=2, y=0, z=0)

cords = [cord1, cord2, cord3]
x, y, z = generate_plane_by_three_coordinates(*cords)

a = get_all_coordinates_triplets(z)

print(a)

print(z[0][0])
print(z[0][1])
print(z[2][0])
build_surface(AXES, x, y, z)
PLOT.show()
