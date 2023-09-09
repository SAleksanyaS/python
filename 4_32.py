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


class PrintVisitor:
    def visit_num(self, node):
        return str(node.value)

    def visit_add(self, node):
        return '({} + {})'.format(node.left.accept(self), node.right.accept(self))

    def visit_mul(self, node):
        return '({} * {})'.format(node.left.accept(self), node.right.accept(self))


ast = Add(Num(7), Mul(Num(3), Num(2)))
pv = PrintVisitor()
print(pv.visit_add(ast))  # (7 + (3 * 2))
