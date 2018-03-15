from mcpi.minecraft import Minecraft
import mcpi.block as block
import time
import threading

class ExplodingBlock(threading.Thread):

    def __init__(self, pos, fuseInSecs, blastRadius, blk):
        #Setup object
        threading.Thread.__init__(self)
        self.pos = pos
        self.fuseInSecs = fuseInSecs
        self.blastRadius = blastRadius
        self.blk = blk

    def run(self):
        #Open connect to minecraft
        mc = Minecraft.create()

        #Get values
        pos = self.pos
        blastRadius = self.blastRadius

        #Explode the block!
        # get block type
        blockType = mc.getBlock(pos.x, pos.y, pos.z)
        # flash the block
        for fuse in range(0, self.fuseInSecs):
            mc.setBlock(pos.x, pos.y, pos.z, block.AIR)
            time.sleep(0.5)
            mc.setBlock(pos.x, pos.y, pos.z, blockType)
            time.sleep(0.5)
        # create sphere of air
        for x in range(blastRadius*-1,blastRadius):
            for y in range(blastRadius*-1, blastRadius):
                for z in range(blastRadius*-1,blastRadius):
                    if x**2 + y**2 + z**2 < blastRadius**2:
                        mc.setBlock(pos.x + x, pos.y + y, pos.z + z, self.blk, 1)

if __name__ == "__main__":

    time.sleep(5)
    #Connect to minecraft by creating the minecraft object
    # - minecraft needs to be running and in a game
    mc = Minecraft.create()

    #Post a message to the minecraft chat window
    mc.postToChat("Mr Mikes World Destroyer")

    #loop until Ctrl C
    try:
        while True:
            #Get the block hit events
            blockHits = mc.events.pollBlockHits()
            # if a block has been hit
            if blockHits:
                # for each block that has been hit
                for blockHit in blockHits:
                    blk = mc.getBlock(blockHit.pos)
                    #Create and run the exploding block class in its own thread
                    # pass the position of the block, fuse time in seconds and blast radius
                    # threads are used so multiple exploding blocks can be created
                    explodingBlock = ExplodingBlock(blockHit.pos, 3, 3, blk)
                    explodingBlock.daemon
                    explodingBlock.start()
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("stopped")
