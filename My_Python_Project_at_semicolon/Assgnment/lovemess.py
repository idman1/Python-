import turtle

t = turtle.Turtle()
t.screen.bgcolor('BLACK')
t.pensize(2)
t.color('GOLD')
t.left(200)
t.backward(10)
t.speed(20000000)
t.shape('arrow')


def car(i):
    if i < 10:
        return

    else:
        t.forward(i)
    t.color('green')
    t.circle(2)
    t.color('brown')
    t.left(30)
    car(3 * i / 4)
    t.right(60)
    car(3 * i / 4)
    t.left(30)
    t.backward(i)


car(100)
turtle.done()
