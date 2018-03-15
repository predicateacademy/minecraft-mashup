from mcpi.minecraft import Minecraft
import mcpi.block as block
from time import *
from distance import *
from gpiozero import LED

mc = Minecraft.create()

# My position
me = mc.player.getPos()

# My Finder Light
led = LED(20)

# A random block
rblock = hidden(me, 50)
print rblock

# Find a single block (this can be really hard)
mc.setBlock(rblock.x, rblock.y, rblock.z, block.LAPIS_LAZULI_BLOCK.id)

# Find a wall of tnt
#mc.setBlocks(rblock.x, rblock.y, rblock.z,
#            rblock.x+10, rblock.y+10, rblock.z+10,
#            block.TNT.id, 1)

mc.postToChat("Find it!")

seeking = True
lastPos = me
lastDistanceFromBlock = point_distance(me, rblock)

while seeking :
    me = mc.player.getPos()
    #did me move?
    if lastPos != me:
        distanceFromBlock = point_distance(rblock, me)

        if distanceFromBlock < 2:
            seeking = False
        else:
            if distanceFromBlock < 5:
                led.on()
            if 4 < distanceFromBlock < 11:
                led.blink(0.3,0.3)
            if 10 < distanceFromBlock < 26:
                led.blink(0.6,0.5)
            if 25 < distanceFromBlock < 41:
                led.blink(1,0.5)
            if distanceFromBlock > 40 and distanceFromBlock < lastDistanceFromBlock:
                led.blink()
            if distanceFromBlock > 40 and distanceFromBlock > lastDistanceFromBlock:
                led.off()
          
            lastDistanceFromBlock = distanceFromBlock
          
        sleep(1)         
        
mc.postToChat("Found it!")

  

