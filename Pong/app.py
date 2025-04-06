import turtle

# Window setup
win = turtle.Screen()
win.title("Pong Game")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Paddle Left
paddle_left = turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape("square")
paddle_left.color("white")
paddle_left.shapesize(stretch_wid=6, stretch_len=1)
paddle_left.penup()
paddle_left.goto(-350, 0)

# Paddle Right
paddle_right = turtle.Turtle()
paddle_right.speed(0)
paddle_right.shape("square")
paddle_right.color("white")
paddle_right.shapesize(stretch_wid=6, stretch_len=1)
paddle_right.penup()
paddle_right.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

# Paddle Movement
def paddle_left_up():
    y = paddle_left.ycor()
    if y < 250:
        paddle_left.sety(y + 20)

def paddle_left_down():
    y = paddle_left.ycor()
    if y > -240:
        paddle_left.sety(y - 20)

def paddle_right_up():
    y = paddle_right.ycor()
    if y < 250:
        paddle_right.sety(y + 20)

def paddle_right_down():
    y = paddle_right.ycor()
    if y > -240:
        paddle_right.sety(y - 20)

# Keyboard Bindings
win.listen()
win.onkeypress(paddle_left_up, "w")
win.onkeypress(paddle_left_down, "s")
win.onkeypress(paddle_right_up, "Up")
win.onkeypress(paddle_right_down, "Down")

# Game Loop
while True:
    win.update()
    
    # Move Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() )
    
    # Border Collision
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
    
    # Paddle Collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_right.ycor() + 50 and ball.ycor() > paddle_right.ycor() - 50):
        ball.dx *= -1
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_left.ycor() + 50 and ball.ycor() > paddle_left.ycor() - 50):
        ball.dx *= -1









