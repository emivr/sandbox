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

fig, ax = plt.subplots()

ax.plot(ms)
ax.set(xlabel='Number of packets', ylabel='Miliseconds',
       title="Miliseconds to Vg.no for {} packets".format(len(ms)))
ax.grid()

plt.show()
