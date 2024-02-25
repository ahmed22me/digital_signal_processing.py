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



# --------------------------------------------
# --------------------------------------------
# task 5


# Function to read signal from a file
def read_signal_from_file_task5():
    filename = filedialog.askopenfilename(title="Select a Signal File")
    with open(filename, 'r') as file:
        lines = file.readlines()

    signal_type = int(lines[1].strip())
    samples = []

    if signal_type == 0:
        for line in lines[3:]:
            values = line.strip().split()
            if len(values) == 2:
                index, amplitude = values
                samples.append((float(index), float(amplitude)))
        return [sample[1] for sample in samples]  # Returning only amplitudes

    elif signal_type == 1:
        complex_numbers = []
        for line in lines[3:]:
            values = line.strip().split()
            if len(values) == 2:
                amplitude, phase = values
                amplitude, phase = float(amplitude), float(phase)
                real_part = amplitude * np.cos(phase)
                imaginary_part = amplitude * np.sin(phase)
                complex_number = real_part + 1j * imaginary_part
                complex_numbers.append(complex_number)
        return complex_numbers
    else:
        raise ValueError("Unsupported signal type")



# Function to perform Discrete Cosine Transform (DCT)
def dct(signal):
    N = len(signal)
    dct_result = np.zeros(N, dtype=np.float64)  # Ensure the result array has a specific data type

    for k in range(N):
        dct_sum = 0
        for n in range(N):
            # Check if the element in the signal array is numerical
            if isinstance(signal[n], (int, float, np.integer, np.floating)):
                dct_sum += signal[n] * np.cos(np.pi / (4 * N) * (2 * n - 1) * (2 * k - 1))
            else:
                raise TypeError("Input signal must contain numerical elements.")

        dct_result[k] = np.sqrt(2 / N) * dct_sum

    print(dct_result)

    return dct_result

# Function to compute DCT, display the result, and save selected coefficients
def compute_dct_and_save_coefficients(signal_samples):
    dct_result = dct(signal_samples)

    # Display DCT result
    plt.figure(figsize=(8, 4))
    plt.stem(dct_result, basefmt="", label='samples')
    plt.xlabel('DCT Coefficients')
    plt.ylabel('Amplitude')
    plt.title('DCT Result')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Ask the user to choose the number of coefficients to save
    num_coefficients = simpledialog.askinteger("Input", "Enter the number of coefficients to save:", parent=root)

    if num_coefficients is not None:
        # Save selected coefficients to a text file
        with open('selected_dct_coefficients.txt', 'w') as file:
            for i in range(num_coefficients):
                file.write(f"{dct_result[i]:.4f}\n")
        messagebox.showinfo("Success", f"{num_coefficients} DCT coefficients saved to file.")

# Function to remove DC component from the time domain signal
def remove_dc_component(time_signal):
    mean_value = np.mean(time_signal)
    dc_removed_signal = time_signal - mean_value

    print(dc_removed_signal)

    return dc_removed_signal


# Add a function to plot the DC-removed signal
def remove_dc_and_plot(signal):
    dc_removed_signal = remove_dc_component(signal)

    # Display the DC-removed signal
    plt.figure(figsize=(8, 4))
    plt.plot(dc_removed_signal)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('DC-Removed Signal')
    plt.show()



# end of task 5
# ------------------------------------------
# ---------------------------------------





root = tk.Tk()
root.title("DSP Tasks")


root.configure(bg='#B5E6D6')

# Create a style
style = ttk.Style()
style.configure("TButton", font=('a', 20), background='#83C8B1',)


# ---------------------------------------------------------------------------------------
# gui task 5

task5_frame = ttk.Frame(root)
task5_frame.grid(row=0, column=2, padx=5, pady=5)
ttk.Label(task5_frame, text="Task 5", font=("Helvetica", 20)).grid(row=0, column=0, columnspan=2)

ttk.Button(task5_frame, text="Compute DCT", command=lambda: compute_dct_and_save_coefficients(read_signal_from_file_task5()),width=30,padding=2).grid(row=2,column=0,columnspan=2)

ttk.Button(task5_frame, text="Remove DC Component ", command=lambda:remove_dc_and_plot(read_signal_from_file_task5()),width=30,padding=2).grid(row=3,column=0,columnspan=2)

# ----------------------------------------------------------------------------------------




# Start the GUI main loop
root.mainloop()