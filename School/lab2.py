#Create a bouncing ball animation inside a room consisting of a floor, a ceiling, a back wall, a left wall, and a right wall.
#The dimensions of the room and the ball are individually assigned to each student.
#The colors of the room and the ball are assigned per class.
#The ball should bounce in three directions (X, Y, Z)
#The ball should not pass through the walls, floor, or ceiling, and should continue bouncing inside the room.
#Submit your laboratory report and Python program code here.

#(Note: Save the Python program code as LBYMF4D_Section_IDNumber (i.e. LBYMF4D_EG8_11111111)

#DIMENSIONS: L10 - W48 - H40 - T0.1 - R0.50

from vpython import *

ballR=0.50; 
wallT=0.1; 
wallL=10; 
wallW=48; 
wallH=40

botwall = box(pos=vector(0,-wallH/2,0), color=color.white, size=vector(wallW,wallT,wallL))
topwall = box(pos=vector(0,wallH/2,0), color=color.white, size=vector(wallW,wallT,wallL))
leftwall = box(pos=vector(-wallW/2,0,0), color=color.white, size=vector(wallT,wallH,wallL))
rightwall = box(pos=vector(wallW/2,0,0), color=color.white, size=vector(wallT,wallH,wallL))
backwall = box(pos=vector(0,0,-wallL/2), color=color.white, size=vector(wallW, wallH, wallT))

marble = sphere(radius=ballR,color=color.red, make_trail=True)

velocity = vector(1, 1, 1)
dt = 1
while True:
    rate(10)

    marble.pos = marble.pos + velocity * dt

    if abs(marble.pos.y) > wallH/2 - ballR:
        velocity.y = -velocity.y
    if abs(marble.pos.x) > wallW/2 - ballR:
        velocity.x = -velocity.x    
    if abs(marble.pos.z) > wallL/2 - ballR:
        velocity.z = -velocity.z