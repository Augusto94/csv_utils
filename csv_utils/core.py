import boto3
import csv
import os

from alive_progress import alive_bar

from csv_utils.utils import validate_path


@validate_path
def csv_to_list(path_file, header=False):
    with open(path_file, 'r') as f:
        if header:
            fields = f.readline().strip().split(',')
            rows = csv.DictReader(f, fields)
            return [row for row in rows]
        else:
            rows = csv.reader(f)
            return [row[0] if len(row) == 1 else row for row in rows]


def list_to_csv(path_file, content, fieldnames=[]):
    with open(path_file, 'w') as f:
        if fieldnames:
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
        else:
            w = csv.writer(f)

        with alive_bar(len(content), bar='filling') as bar:
            for item in content:
                if isinstance(item, str):
                    item = [item]
                w.writerow(item)
                bar()


def read_from_s3(bucket_name, path_file):

    bucket = boto3.resource('s3').Bucket(bucket_name)
    filename = os.path.basename(path_file)
    bucket.download_file(Filename=filename, Key=path_file)
    content = csv_to_list(filename)
    os.remove(filename)
    return content
