import turtle
def bresenham_line(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x_step = 1 if x1 < x2 else -1
    y_step = 1 if y1 < y2 else -1
    error = dx - dy
    line_p = []
    x, y = x1, y1
    while True:
        line_p.append((x, y))
        if x == x2 and y == y2:
            break
        e2 = 2 * error
        if e2 > -dy:
            error -= dy
            x += x_step
        if e2 < dx:
            error += dx
            y += y_step
    return line_p
turtle.setup(500, 500)
turtle.speed(0)
x1, y1 = 100, 100
x2, y2 = 400, 300
line_p = bresenham_line(x1, y1, x2, y2)
turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
for x, y in line_p:
    turtle.goto(x, y)
turtle.exitonclick()