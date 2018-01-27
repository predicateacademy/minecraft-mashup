from mcpi.minecraft import Minecraft
import mcpi.block as block
from time import *

mc = Minecraft.create()

x, y, z = mc.player.getPos()


for i in range(50):
  mc.setBlock(x+1, y-i, z, block.AIR.id, 1)

for i in range(75):
  mc.setBlock(x+1+i, y-49, z, block.AIR.id, 1)
  mc.setBlock(x+1+i, y-50, z, block.AIR.id, 1)

for i in range(50):
  mc.setBlock(x+1+75, y-i, z, block.AIR.id, 1)

mc.setBlocks(x+35, y-50, z-10, x+50, y-65, z+10, block.AIR.id)
