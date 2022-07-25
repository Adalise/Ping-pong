import turtle

# initiate ping-pong window parameters

window = turtle.Screen()
window.title('Hello, I\'m a humble Ping-Pong')
window.bgcolor('black')
window.setup(width=800, height=600)  # window.screensize(800, 600)
window.tracer(0)

# initiate rackets parameters

racket_left = turtle.Turtle()
racket_left.speed(0)
racket_left.shape('square')
racket_left.color('#C70039')
racket_left.shapesize(stretch_len=1, stretch_wid=5)
racket_left.left(180)
racket_left.penup()
racket_left.goto(-350, 0)

racket_right = turtle.Turtle()
racket_right.speed(0)
racket_right.shape('square')
racket_right.color('#21D1AE')
racket_right.shapesize(stretch_len=1, stretch_wid=5)
racket_right.penup()
racket_right.goto(350, 0)

# initiate ball parameters

ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('#16C0E6')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

# score table
score = turtle.Turtle()
score.speed(0)
score.shape('square')
score.color('#DFC7F8')
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write('Player A: 0  Player B: 0', align='center', font=('Courier', 17, 'normal'))

# score variables
player_a = 0  # left player
player_b = 0  # right player

# movement funcs

def racket_left_up():
    y = racket_left.ycor()
    y += 20
    racket_left.sety(y)


def racket_left_down():
    y = racket_left.ycor()
    y -= 20
    racket_left.sety(y)


def racket_right_up():
    y = racket_right.ycor()
    y += 20
    racket_right.sety(y)


def racket_right_down():
    y = racket_right.ycor()
    y -= 20
    racket_right.sety(y)


# keyboard binds

window.listen()

window.onkeypress(racket_left_up, 'w')
window.onkeypress(racket_left_down, 's')
window.onkeypress(racket_right_up, 'Up')
window.onkeypress(racket_right_down, 'Down')

# loop to keep ping-pong window visible for an unlimited period
while True:
    window.update()
    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # prevent ball from going off the y border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # return ball to the center of the field if it goes off the x border
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        # score counter Player A
        player_a += 1
        score.clear()
        score.write(f'Player A: {player_a}  Player B: {player_b}', align='center', font=('Courier', 17, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        # score counter Player B
        player_b += 1
        score.clear()
        score.write(f'Player A: {player_a}  Player B: {player_b}', align='center', font=('Courier', 17, 'normal'))

    # racket&ball interactions
    if ball.xcor() > 340 and ball.ycor() < racket_right.ycor() + 50 and ball.ycor() > racket_right.ycor() - 50:
        ball.dx *= -1

    if ball.xcor() < -340 and ball.ycor() < racket_left.ycor() + 50 and ball.ycor() > racket_left.ycor() - 50:
        ball.dx *= -1

    # prevent the rackets to go off the borders
    if racket_left.ycor() > 260:
        racket_left.goto(-350, 260)

    if racket_left.ycor() < -240:
        racket_left.goto(-350, -240)

    if racket_right.ycor() > 260:
        racket_right.goto(350, 260)

    if racket_right.ycor() < -240:
        racket_right.goto(350, -240)

