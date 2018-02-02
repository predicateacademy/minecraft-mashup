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
    mc.player.setPos(x,y+25,z)

def tunnel():
    # grab the players current position
    x, y, z = mc.player.getPos()

    # build an AIR tunnel down fifty blocks
    for i in range(50):
      mc.setBlock(x+1, y-i, z, block.AIR.id, 1)

    # build an AIR tunnel across (by 2) 50 blocks below ground
    for i in range(75):
      mc.setBlock(x+1+i, y-49, z, block.AIR.id, 1)
      mc.setBlock(x+1+i, y-50, z, block.AIR.id, 1)

    # build an AIR tunnel back up to the surface
    for i in range(50):
      mc.setBlock(x+1+75, y-i, z, block.AIR.id, 1)

    # create a bunker
    mc.setBlocks(x+35, y-50, z-10, x+50, y-65, z+10, block.AIR.id)

while True:
    # wait for input
    hitted = poll()

    if hitted == block.DIAMOND_BLOCK.id:
        tunnel()
        
    if hitted == block.TNT.id:
        house()
        teleport()

    if hitted == block.SAND.id:
        pool()
        teleport()

    if hitted == block.GRASS.id:
        words.draw(mc, "Predicate Academy", block.TNT.id)
