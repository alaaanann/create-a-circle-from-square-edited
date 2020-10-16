import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(0)
my_turtle.color('white')
turtle.bgcolor('pink')

def square(angle, lenght):
  for i in range(4):
    my_turtle.right(angle)
    my_turtle.forward(lenght)

for i in range(200):
  square(90, 90)
  my_turtle.right(7)

