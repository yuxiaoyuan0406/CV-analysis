'''
Author: Yu Xiaoyuan
'''
import argparse
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

from util import Experiment


def argue_parser():
    '''
    Arguments.
    '''
    parser = argparse.ArgumentParser(
        description='Run analysis on CV tests data.')

    parser.add_argument(
        '--data',
        type=str,
        help=
        'Directory to data files, must contains two subdirectory: `C-V` and `Sec Para`.'
    )
    parser.add_argument('--verbose',
                        action='store_true',
                        default=False,
                        help='Print extra info.')

    return parser.parse_args()


def plot_condition(exp_list, condition_func, fig_file_name):
    plt.figure()
    for exp in exp_list:
        if condition_func(exp):
            vol = exp.raw_data[0]
            cap = exp.raw_data[1:]
            cap_mean = np.mean(cap, axis=0)
            cap_std = np.std(cap, axis=0)
            mean_line, = plt.plot(vol,
                                  cap_mean,
                                  linewidth=2,
                                  label=f'{exp.name}',
                                  zorder=2)
            color = mean_line.get_color()

            hsv_color = mcolors.rgb_to_hsv(mcolors.to_rgb(color))
            hsv_color[1] *= 0.3
            ebar_color = mcolors.hsv_to_rgb(hsv_color)
            hsv_color[1] *= 0.3
            rawd_color = mcolors.hsv_to_rgb(hsv_color)

            plt.errorbar(vol,
                         cap_mean,
                         yerr=cap_std,
                         color=ebar_color,
                         fmt='.',
                         zorder=3)
            for _ in cap:
                plt.plot(vol,
                         _,
                         color=rawd_color,
                         linewidth=1,
                         linestyle='--',
                         zorder=1)

    plt.xlabel('Voltage/V')
    plt.ylabel('Capacitance/F')
    plt.legend()
    plt.grid(True)
    plt.gcf().set_size_inches(12, 6)
    plt.savefig(fig_file_name, dpi=600, bbox_inches='tight')


if __name__ == "__main__":
    args = argue_parser()
    verbose = args.verbose

    cv_data_dir = args.data
    raw_data_dir = os.path.join(cv_data_dir, 'C-V')

    raw_data_list = os.listdir(raw_data_dir)
    exp_dir = os.path.join(cv_data_dir, 'Experiments')
    fig_dir = os.path.join(exp_dir, 'figures')
    os.makedirs(fig_dir, exist_ok=True)

    exp_list = []
    for file in raw_data_list:
        exp_list.append(Experiment(exp_dir, os.path.join(raw_data_dir, file)))

    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.serif'] = ['Times New Roman']

    condition_and_name = [
        (lambda exp: exp.id == 'COLI' and exp.plates == 'CT', 'COLI_CT.png'),
        (lambda exp: exp.id == 'COLI' and exp.plates == 'CB', 'COLI_CB.png'),
        (lambda exp: exp.id == '9-14', '9-14.png'),
        (lambda exp: exp.id == '13', '13.png'),
        (lambda exp: exp.id == '14', '14.png'),
        (lambda exp: exp.id == '15', '15.png'),
        (lambda exp: exp.id == '16', '16.png'),
    ]

    for _ in condition_and_name:
        plot_condition(exp_list,
                       _[0],
                       fig_file_name=os.path.join(fig_dir, _[1]))

    plt.show()
