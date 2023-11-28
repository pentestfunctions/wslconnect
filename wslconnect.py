import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import subprocess
import sys
import os
from utils.commandverifier import check_wsl_commands_and_files
from utils.command_templates import command_templates
import tkinter.messagebox as messagebox

def run_checks():
    missing_elements = check_wsl_commands_and_files()
    update_buttons(input_type_var.get(), missing_elements)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

background_color = "#1f1f23"
button_color = "#303238"
hover_button_color = "#2a2d30"
text_color = "#ebeaee"
font_normal = ("Arial", 12)
font_bold = ("Arial", 12, "bold")

app = tk.Tk()
app.title("WSL Command Runner")
app.geometry("500x600")
app.config(bg=background_color)
app.resizable(False, False)

top_buttons_frame = tk.Frame(app, bg=background_color)
top_buttons_frame.pack(pady=10, fill='x', padx=10)

check_button = tk.Button(top_buttons_frame, text="Check Installed", command=run_checks,
                         bg=button_color, fg=text_color, font=font_normal)
check_button.pack(side=tk.RIGHT, padx=10)

run_all_button = tk.Button(top_buttons_frame, text="Run All", command=lambda: run_all_commands(input_type_var.get()),
                           bg=button_color, fg=text_color, font=font_normal)
run_all_button.pack(side=tk.LEFT, padx=10)

original_logo = Image.open(resource_path("./utils/logo.png"))
resized_logo = original_logo.resize((250, 260), Image.LANCZOS)
logo = ImageTk.PhotoImage(resized_logo)
logo_label = tk.Label(app, image=logo, bg=background_color)
logo_label.pack(pady=10)


def run_command_in_terminal(command_template):
    input_value = input_entry.get()
    if not input_value:
        messagebox.showerror("Error", "Please enter a value.")
        return

    try:
        full_command = command_template.format(input_value, input_value)
    except IndexError:
        print("Error: Command string format and provided arguments do not match.")
        return

    terminal_command = f'cmd.exe /c start cmd.exe /k "{full_command}"'
    subprocess.Popen(terminal_command, shell=True)
    print("Command executed!")


def validate_input():
    input_value = input_entry.get()
    if not input_value:
        print("Please enter a value.")
        return False
    return True

command_buttons = {}

def update_buttons(input_type, missing_elements=None):
    global command_buttons
    command_buttons.clear()
    for widget in commands_frame.winfo_children():
        widget.destroy()

    row = 0
    col = 0
    max_buttons_per_row = 3
    button_width = 15

    for cmd, details in command_templates[input_type].items():
        if cmd == "Explanation":
            continue

        command = details['command']
        required_files = details.get('required_files', [])

        def make_command(command):
            return lambda: run_command_in_terminal(command)

        button_color_to_use = button_color
        if missing_elements:
            if any(file in missing_elements['files'] for file in required_files):
                button_color_to_use = 'red'

        button = tk.Button(commands_frame, text=cmd.capitalize(),
                           command=make_command(command),
                           bg=button_color_to_use, fg=text_color, font=font_normal, width=button_width)
        button.grid(row=row, column=col, padx=5, pady=5)
        button.bind("<Enter>", lambda e: e.widget.config(bg=hover_button_color))
        button.bind("<Leave>", lambda e: e.widget.config(bg=button_color_to_use))

        col += 1
        if col >= max_buttons_per_row:
            col = 0
            row += 1

        command_buttons[cmd] = button


def update_button_colors(missing_elements):
    print("Missing Elements:", missing_elements)

    for command, button in command_buttons.items():
        command_details = command_templates.get(command, {})

        # Check if required files are missing
        required_files = command_details.get('required_files', [])
        if any(file in missing_elements['files'] for file in required_files):
            button.config(bg='red')
            print(f"Updated color for {command}")


def show_help():
    help_window = tk.Toplevel(app)
    help_window.title("Help")
    help_label = tk.Label(help_window, text="If you needed help, you should have asked...", font=font_normal)
    help_label.pack(pady=10, padx=10)


def run_all_commands(input_type):
    if not validate_input():
        return

    input_value = input_entry.get()
    for cmd, template in command_templates[input_type].items():
        full_command = template.format(input_value)
        terminal_command = f'cmd.exe /c start cmd.exe /k "{full_command}"'
        subprocess.Popen(terminal_command, shell=True)
        print(f"Executing: {cmd}")

frame_type_selector = tk.Frame(app, bg=background_color)
frame_type_selector.pack(pady=10)

input_type_var = tk.StringVar(app)
input_type_var.set("url reconnaissance")
input_type_options = list(command_templates.keys())
input_type_menu = tk.OptionMenu(frame_type_selector, input_type_var, *input_type_options, command=update_buttons)
input_type_menu.config(bg=button_color, fg=text_color, font=font_normal, relief=tk.FLAT)
input_type_menu.pack(side=tk.LEFT)

frame_input_text = tk.Frame(app, bg=background_color)
frame_input_text.pack(pady=10, fill='x', padx=10)

input_entry = tk.Entry(frame_input_text, width=20, font=font_normal)
input_entry.pack()

help_button = tk.Button(frame_input_text, text="Help", command=show_help, bg=button_color, fg=text_color, font=font_normal)
help_button.pack(side=tk.RIGHT, padx=5)

commands_frame = tk.Frame(app, bg=background_color)
commands_frame.pack(pady=10, fill='x', padx=10)

update_buttons(input_type_var.get())

footer_label = tk.Label(app, text="© Rowboat (WSL Command Runner)", font=("Arial", 10), bg=background_color, fg=text_color)

footer_label.pack(side=tk.BOTTOM, anchor=tk.CENTER, pady=10)

app.mainloop()
