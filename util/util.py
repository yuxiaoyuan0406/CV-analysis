import os

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

class Experiment:
    def __init__(self, root_dir, name) -> None:
        self.root = root_dir
        self.name = name
        self.dir = os.path.join(self.root, self.name)
        os.makedirs(self.dir, exist_ok=True)
        self.info = os.path.join(self.dir, 'info.txt')
        self.data = os.path.join(self.dir, 'data')
        self.img_dir = os.path.join(self.root, 'figures')
        os.makedirs(self.img_dir, exist_ok=True)
        self.img = os.path.join(self.img_dir, f'{self.name}.png')

    def __del__(self):
        pass