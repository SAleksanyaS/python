import turtle

scale_x = 25
scale_y = 50

class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.x = 0
        self.y = 0

def set_positions(node, x, y):
    if node is None:
        return x
    node.x = x
    node.y = y
    x_left = set_positions(node.left, x, y + 1)
    x_right = set_positions(node.right, x_left + 1, y + 1)
    return max(x_left, x_right)

def draw_circle(x, y, radius=20):
    turtle.up()
    turtle.goto(x, y - radius)
    turtle.down()
    turtle.circle(radius)

def draw_line(x1, y1, x2, y2):
    turtle.up()
    turtle.goto(x1, y1)
    turtle.down()
    turtle.goto(x2, y2)

def draw_tree(node):
    if node is None:
        return
    draw_circle(node.x * scale_x, node.y * scale_y)
    if node.left is not None:
        draw_line(node.x * scale_x, node.y * scale_y, node.left.x * scale_x, node.left.y * scale_y)
    if node.right is not None:
        draw_line(node.x * scale_x, node.y * scale_y, node.right.x * scale_x, node.right.y * scale_y)
    draw_tree(node.left)
    draw_tree(node.right)

tree_2 = Tree(2, Tree(3, Tree(4), Tree(5)), Tree(6, Tree(7)))
tree_8 = Tree(8, Tree(9, Tree(10), Tree(11, Tree(12), Tree(13))), Tree(14))
tree = Tree(1, tree_2, tree_8)

set_positions(tree, 0, 0)

turtle.speed(0)
turtle.delay(0)
draw_tree(tree)
turtle.hideturtle()
turtle.mainloop()
