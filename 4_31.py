class Num:
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        return visitor.visit_num(self)


class Add:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def accept(self, visitor):
        return visitor.visit_add(self)


class Mul:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def accept(self, visitor):
        return visitor.visit_mul(self)
ast = Add(Num(7), Mul(Num(3), Num(2)))