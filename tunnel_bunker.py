from mcpi.minecraft import Minecraft
import mcpi.block as block
from time import *

# connect to minecraft
mc = Minecraft.create()

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
