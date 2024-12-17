import os
from nptdms import TdmsFile
import numpy as np
import matplotlib.pyplot as plt


class OLTFTest:

    def __init__(self, tdms_file: TdmsFile):
        """Initialize a OLTF test object.

        A typical OLTF test tdms file has a structure like this:

        ```
        tdms_file
        ├── Group[0]: Experimental Datas
        │   ├── Channel[0]: Frequency
        │   ├── Channel[1]: Mag Values
        │   └── Channel[2]: Unwrapped Phase Values
        ├── Group[1]: Fitting Datas
        └── Group[2]: Open Loop System Parameters
        ```

        Args:
            tdms_file (TdmsFile): A tdms type file.
        """
        self.experimental_datas = tdms_file.groups()[0]
        self.f = np.array(self.experimental_datas.channels()[0])
        self.mag = np.array(self.experimental_datas.channels()[1])
        self.pha = np.array(self.experimental_datas.channels()[2])

    def plot(self,
             label: str = 'Data',
             ax_mag=None,
             ax_pha=None,
             show=False,
             block=False):
        if ax_mag is None or ax_pha is None:
            fig, (ax_mag, ax_pha) = plt.subplots(2, 1, sharex=True)
            ax_mag.grid(True)
            ax_pha.grid(True)
            ax_mag.set_xscale('log')
            ax_pha.set_xscale('log')
            ax_mag.set_ylabel('dB')
            ax_pha.set_ylabel('deg')
            ax_pha.set_xlabel('freq')
        else:
            fig = ax_pha.figure
        ax_mag.plot(
            self.f,
            self.mag,
            label=label,
        )
        ax_pha.plot(self.f, self.pha, label=label)
        ax_mag.legend(loc='upper right')
        ax_pha.legend(loc='upper right')

        if show:
            plt.show(block=block)

        return ax_mag, ax_pha


def open_tdms(file_path: str):
    return OLTFTest(TdmsFile.read(file_path))
