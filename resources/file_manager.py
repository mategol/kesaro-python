from shutil import copy2

def generate_file_loader(mode):
    if mode == '==':
        copy2('resources/file_loaders/equal.py', 'temporary_files/file_loader.py')