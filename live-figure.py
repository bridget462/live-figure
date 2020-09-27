import numpy as np  # to generate random data
import matplotlib.pyplot as plt  # to make figure
plt.style.use('seaborn-colorblind')
plt.style.use('seaborn-whitegrid')

MEASUREMENT_TIME = 50
INTERVAL_SEC = 0.1

for i in range(MEASUREMENT_TIME):
    # replace with your data
    data = np.random.rand(100)

    plt.plot(data)

    # figure appearenc adjustments
    plt.ylim(-0.2, 1.2)
    plt.title(f'FRAME {i+1}')

    # to avoid clearing last plot
    if (i != MEASUREMENT_TIME-1):
        plt.draw()
        plt.pause(INTERVAL_SEC)
        plt.cla()
    else:
        plt.show()
