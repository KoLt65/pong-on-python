import turtle
import os

wn = turtle.Screen()
wn.title("рong")
wn.bgcolor("black")
wn.setup(width = 1.0, height = 1.0)
wn.tracer(0)

# Счет в начале
score_a = 0
score_b = 0

# Игрок А
paddle_a = turtle.Turtle()
paddle_a.speed(100)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Игрок B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Мячь
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# Ракетки
pen = turtle.Turtle()
pen.speed(100)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("0                    0", align="center", font=("Courier", 25, "normal"))

# Функции
def paddle_a_up():
    y = paddle_a.ycor()
    y += 10
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 10
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 10
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 10
    paddle_b.sety(y)

# Кнопки управления игроков
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Основной цикл
while True:
    wn.update()
    
    # анимация шара
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Проверка краев

    # Вверх и вниз
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")
   
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    # Лево и право
    if ball.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write("{}                    {}".format(score_a, score_b), align="center", font=("Courier", 25, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("{}                    {}".format(score_a, score_b), align="center", font=("Courier", 25, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Столкновение с ракеткой
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1 
        os.system("afplay bounce.wav&")
    
    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
        os.system("afplay bounce.wav&")
