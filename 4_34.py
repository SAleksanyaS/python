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

ast = Mul(Num(7), Mul(Num(3), Num(2)))
pv = PrintVisitor()
print(pv.visit_mul(ast))


class CalcVisitor:
    def visit_num(self, node):
        return node.value

    def visit_add(self, node):
        return node.left.accept(self) + node.right.accept(self)

    def visit_mul(self, node):
        return node.left.accept(self) * node.right.accept(self)

ast = Mul(Num(7), Mul(Num(3), Num(2)))
cv = CalcVisitor()
print(cv.visit_mul(ast))


class StackVisitor:
    def visit_num(self, node):
        return 'PUSH {}'.format(node.value)

    def visit_add(self, node):
        return '{}\n{}'.format(node.left.accept(self), node.right.accept(self)) + '\nADD'

    def visit_mul(self, node):
        return '{}\n{}'.format(node.left.accept(self), node.right.accept(self)) + '\nMUL'

sv = StackVisitor()
print(sv.visit_mul(ast))