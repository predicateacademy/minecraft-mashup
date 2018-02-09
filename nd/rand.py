import mcpi.minecraft as minc
import mcpi.block as block
import random, time
from disasters import *
mc = minc.Minecraft.create()

disasters = [tsunami, heatwave, meteor, meteor_shower, geyser, earthquake, sinkhole]

while True:
    random.shuffle(disasters)
    disaster = random.choice(disasters)
    mc.postToChat(disaster)
    ppos = mc.player.getTilePos()
    disaster(mc, ppos.x, ppos.z)
    time.sleep(5)
