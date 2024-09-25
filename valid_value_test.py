import os
import numpy as np
import matplotlib.pyplot as plt
from util import Experiment

if __name__ == '__main__':
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.serif'] = ['Times New Roman']

    exp_root = 'data/20240919/cv/Experiments'
    valid_value_tests = ['9-14-valid50mV','9-14-valid100mV']
    valid_value_dirs = [os.path.join(exp_root, _) for _ in valid_value_tests]

    exp = Experiment(exp_root, '9-14-valid')

    for test in valid_value_tests:
        data_path = os.path.join(exp_root, test, 'data.npy')
        data = np.load(data_path)

        vol = data[0]
        cap = data[1:]

        for _ in cap:
            plt.plot(vol, _, label=test)

    plt.xlabel('Voltage/V')
    plt.ylabel('Capacitance/F')

    plt.legend(loc='upper right')
    plt.grid(True)

    plt.gcf().set_size_inches(8,6)
    plt.savefig(exp.img, dpi=300, bbox_inches='tight')
