import csv
from alive_progress import alive_bar


class WriteFile():

    def _validate_content(self):
        try:
            _ = iter(self.content)
        except TypeError as e:
            raise e

    def _write_content_list(self):
        with open(self.path_file, 'w') as f:
            w = csv.writer(f)
            with alive_bar(len(self.content), bar='filling') as bar:
                for item in self.content:
                    if isinstance(item, str):
                        item = [item]
                    w.writerow(item)
                    bar()

    def _write_content_dict(self):
        with open(self.path_file, 'w') as f:
            w = csv.DictWriter(f, fieldnames=self.header)
            w.writeheader()
            with alive_bar(len(self.content), bar='filling') as bar:
                for item in self.content:
                    w.writerow(item)
                    bar()

    def write(self, path_file, content, header=[]):
        self.path_file = path_file
        self.content = content
        self._validate_content()
        self.header = header
        self._write_content_dict() if self.header else self._write_content_list()  # noqa
