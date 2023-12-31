class Vector:
    """Represent a vector in multidimensional space."""
    
    def __init__(self, d) -> None:
        """Create a d-dimensional vector of zeros."""
        self._coords = [0] * d
    
    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)
    
    def __getitem__(self, j):
        """Return jth coordinate of the vector"""
        return self._coords[j]
    
    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value."""
        self._coords[j] = val

    def __add__(self, other):
        """Return the sum of two vectors"""
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self)) # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    
    def __eq__(self, other: object) -> bool:
        """Return true if vector has same coordinates as other."""
        return self._coords == other._coords
    
    def __ne__(self, other: object) -> bool:
        """Return True if vector differs from other."""
        return not self == other
    
    def __str__(self) -> str:
        """Produce string representation of vector."""
        return '<' + str(self._coords)[1:-1] + '>'