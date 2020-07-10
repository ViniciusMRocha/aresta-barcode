import time

# My Files

import countFiles
import ruaInfo

# Start function timer
startTime = time.time()

try:
    ruaInfo.test()
    # ruaInfo.rua1()
    # ruaInfo.rua2()
    # ruaInfo.rua3()
    # ruaInfo.rua4()
    # ruaInfo.rua5()
    # ruaInfo.rua6()
    # ruaInfo.rua7()
    # ruaInfo.rua8()
    # ruaInfo.rua9()
    # ruaInfo.rua10()
    # ruaInfo.rua11()
    # ruaInfo.mergeToPrint()

except:
    print("\n!!!!!!! Error Found !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    raise Exception

# =========== COUNT ALL FILES ================================================================
print("\n======= Total Images Report ==================================")
countFiles.getTotalImageCount()

print("\n======= Elapsed Time ==================================")
endTime = time.time() - startTime
time.strftime("%H:%M:%S", time.gmtime(endTime))
print(time.strftime("%H:%M:%S", time.gmtime(endTime)))
