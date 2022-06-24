import os
from shutil import rmtree, copy2
from properties_manager import *
from file_manager import *

def inject(file_to_inject, target_file, clone_properties):
    if os.path.isdir('cached_files'):
        rmtree('cached_files')
    if os.path.isdir('temporary_files'):
        rmtree('temporary_files')
    os.mkdir('cached_files')
    os.mkdir('temporary_files')

    if clone_properties:
        clone_file_properties(target_file)

    if os.path.isfile(file_to_inject) and os.path.isfile(target_file):
        copy2(file_to_inject, 'cached_files/inject.exe')
        copy2(file_to_inject, 'cached_files/target.exe')




    else:
        print('asd')
