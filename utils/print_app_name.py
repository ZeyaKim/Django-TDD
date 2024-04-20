import pathlib


def print_app_name():
    metadata = pathlib.Path(__file__).parent.parent / 'metadata.json'
    print(metadata.read_text())

print_app_name()