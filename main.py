#in this project, we'll gonna try to work on some modern art
#inspired by Damien Hirst and his dots
#hope you guys enjoy it.

import colorgram
import random
import turtle as t


#colors = colorgram.extract('art.jpg', 25)

rgbcolors = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), 
             (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), 
             (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), 
             (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), 
             (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), 
             (172, 153, 159), (212, 183, 177), (176, 198, 203)]

# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     new_color = (r, g, b)
#     rgbcolors.append(new_color)

t.colormode(255)   

torugo = t.Turtle()

torugo.shape('turtle')

numofdots = 100

    
def drawn():
    torugo.penup()
    for i in range(10):
        torugo.dot(20, random.choice(rgbcolors))
        torugo.penup
        torugo.forward(50)      
        
        

torugo.penup()
torugo.goto(-300, -250) 
for dot_count in range(1, numofdots + 1):
    torugo.dot(20, random.choice(rgbcolors))
    torugo.forward(50)
    if dot_count % 10 == 0:
        torugo.setheading(90)
        torugo.forward(50)
        torugo.setheading(180)
        torugo.forward(500)
        torugo.setheading(0)
        
screen = t.Screen()
screen.exitonclick()