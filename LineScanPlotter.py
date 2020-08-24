import matplotlib.pyplot as plt
# from PyQt5 import QtCore
# from plotter import *

freq = 50 # Hz
maxX = 4000 # Approx. 4000 to cut off after test 3
step = 10 # Plotting step, e.g. 10 => plot every 0.2 sec
t_start = 20 # Start time in sec, 20 for test 3
xlim = [-17.0, -1.0]
ylim = [-3.0, 11.0]


# f = open("/Users/tatsuhikosweet/PycharmProjects/Research/t3_lineplot.txt", "r")
f = open("t3_lineplot.txt", "r")

lineCount = 0
scan = [{'y': [], 'z': [], 'time': 0.0}]

X = 0
for line in f:
    # if X > t_start*freq:
    #     X += 1
    #     continue
    lineCount =+ 1
    # row = line.strip("\n").replace('"','').split("\t")
    row = line.strip("\n").split(",")
    x = float(row[0])
    y = float(row[1])
    z = float(row[2])
    if abs(x - X) < 0.01:
        scan[X]['y'].append(y)
        scan[X]['z'].append(z)
    else:
        X += 1
        scan.append({'y': [], 'z': [], 'time': X/freq})
    if X == maxX:
        break

    pass
pass

f.close()

plt.ion()
for i in range(t_start*freq, step, step):
    plt.plot(scan[i]['y'], scan[i]['z'], '-b')
    # plt.scatter(scan[i]['y'], scan[i]['z'], '-b')
    plt.title('Time = {} sec'.format(scan[i]['time']))
    plt.xlim(xlim[0], xlim[1])
    plt.ylim(ylim[0], ylim[1])
    plt.xlabel('[m]')
    plt.ylabel('[m]')
    plt.draw()
    plt.pause(0.0001)
    plt.clf()
    pass


pass



