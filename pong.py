
import turtle  # module for drawing (thanks ENGR 102)
# can also use pygame
import os


#showing the game. 
wn = turtle.Screen() 
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)  # can change this later, dimensions
wn.tracer(0)
# Score
score_a = 0  # player A
score_b = 0  # player B



# Paddle A
paddle_a = turtle.Turtle()  # turtle object
paddle_a.speed(0)  # speed of animation for turtle module (max speed)
paddle_a.shape("square")  # default 20 by 20
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # 100 by 20
paddle_a.penup()  # means that we aren't drawing continiously
paddle_a.goto(-350,0)  # on the left side


# Paddle B
paddle_b = turtle.Turtle()  # turtle object
paddle_b.speed(0)  # speed of animation for turtle module (max speed)
paddle_b.shape("square")  # default 20 by 20
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) # 100 by 20
paddle_b.penup()  # means that we aren't drawing continiously
paddle_b.goto(350,0)  # now on the right side


# Pen: default score
pen = turtle.Turtle()
pen.speed(0)  # animation speed
pen.color("white")
pen.penup()  # don't want to see the drawing proceess
pen.hideturtle()
pen.goto(0, 260)  # sc
pen.write("Player A: 0  Player B: 0", align = "center", font = ("Courier", 24, "normal"))  # bold, italics i think

ball = turtle.Turtle()  # turtle object
ball.speed(0)  # speed of animation for turtle module (max speed)
ball.shape("circle")  # default 20 by 20
ball.color("white")
ball.penup()  # means that we aren't drawing continiously
ball.goto(0, 0)  # now on the middle
# adjusting the speed for the ball
ball.dx = 0.20  # ball moves by 2 pixels (right)
ball.dy = 0.20  # (up)

def paddle_a_up():
    y = paddle_a.ycor()  # returns y coordinate
    y += 20  # moves up 20 pixels
    paddle_a.sety(y)
    os.systen("afplay bounce.wav&")  # need to download the music though

def paddle_a_down():
    y = paddle_a.ycor()  # returns y coordinate
    y -= 20  # moves up 20 pixels
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()  # returns y coordinate
    y += 20  # moves up 20 pixels
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()  # returns y coordinate
    y -= 20  # moves up 20 pixels
    paddle_b.sety(y)

# keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")  # W, paddle goes up by 20
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")  # arrow keys
wn.onkeypress(paddle_b_down, "Down")  # arrow keys


while True:
    wn.update()
    # move the ball
    ball.setx(ball.xcor() + ball.dx)  # dx cause speed of xcor
    ball.sety(ball.ycor() + ball.dy)  # dy cause speed of ycor
    # top border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  # reverses the direction (slope is negative)
    # right side border  player 2: point
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
        score_a += 1
        # updating the score
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))  # bold, italics i think
    # bottom border
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    # left side border  player 1: point
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
        score_b += 1
        # updating the score
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",font=("Courier", 24, "normal"))  # bold, italics i think


    # right paddle
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40) and ball.ycor() > paddle_b.ycor() -40:
        ball.setx(340)
        ball.dx *= -1
    # left paddle
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40) and ball.ycor() > paddle_a.ycor() -40:
        ball.setx(-340)
        ball.dx *= -1



#  i want to add a welcome page (in text fle) which interacts with the user

#  as level progresses:
    # add more obstacles
    # higher speed of the ball
    # add multiple balls that react to each other
# also i wannt the background to be better

