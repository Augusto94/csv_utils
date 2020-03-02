from pathlib import Path


def validate_path(func):
    def wrapper(*args):
        path = args[0]
        if not Path(path).exists():
            raise FileNotFoundError(path)
        return func(*args)

    return wrapper
