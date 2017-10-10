class VectorException(Exception):
    pass


def magnitudes3(components, scale=1.0):
    """takes flat list of components and returns 
    a list of corresponding magnitudes"""
    if len(components) % 3 != 0:
        raise VectorException("cannot map cleanly into vector magnitudes")

    magnitudes = []
    for i in xrange(0, len(components), 3):
        x = components[i] * scale
        y = components[i + 1] * scale
        z = components[i + 2] * scale
        magnitudes.append(x * x + y * y + z * z)

    return magnitudes
