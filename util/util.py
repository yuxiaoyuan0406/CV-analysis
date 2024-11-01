import os
import numpy as np

def change_encoding(filename, op_encoding='GB2312', sv_encoding='UTF-8'):
    """Change the encoding of a text file.

    Args:
        filename (_type_): Path to file to be re-encoded.
        op_encoding (str, optional): Opening encoding. Defaults to 'GB2313'.
        sv_encoding (str, optional): Saving encoding. Defaults to 'UTF-8'.
    """
    try:
        with open(filename, 'r', encoding=op_encoding) as file:
            content = file.read()
        with open(filename, 'w', encoding=sv_encoding) as file:
            file.write(content)
    except Exception as e:
        print(f'Exception handling file: {e}')

def raw_cv_to_array(filename, encoding='GB2312'):
    with open(filename, 'r', encoding=encoding) as file:
        lines = file.readlines()

    data_lines = lines[8:]
    return np.loadtxt(data_lines, delimiter='\t').transpose()

class Experiment:
    def __init__(
        self,
        exp_save_dir,
        raw_file,
    ) -> None:
        self.save_dir = exp_save_dir
        self.raw_file = raw_file

        self.filename = os.path.splitext(os.path.basename(raw_file))[0]
        self.name, self.date, self.time = self.filename.split(' ')
        self.name_split = self.name.split('_')
        self.id = self.name_split[0]
        self.plates = self.name_split[1]
        self.save_dir = os.path.join(self.save_dir, self.id, self.plates)
        os.makedirs(self.save_dir, exist_ok=True)

        self.raw_data = raw_cv_to_array(self.raw_file)
