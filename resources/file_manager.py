from shutil import copy2
from tkinter import Tk, filedialog

def generate_file_loader(mode):
    if mode == '==':
        copy2('resources/file_loaders/equal.py', 'temporary_files/file_loader.py')

    with open('temporary_files/file_loader.py', 'r') as file_loader:
        file_content = file_loader.readlines()
        file_content[0] = "injected_program_path='cached_files/inject.exe'\n"
        file_content[1] = "original_program_path='cached_files/target.exe'\n"

    with open('temporary_files/file_loader.py', 'w') as file_loader:
        for i in file_content:
            file_loader.write(i)

def get_manual_path(message, extension):
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    open_dir = filedialog.askopenfilename(filetypes=[(message, extension)])
    root.destroy()
    return open_dir