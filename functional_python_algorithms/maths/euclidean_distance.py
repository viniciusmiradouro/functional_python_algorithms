Point1D = float
Point2D = tuple[float, float]
Point3D = tuple[float, float, float]


def euclidean_distance_1d(p: Point1D, q: Point1D) -> float:
    return abs(p - q)


def euclidean_distance_2d(p: Point2D, q: Point2D) -> float:
    return ((p[0] - q[0])**2 + (p[1] - q[1])**2)**0.5


def euclidean_distance_3d(p: Point3D, q: Point3D) -> float:
    return ((p[0] - q[0])**2 + (p[1] - q[1])**2 + (p[2] - q[2])**2)**0.5
