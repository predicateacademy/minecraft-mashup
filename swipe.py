from mcpi.minecraft import Minecraft, Vec3
import mcpi.block as block
import time
import random
import words

mc = Minecraft.create()
x, y, z = mc.player.getPos()

def poll():
    while True:
        for evt in mc.events.pollBlockHits():
            bx,by,bz = evt.pos
            return mc.getBlock(bx,by,bz)
        time.sleep(0.1)

def house():
    x, y, z = mc.player.getPos()
    mc.setBlocks(x-5, y-5, z-5, x+5, y+5, z+5, block.GLASS.id)
    mc.setBlocks(x-4, y-4, z-4, x+4, y+4, z+4, block.AIR.id)
    

def pool():
    x, y, z = mc.player.getPos()
    mc.setBlocks(x-3, y-1, z-3, x+3, y-5, z+3, block.WATER.id)

def teleport():
    x, y, z = mc.player.getPos()
    mc.setBlocks(x,y+15,z)    

while True:    
    # wait for input
    hitted = poll()

    if hitted == block.TNT.id:
        house()
        teleport()

    if hitted == block.SAND.id:
        pool()
        teleport()

    if hitted == block.GRASS.id:
        words.draw(mc, "Predicate Academy", block.TNT.id)


