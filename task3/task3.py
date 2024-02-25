import cmath
import math
from math import ceil
import os
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox , simpledialog
from tkinter import filedialog
from scipy.signal import convolve




# ---------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------
# start of task 3

class QuantizationAndEncoding:
    def __init__(self, root):
        self.root = root
        self.InputSignal = None
        self.OutputQuantizedSignal = []
        self.OutputIntervalIndices = []
        self.OutputIntervalIndices_unformated = []
        self.QuantizationError = []
        self.num_bits_or_levels = None

    def quantize_signal(self):
        if self.InputSignal is None:
            return "Please load a signal first."

        if self.num_bits_or_levels is None:
            return "Please choose the number of bits or levels."

        max_amp, min_amp, delta = max(self.InputSignal), min(self.InputSignal), None

        if self.num_bits_or_levels == 3:
            num_quantization_levels = 2 ** 3  # 3 bits
        elif self.num_bits_or_levels == 4:
            num_quantization_levels = 4  # 4 levels

        delta = (max_amp - min_amp) / num_quantization_levels
        x = float(format(delta,'.2f'))
        intervals = [(min_amp + i * x, min_amp + (i + 1) * x) for i in range(num_quantization_levels)]
        self.OutputIntervalIndices = []
        self.OutputIntervalsamples = []
        self.OutputIntervalIndices_unformated = []
        self.QuantizationError = []

        if num_quantization_levels == 8:
            for sample in self.InputSignal:

                for i, (lower_limit, upper_limit) in enumerate(intervals):
                    if lower_limit <= sample <= upper_limit:
                        quantized = (lower_limit + upper_limit) / 2.0
                        self.OutputIntervalIndices.append((format(i,'0{}b'.format(3))))
                        self.OutputIntervalsamples.append(float(format(quantized,'.2f')))

                        break

            for index, sample in zip(self.OutputIntervalIndices, self.OutputIntervalsamples):
                print(f"{index}  {sample} ")


        elif num_quantization_levels == 4:
            for sample in self.InputSignal:

                for i, (lower_limit, upper_limit) in enumerate(intervals):
                    if lower_limit <= sample <= upper_limit:
                        quantized = (lower_limit + upper_limit) / 2.0
                        quantization_error = quantized - sample
                        self.OutputIntervalIndices_unformated.append(i+1)
                        self.OutputIntervalIndices.append(format(i,'0{}b'.format(2)))
                        self.OutputIntervalsamples.append(float(format(quantized,'.3f')))
                        self.QuantizationError.append(float(format(quantization_error,'.3f')))

                        break


            for index_un,index, sample , error in zip(self.OutputIntervalIndices_unformated,self.OutputIntervalIndices, self.OutputIntervalsamples,self.QuantizationError):
                print(f"{index_un}  {index}  {sample}  {error}")


        return "Quantization complete."

    def load_signal_data_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                lines = lines[3:]  # Skip the first 3 lines
                self.InputSignal = [float(line.split()[1]) for line in lines]
                return "Signal loaded successfully."
        except FileNotFoundError:
            return f"Error: File '{filename}' not found."
        except ValueError:
            return f"Error: Invalid data format in '{filename}'. Each line should contain a numeric value."

def choose_input_file():
    file_path = filedialog.askopenfilename(title="Select Input File")
    if file_path:
        error_message = quantization_and_encoding.load_signal_data_from_file(file_path)
        if error_message:
            quantization_result.set(error_message)

def set_num_bits_or_levels(value):
    quantization_and_encoding.num_bits_or_levels = value

def quantize_signal():
    if quantization_and_encoding.num_bits_or_levels is None:
        quantization_result.set("Please choose the number of bits or levels.")
    else:
        error_message = quantization_and_encoding.quantize_signal()
        if error_message:
            quantization_result.set(error_message)
        else:
            quantization_result.set("Quantization complete.")


# end of task 3
# --------------------------------------------------------------------------
# ----------------------------------------------------------------------------




root = tk.Tk()
root.title("DSP Tasks")

root.configure(bg='#B5E6D6')

# Create a style
style = ttk.Style()
style.configure("TButton", font=('a', 20), background='#83C8B1',)


# ----------------------------------------------------------------------------
# gui task 3
quantization_and_encoding = QuantizationAndEncoding(root)

frame = ttk.Frame(root)
frame.grid(row=0, column=0, padx=30, pady=30)

ttk.Label(frame, text="Task 3", font=("Helvetica", 20)).grid(row=0, column=0, columnspan=2)
ttk.Button(frame, text="Choose Input File", command=choose_input_file,width=30,padding=2).grid(row=1, column=0, columnspan=2)

ttk.Radiobutton(frame, text="3 Bits", variable=quantization_and_encoding.num_bits_or_levels, value=3, command=lambda: set_num_bits_or_levels(3)).grid(row=2, column=0)
ttk.Radiobutton(frame, text="4 Levels", variable=quantization_and_encoding.num_bits_or_levels, value=4, command=lambda: set_num_bits_or_levels(4)).grid(row=2, column=1)

ttk.Button(frame, text="Quantize Signal", command=quantize_signal,width=30,padding=2).grid(row=3, column=0, columnspan=2)
quantization_result = tk.StringVar()
result_label = ttk.Label(frame, textvariable=quantization_result)
result_label.grid(row=4, column=0, columnspan=2)
# -------------------------------------------------------------------------------------
root.mainloop()