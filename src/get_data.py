# declaring empty list for storing filenames
import os

List = []


def get_data(file_path):
    for path, subdir, files in os.walk(file_path):
        for name in files:
            List.append(os.path.join(path, name))
    return List






