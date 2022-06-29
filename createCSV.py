# --------------------------------------------------------------------------------
# createCSV.py                                                          2022-06-05
# created by tobias(at)haueter.one
# .csv files creating script for test charts
# --------------------------------------------------------------------------------

import datetime
import os
import runpy
import time
import numpy as np


# Number of Lines in CSV ##############################################################################################
#
numIterations = 10000 # 518400 = 180Day@30sec
#
#######################################################################################################################


# Get the current time to build a time-stamp. -------------------------------------------------------------------------
appStartTime = datetime.datetime.now()  # 2022-06-06 17:31:21.401397 <class 'datetime.datetime'>
startTimeStr = appStartTime.isoformat(timespec='milliseconds') # 2022-06-06T17:31:21.401 <class 'str'>
# startTimeStr = appStartTime.strftime("%Y-%m-%dT%H:%M:%S") # 2022-06-06T17:32:37 <class 'str'>

# Get the current working directory -----------------------------------------------------------------------------------
folder = 'outputCSV'
cwd = str(os.getcwd()) + '/' + str(folder)

# Build a filename and the file path; option with timestamp -----------------------------------------------------------
ts = int(time.time()) # UNIX Epoch format
# fileName = "plotlyJS_data_%s.csv" % ts
fileName = "plotlyJS_data10000.csv"
filePath = os.path.join(cwd, fileName)


# Open the file & write a header-line #################################################################################
#
f = open(filePath, 'w')
f.write(
        "time1,"
        "amplitude1,"
        "amplitude2,"
        "amplitude3,"
        "amplitude4\n"
        )
#
#######################################################################################################################


# Print some program-initialization information -----------------------------------------------------------------------
print("The time is: %s" % startTimeStr)
print("Reading %i times and saving data to the file:\n - %s\n" % (numIterations, filePath))

# Prepare final variables for program execution -----------------------------------------------------------------------
curIteration = 0
numSkippedIntervals = 0

duration = 0
curTimeStr = 0

# Sinus Wave Calculation
x0 = np.arange(0, numIterations, 0.01)  # start,stop,step
y1 = np.sin(x0*1)*1
y2 = np.sin(x0*10)*0.75
y3 = np.sin(x0*2)*0.5
y4 = np.sin(x0*0.8)*0.2

# Time Start Step
time_ = appStartTime + datetime.timedelta(seconds=30)

# Iteration Loop for File Content
while curIteration < numIterations:
    try:

        time_ = time_ + datetime.timedelta(seconds=30)
        time1 = time_.strftime("%Y-%m-%d %H:%M:%S")
        # writing content for csv #####################################################################################
        #
        f.write("%s,%s,%s,%s,%s\n" % (time1,
                                        y1[curIteration],
                                        y2[curIteration],
                                        y3[curIteration],
                                        y4[curIteration]
                                        )
                )
        #
        ###############################################################################################################

        print(numIterations, "/", curIteration)
        curIteration = curIteration + 1

    except KeyboardInterrupt:
        break
    except Exception:
        import sys

        print(sys.exc_info()[1])
        break

print("\nFinished!")

# Close file
f.close()

# Auto Call Plotly Script for WebView
# runpy.run_path(path_name='webChart.py')