from mcpi.minecraft import Minecraft
import mcpi.block as block
from time import *

mc = Minecraft.create()

# you can replace TNT with
# AIR, STONE, DIRT, WOOD, WATER, SAND
# http://www.stuffaboutcode.com/p/minecraft-api-reference.html

# try placing things above you
# replace y with y+10

while True:
   x, y, z = mc.player.getPos()
   mc.setBlock(x, y-1, z, block.SAND.id)
   # want to dig a hole? try this
   # mc.setBlocks(x-2,y-2,z-2,x+2,y+2,z+2,block.AIR.id)
   sleep(0.05)


