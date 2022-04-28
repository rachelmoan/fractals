# Simple python program that draws a fractal using the turtle library
from turtle import *
import turtle
  

# build_tree function. Recursive function
# input: turt- instance of turtle,
#        length- length of branchs, 
#        subtract- length by which subbranches will be smaller than main branch
#        angle- angle from which branches will emerge
# output: drawing of tree

def draw_tree(turt, length, subtract, angle):

  # base case: exit when the branch lengths get too short
  if length > 15:
    turt.forward(length)
    new_length = length - subtract
    turt.left(angle)
    draw_tree(turt, new_length, subtract, angle)
    turt.right(angle * 2)
    draw_tree(turt, new_length, subtract, angle)
    turt.left(angle)
    turt.backward(length)


def draw_koch_curve(t, iterations, length, shortening_factor, angle):
  if iterations == 0:
    t.forward(length)
  else:
    iterations = iterations - 1
    length = length / shortening_factor
    draw_koch_curve(t, iterations, length, shortening_factor, angle)
    t.left(angle)
    draw_koch_curve(t, iterations, length, shortening_factor, angle)
    t.right(angle * 2)
    draw_koch_curve(t, iterations, length, shortening_factor, angle)
    t.left(angle)
    draw_koch_curve(t, iterations, length, shortening_factor, angle)


def draw_koch_stool(turtle, level):
    if level < 1:
        turtle.forward(10)
    else:
        draw_koch_stool(turtle, level-1)
        turtle.left(90)
        draw_koch_stool(turtle, level-1)
        turtle.right(90)
        draw_koch_stool(turtle, level-1)
        turtle.right(90)
        draw_koch_stool(turtle, level-1)
        turtle.left(90)
        draw_koch_stool(turtle, level-1)



# draw the tree

tree = turtle.Turtle()
tree.hideturtle()


# make the drawing face upward 
tree.setheading(90)
tree.color('green')
draw_tree(tree, 50, 5, 30)
turtle.mainloop()


'''
#uncomment whatever you want to draw

# draw the koch curve

koch = turtle.Turtle()
koch.hideturtle()

#draw_koch_stool(koch, 3)

for i in range(3):
  #draw_koch_stool(koch, 200, 3)
  #draw_koch_curve(koch, 3, 200, 3, 60)
  koch.right(120)
turtle.mainloop()

'''
