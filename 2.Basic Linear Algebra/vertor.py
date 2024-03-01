class Vector:
    def __init__(self, *lst): # *lst - 여러 개의 값을 튜플로 받음(*이 빠지면 값 하나만 받음)
        self.data = lst

    def __str__(self): # print
        return f"Vector{self.data}"

    def add(self, other): # a.add(b)
        tmp = [a+b for a, b in zip(self.data, other.data)]
        # tmp = [3, 5, 7]
        # Vector(tmp) -> Vector([3,5,7])
        # Vector(*tmp) = Vector(3,5,7)
        return Vector(*tmp)

    def __add__(self, other): # a + b
        tmp = [a+b for a, b in zip(self.data, other.data)]
        return Vector(*tmp)

    def __sub__(self, other):
        return Vector(*[a-b for a, b in zip(self.data, other.data)])

    def mul(self, other): # a.mul(4)
        return Vector(*[a*other for a in self.data])

    def __mul__(self, other): # a * 4
        if type(other) == Vector: # dot product
            return sum(a*b for a, b in zip(self.data, other.data))
        else:
            return Vector(*[a * other for a in self.data])

    def __rmul__(self, other): # 4 * a
        return Vector(*[a * other for a in self.data])



a = Vector(1,2,3)
b = Vector(2,3,4)
c = a + b
d = b - a
e = a * 4
f = 3 * a
g = a * b

print(a, b, c, d, e, f, g)
