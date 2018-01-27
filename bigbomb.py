from mcpi.minecraft import Minecraft
import mcpi.block as block
from time import *

mc = Minecraft.create()

x, y, z = mc.player.getPos()
mc.setBlock(x-5, y-1, z-5, x+5, y-6, z+5, block.TNT.id, 1)

