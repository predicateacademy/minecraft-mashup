from mcpi.minecraft import Minecraft
import mcpi.block as block
import math
from time import *
from distance import *

mc = Minecraft.create()

mc.postToChat("Get ready..")
sleep(5)
start = mc.player.getPos()
mc.postToChat("Go!")
sleep(3)
mc.postToChat("Stop")
stop = mc.player.getPos()
mc.postToChat("You moved: " + str(point_distance(start, stop)))

