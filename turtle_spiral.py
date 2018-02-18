#Minecraft Turtle Example - Spiral
import sys
sys.path.insert(0, 'turtle')
import minecraftturtle
import minecraft
import block
import random

#create connection to minecraft
mc = minecraft.Minecraft.create()

#get players position
pos = mc.player.getPos()

#create minecraft turtle
turtle = minecraftturtle.MinecraftTurtle(mc, pos)

turtle.penblock(block.TNT.id, 1)
turtle.speed(10)
turtle.up(5)

for step in range(0,1000):
    turtle.forward(2)
    turtle.right(10)
