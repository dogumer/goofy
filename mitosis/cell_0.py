import os
import subprocess
import time


time.sleep(2)

cells = os.listdir(os.curdir)
totalcell = len(cells)


selfname = os.path.basename(__file__)

seperator = selfname.split(".")
anotherseperator = seperator[0].split("_")

cellnum = int(anotherseperator[1])

if totalcell > 32-1:
    quit()
    quit
    

newcell1 = "cell_" + str(cellnum*2 + 1) + ".py"
newcell2 = "cell_" + str(cellnum*2 + 2) + ".py"

with open(selfname, 'r') as reader:
    code = reader.readlines()

with open(newcell1, 'w') as writer:
    writer.writelines(code)

with open(newcell2, 'w') as writer:
    writer.writelines(code)

com1 = "python3 " + newcell1
com2 = "python3 " + newcell2


subprocess.Popen(['python3', newcell1])
subprocess.Popen(['python3', newcell2])


os.remove(selfname)


