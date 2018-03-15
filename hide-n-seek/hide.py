from mcpi.minecraft import Minecraft
import mcpi.block as block
from time import *
from distance import *

mc = Minecraft.create()

# My position
me = mc.player.getPos()  

# A random block
rblock = hidden(me, 50)
print rblock

# Find a single block (this can be really hard)
#mc.setBlock(rblock.x, rblock.y, rblock.z, block.LAPIS_LAZULI_BLOCK.id)

# Find a wall of tnt
mc.setBlocks(rblock.x, rblock.y, rblock.z,
            rblock.x+10, rblock.y+10, rblock.z+10,
            block.TNT.id, 1)

mc.postToChat("Find it!")
d = point_distance(me, rblock)
while d > 3.0 :    
    mc.postToChat("Distance to target: " + str(int(d)))    
    sleep(1)
    me = mc.player.getPos()
    d = point_distance(me, rblock)
mc.postToChat("Found it!")

  

