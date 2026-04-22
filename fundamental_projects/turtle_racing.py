import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ["red", "blue", "green", "orange", "purple", "yellow", "pink", "magenta", "brown", "black"]

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing")
    screen.bgcolor("lightgreen")

def get_number_of_turtles():
    racers = 0
    while True:
        racers = input("How many turtles are racing? (2-10): ")
        if racers.isdigit() and 2 <= int(racers) <= 10:
            racers = int(racers)
        else:
            print("Invalid input. Please enter a number between 2 and 10.")
            continue
        return racers
    

def create_turtles(colors):
    turtles = []
    spacing = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.shape("turtle")
        racer.color(color)
        racer.left(90)
        racer.penup()
        racer.setposition(-WIDTH//2 + (i+1)*spacing, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles

def race(colors):
    r_turtles = create_turtles(colors)

    while True:
        for racer in r_turtles:
            racer.forward(random.randint(1, 10))

            x,y = racer.position()
            if y >= HEIGHT//2 - 10:
                return colors[r_turtles.index(racer)]
     

turtles = get_number_of_turtles()
print(f"{turtles} turtles are racing!")

init_turtle()

'''racer_turtles = turtle.Turtle()
racer_turtles.shape("turtle")
racer_turtles.color("cyan")
racer_turtles.penup()
racer_turtles.speed(5)
racer_turtles.forward(100)'''

random.shuffle(COLORS)
colors = COLORS[:turtles]
winner = race(colors)
print(f"The {winner.capitalize()} turtle wins!")
time.sleep(1)
