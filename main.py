import os
import numpy as np
import matplotlib.pyplot as plt

from util import Experiment

def run_analysis(exp_dir, data_dir):
    experiment_name = os.path.split(data_dir)[1].split(' ')[0]
    exp = Experiment(exp_dir, experiment_name)

    with open(data_dir, 'r') as file:
        lines = file.readlines()
    with open(exp.info, 'w') as info:
        info.writelines(lines[1:5])

    data_lines = lines[8:]
    raw_data = np.loadtxt(data_lines, delimiter='\t').transpose()
    np.save(exp.data, raw_data)

    vol = raw_data[0]
    cap = raw_data[1:]

    cap_mean = np.mean(cap, axis=0)
    cap_std = np.std(cap, axis=0)

    plt.figure()

    for _ in cap:
        plt.plot(vol, _, color='gray', linewidth=1, linestyle='--')
    plt.plot(vol, cap_mean, linewidth=2, label=f'{exp.name} average')
    plt.errorbar(vol, cap_mean, yerr=cap_std, fmt='r.')

    plt.xlabel('Voltage/V')
    plt.ylabel('Capacitance/F')

    plt.grid(True)

    plt.gcf().set_size_inches(12,6)
    plt.savefig(exp.img, dpi=300, bbox_inches='tight')

    plt.close()

if __name__ == "__main__":
    data_dir = '/home/dennis/Program/cv-analysis/data/20240919'
    cv_data_dir = os.path.join(data_dir, 'cv')
    raw_data_dir = os.path.join(cv_data_dir, 'C-V')
    raw_data_list = [os.path.join(raw_data_dir, filename) for filename in os.listdir(raw_data_dir)]
    exp_dir = os.path.join(cv_data_dir, 'Experiments')
    os.makedirs(exp_dir, exist_ok=True)

    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.serif'] = ['Times New Roman']

    for data_dir in raw_data_list:
        run_analysis(exp_dir, data_dir)
