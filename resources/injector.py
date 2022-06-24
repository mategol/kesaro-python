import os
from shutil import rmtree

def inject(file_to_inject, target_file, clone_metadata):
    if os.path.isdir('cached_files'):
        rmtree('cached_files')
    if os.path.isdir('temporary_files'):
        rmtree('temporary_files')
    os.mkdir('cached_files')
    os.mkdir('temporary_files')

    
