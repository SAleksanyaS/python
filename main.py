import random
import turtle


# Определяем функцию для создания дерева
def create_tree(t, trunk_length, level):
    rand_color = (random.randrange(255), random.randrange(255), random.randrange(255))
    if level > 0:
        k = random.uniform(0.1, 0.9)
        # Создаем ствол дерева
        t.forward(trunk_length)
        t.right(30)
        create_tree(t, trunk_length * k, level - 1)
        t.left(60)
        create_tree(t, trunk_length * k, level - 1)
        t.right(30)
        t.backward(trunk_length)

        # Создаем листья на верхушке ствола
        if level == 1:
            t.color("green")
            t.begin_fill()
            t.circle(10)
            t.end_fill()
            t.color("brown")


# Создаем экран и черепашку
screen = turtle.Screen()
screen.setup(800, 600)
t = turtle.Turtle()

# Настраиваем параметры черепашки
t.speed(0)
t.left(90)
t.up()
t.goto(0, -200)
t.down()
t.color("brown")

# Создаем дерево
create_tree(t, 100, 5)

screen.exitonclick()