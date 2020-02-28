import csv
from pathlib import Path


class ReadFile():

    def __init__(self, path_file, header=False):
        self.content_file = None
        self.path_file = path_file
        self._validate_path()
        self.header = header
        self._get_content_dict() if self.header else self._get_content_list()

    def _validate_path(self):
        if not Path(self.path_file).exists():
            raise FileNotFoundError(self.path_file)

    def _get_content_list(self):
        with open(self.path_file, 'r') as f:
            r = csv.reader(f)
            self.content_file = [i[0] if len(i) == 1 else i for i in r]

    def _get_content_dict(self):
        with open(self.path_file, 'r') as f:
            header = f.readline().strip().split(',')
            r = csv.DictReader(f, header)
            self.content_file = [i for i in r]

    def content(self):
        return self.content_file

    def len_file(self):
        return self.content_file.__len__()
