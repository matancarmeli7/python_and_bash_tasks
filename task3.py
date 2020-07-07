#!/usr/bin/python3
from pathlib import Path, PurePosixPath
import filecmp
def find_identical_files_in_directory(file, directory):
    identical_files = []
    current_directory = Path(directory)

    for current_file in current_directory.iterdir():

        if Path(file).stat().st_size == Path(current_file).stat().st_size:
            
            if filecmp.cmp(file, current_file, shallow = False):
                identical_files.append(str(current_file))
    
    return identical_files