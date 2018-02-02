from mcpi.minecraft import Minecraft
import mcpi.block as block
from time import *

# connect to minecraft
mc = Minecraft.create()

# get players position
x, y, z = mc.player.getPos()

# create a big cube of TNT - how many blocks are there?
mc.setBlocks(x-5, y-1, z-5, x+5, y-6, z+5, block.TNT.id, 1)
