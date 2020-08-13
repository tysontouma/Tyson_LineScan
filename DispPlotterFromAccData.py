import matplotlib.pyplot as plt
# from PyQt5 import QtCore
# from plotter import *

freq = 100 # Hz
maxX = 4000 # Approx. 4000 to cut off after test 3
step = 10 # Plotting step, e.g. 10 => plot every 0.2 sec
t_start = 60 # Start time in sec, 20 for test 3
storyHeights = [0, 4, 7.2, 10.4] # In meters
xlim = [-5.0, 11.0]
ylim = [-3.0, 11.0]

lineCount = 0
scan = [{'y': [], 'z': [], 'time': 0.0}]

X = 0
with open("Research/DispFromAcc/ALAB-Center-160D-1.txt", "r") as f:
    next(f)
    for line in f:
        row = line.strip("\n").split(",")

        time   = float(row[0])
        table  = float(row[1])/100
        second = float(row[2])/100
        third  = float(row[3])/100
        roof   = float(row[4])/100

        scan[lineCount]['time'] = time
        scan[lineCount]['y'].append(table)
        scan[lineCount]['y'].append(second)
        scan[lineCount]['y'].append(third)
        scan[lineCount]['y'].append(roof)
        scan[lineCount]['z'] = storyHeights

        lineCount = lineCount + 1
        scan.append({'y': [], 'z': [], 'time': 0})
        X += 1

        # if X == maxX:
        #     break


plt.ion()
for i in range(t_start*freq, X, step):
    plt.plot(scan[i]['y'], scan[i]['z'], '-bo')
    plt.title('Time = {} sec'.format(scan[i]['time']))
    plt.xlim(xlim[0], xlim[1])
    plt.ylim(ylim[0], ylim[1])
    plt.xlabel('[m]')
    plt.ylabel('[m]')
    plt.draw()
    plt.pause(0.0001)
    plt.clf()
    pass




