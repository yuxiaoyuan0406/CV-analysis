import os
import numpy as np
import matplotlib.pyplot as plt
from util import Experiment

if __name__ == '__main__':
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.serif'] = ['Times New Roman']

    exp_root = 'data/20240919/cv/Experiments'
    exp_target_id = '9-14'
    exp_polar = 'CT'
    exp_name = f'{exp_target_id}-{exp_polar}'
    exp_gravity = ['-0g', '-1g', '+1g']
    exp_dir_names = [f'{exp_name}-valid100mV{_}' for _ in exp_gravity]


    fig = plt.figure()
    exp = Experiment(exp_root, exp_name)

    for test in exp_dir_names:
        data_path = os.path.join(exp_root, test, 'data.npy')
        data = np.load(data_path)

        vol = data[0]
        cap = data[1:]
        cap_mean = np.mean(cap, axis=0)

        plt.plot(vol, cap_mean, label=test)

    plt.xlabel('Voltage/V')
    plt.ylabel('Capacitance/F')

    plt.legend(loc='upper right')
    plt.grid(True)

    plt.gcf().set_size_inches(12,6)
    plt.savefig(exp.img, dpi=300, bbox_inches='tight')
    plt.close()
