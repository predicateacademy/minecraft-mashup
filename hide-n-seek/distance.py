import random
import math
import mcpi.minecraft as minecraft

#function to round players float position to integer position
def roundVec3(vec3):
    return minecraft.Vec3(int(vec3.x), int(vec3.y), int(vec3.z))

#compute the distance between two points in three dimensional space
def point_distance(point1, point2):
    xd = point2.x - point1.x
    yd = point2.y - point1.y
    zd = point2.z - point1.z
    return math.sqrt((xd*xd) + (yd*yd) + (zd*zd))


#create a random position within numblocks from pos
def hidden(pos, numblocks):
    rblock = roundVec3(pos)
    rblock.x = random.randrange(rblock.x - numblocks, rblock.x + numblocks)
    rblock.y = random.randrange(rblock.y - 5,  rblock.y + 5)
    rblock.z = random.randrange(rblock.z - numblocks, rblock.z + numblocks)
    return rblock

