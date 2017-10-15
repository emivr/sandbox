import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
ms = []
timestamps = []
r = open('log','r')
for f in r:
    timestamp, mil  = f.split('\t')
    # print(mil.strip(), timestamp.strip())
    ms.append(mil.strip())
    timestamps.append(timestamp)

plt.ylabel('ms')
plt.xlabel('number of packages')
plt.title("Plot of {} points".format(len(ms)))
plt.plot(ms)
plt.show()
