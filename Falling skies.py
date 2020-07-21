import turtle
import random


score = 0 
lives = 3

wn = turtle.Screen()
wn.title("Falling skies")
wn.bgcolor("black")
wn.bgpic("Nature.gif")
wn.setup(width=800, height=600)
wn.tracer(0)

wn.register_shape("DEER_left.gif")
wn.register_shape("NUT.gif")
wn.register_shape("MEAT.gif")
wn.register_shape("HUNTER.gif")
wn.register_shape("DEER_right.gif")


#Add the player
player = turtle.Turtle()
player.speed(0)
player.shape("DEER_right.gif")
player.color("white")
player.penup()
player.goto(0, -250)
player.direction = "stop"

good_guys = []

for _ in range(10):
    good_guy = turtle.Turtle()
    good_guy.speed(0)
    good_guy.shape("NUT.gif")
    good_guy.color("green")
    good_guy.penup()
    good_guy.goto(-100, 250)
    good_guy.speed(random.uniform(1,2))

    good_guys.append(good_guy)

good_things = []

for _ in range(10):
    good_thing = turtle.Turtle()
    good_thing.speed(0)
    good_thing.shape("MEAT.gif")
    good_thing.color("green")
    good_thing.penup()
    good_thing.goto(-100, 250)
    good_thing.speed(random.uniform(1,2))

    good_things.append(good_thing)


bad_guys = []

for _ in range(10):
    bad_guy = turtle.Turtle()
    bad_guy.speed(0)
    bad_guy.shape("HUNTER.gif")
    bad_guy.color("red")
    bad_guy.penup()
    bad_guy.goto(100, 250)
    bad_guy.speed(random.uniform(1,2))

    bad_guys.append(bad_guy)


pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.shape("square")
pen.color("red")
pen.penup()
pen.goto(0, 260)
font = ("Courier", 24, "normal")
pen.write("Score {} Lives {}".format(score, lives), align="center", font=font)


#Functions

def go_left():
    player.direction = "left"
    player.shape("DEER_left.gif")


def go_right():
    player.direction = "right"
    player.shape("DEER_right.gif")


#Keyboard Binding
wn.listen()
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")


# Main game loop
while True:
    #Update the screen
    wn.update()

    if player.direction == "left":
        player.setx(player.xcor() - 1.5)

    if player.direction == "right":
        player.setx(player.xcor() + 1.5)


    if player.xcor() < - 390:
        player.setx(-390)

    elif player.xcor () > 390:
        player.setx(390)


    for good_guy in good_guys:
        good_guy.sety(good_guy.ycor() - good_guy.speed())

        if good_guy.ycor() < -300:
            good_guy.goto(random.randint(-300, 300), random.randint(400, 800))


        if good_guy.distance(player) < 40:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            good_guy.goto(x, y)
            score += 10
            pen.clear()
            pen.write("Score {} Lives {}".format(score, lives), align="center", font=font)



    for good_thing in good_things:
        good_thing.sety(good_thing.ycor() - good_thing.speed())

        if good_thing.ycor() < -300:
            good_thing.goto(random.randint(-300, 300), random.randint(400, 800))


        if good_thing.distance(player) < 40:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            good_thing.goto(x, y)
            score += 10
            pen.clear()
            pen.write("Score {} Lives {}".format(score, lives), align="center", font=font)

    for bad_guy in bad_guys:
        bad_guy.sety(bad_guy.ycor() - bad_guy.speed())

        if bad_guy.ycor() < -300:
            bad_guy.goto(random.randint(-300, 300), random.randint(400, 800))


        if bad_guy.distance(player) < 30:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            bad_guy.goto(x, y)
            score -= 10
            lives -= 1
            pen.clear()
            pen.write("Score {} Lives {}".format(score, lives), align="center", font=font)



wn.mainloop()