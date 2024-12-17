from nptdms import TdmsFile
import util
import matplotlib.pyplot as plt

if __name__ == "__main__":
    file_path = '/home/dennis/Program/cv-analysis/data/20241203/oltf/OLTF Data(Manual) coli-h520 2024-12-03 16-14.tdms'

    tdms_file = TdmsFile.read(file_path)

    for group in tdms_file.groups():
        print(f'Group: {group.name}')

        for channel in group.channels():
            print(f'\tChannel: {channel.name}')

            # data = channel[:]
            # print(f'\t\tData: {data}')

    experiment = util.open_tdms(file_path)
    experiment.plot()
    plt.show()
