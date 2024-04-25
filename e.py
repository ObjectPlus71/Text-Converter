import tkinter as tk
from tkinter import filedialog
import os

def convert_file(input_path, mode):
    try:
        with open(input_path, 'r') as infile:
            content = infile.read()

        if mode == 'Uppercase':
            content = content.upper()
        elif mode == 'Lowercase':  # Fix: Changed 'Uppercase' to 'Lowercase'
            content = content.lower()
        elif mode == 'Reverse':
            content = content[::-1]
        elif mode == 'Unreverse':
            content = content[::-1]

        file_name = os.path.basename(input_path)
        output_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[('Text files', '*.txt')],
                                                    initialfile=f'{mode.lower()}_{file_name}')

        if output_path:  # Check if the user selected a file
            with open(output_path, 'w') as outfile:
                outfile.write(content)

            result_label.config(text=f"Conversion successful! Saved as {output_path}")
        else:
            result_label.config(text="Conversion canceled.")
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}")

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[('Text files', '*.txt')])
    if file_path:  # Check if a file was selected
        file_path_entry.delete(0, tk.END)
        file_path_entry.insert(0, file_path)

def convert_and_save():
    input_path = file_path_entry.get()
    mode = mode_var.get()
    if input_path:  # Check if a file path is provided
        convert_file(input_path, mode)
    else:
        result_label.config(text="Please select a file.")

# GUI setup
app = tk.Tk()
app.title("Text File Converter")

file_label = tk.Label(app, text="Select a text file:")
file_label.pack(pady=10)

file_path_entry = tk.Entry(app, width=50)
file_path_entry.pack(pady=10)

browse_button = tk.Button(app, text="Browse", command=browse_file)
browse_button.pack(pady=10)

mode_var = tk.StringVar()
mode_var.set('Uppercase')  # Default mode is set to Uppercase

mode_label = tk.Label(app, text="Choose conversion mode:")
mode_label.pack(pady=10)

mode_options = ['Uppercase', 'Lowercase', 'Reverse', 'Unreverse']
mode_dropdown = tk.OptionMenu(app, mode_var, *mode_options)
mode_dropdown.pack(pady=10)

convert_button = tk.Button(app, text="Convert and Save", command=convert_and_save)
convert_button.pack(pady=10)

result_label = tk.Label(app, text="")
result_label.pack(pady=10)

app.mainloop()
