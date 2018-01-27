from mcpi.minecraft import Minecraft, Vec3
import mcpi.block as block
import time
import random
import words

mc = Minecraft.create()
x, y, z = mc.player.getPos()

words.draw(mc, "Hello Hello", block.TNT.id)


