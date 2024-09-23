"""Plot examples of SciencePlot styles."""

import numpy as np
import matplotlib.pyplot as plt
import scienceplots

import os

# Check we are in examples dir
current_dir = os.getcwd().lower()
if (current_dir.endswith('scienceplots')):
    os.chdir('./examples')
# Create 'figures' folder if it does not exist
if (not os.path.exists('./figures')):
    os.makedirs('figures')

def model(x, p):
    return x ** (2 * p + 1) / (1 + x ** (2 * p))


pparam = dict(xlabel='Voltage (mV)', ylabel=r'Current ($\mu$A)')

x = np.linspace(0.75, 1.25, 201)

with plt.style.context(['science', 'usenix']):
    fig, ax = plt.subplots()
    for p in [10, 15, 20, 30, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.autoscale(tight=True)
    ax.set(**pparam)
    fig.savefig('figures/fig01-usenix.pdf')
    fig.savefig('figures/fig01-usenix.jpg')
    plt.close()

