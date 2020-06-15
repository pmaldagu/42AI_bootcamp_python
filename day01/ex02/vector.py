class Vector:
    def __init__(self, data):
        if type(data) is list:
            self.values = data
            self.size = len(self.values)
        elif type(data) is int:
            self.values = [float(i) for i in range(int(data))]
            self.size = data
        elif type(data) is tuple and len(data) == 2:
                self.values = [float(i) for i in range(data[0], data[1])]
                self.size = len(self.values)
        else:
            print("Invalid input")

    def __add__(self, other):
		if (type(other) == (int or float)):
			return Vector(list([a + other for a in self.values]))
		elif (type(other) == Vector):
			return Vector([a + b for a, b in zip(self.values, other.values)])

    def __radd__(self, other):
    	return self + other

    def __sub__(self, other):
    	if (type(other) == (int or float)):
    		return Vector(list([a - other for a in self.values]))
    	elif (type(other) == Vector):
    		return Vector([a - b for a, b in zip(self.values, other.values)])

    def __rsub__(self, other):
    	if type(other) == (int or float):
    		return Vector([other - a for a in self.values])
    	elif (type(other) == Vector):
    		return Vector([b - a for a, b in zip(self.values, other.values)])

    def __truediv__(self, other):
    	if (type(other) == (int or float)) and other == 0:
    		return (print("Cannot divide by 0!"))
    	elif (type(other) == int or type(other) == float):
    		return Vector([a / other for a in self.values])
    	elif (type(other) == Vector):
			return (print("Cannot divide by a vector!"))

    def __rtruediv__(self, other):
    	return (print("Cannot divide by a vector!"))

    def __mul__(self, other):
    	if (type(other) == int or type(other) == float):
    		return Vector([a * other for a in self.values])
    	elif (type(other) == Vector):
    		return sum([b * a for a, b in zip(self.values, other.values)])

    def __rmul__(self, other):
    	return self * other

    def __repr__(self):
    	return f"(Vector {self.values})"

    def __str__(self):
    	return self.__repr__() 
