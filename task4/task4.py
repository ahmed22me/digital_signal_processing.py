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




# -----------------------------------------------------------------
# ----------------------------------------------------------------
# start of task 4


def read_signal_from_file2():
    filename = filedialog.askopenfilename(title="Select a Signal File")
    with open(filename, 'r') as file:
        lines = file.readlines()

    signal_type = int(lines[1].strip())

    samples = []

    if signal_type == 0:  # Time domain
        for line in lines[3:]:
            values = line.strip().split()
            if len(values) == 2:
                index, amplitude = values
                samples.append((float(index), float(amplitude)))
        return [sample[0] for sample in samples], [sample[1] for sample in samples]

    elif signal_type == 1:  # Frequency domain
        complex_numbers = []
        for line in lines[3:]:
            values = line.strip().split()
            if len(values) == 2:
                amplitude, phase = values
                amplitude = float(amplitude)
                phase = float(phase)
                # apply euler formoula
                real_part = amplitude * np.cos(float(phase))
                imaginary_part = amplitude * np.sin(float(phase))
                complex_number = real_part + 1j * imaginary_part
                complex_numbers.append(complex_number)
        return complex_numbers


def dft(signal, sampling_frequency):
    N = len(signal)
    frequencies = np.zeros(N)
    amplitude = np.zeros(N)
    phase = np.zeros(N)
    for k in range(N):
        frequencies[k] = 2 * np.pi * k * sampling_frequency / N
        dft_sum = 0
        for n in range(N):
            complex_exp = np.exp(-2j * np.pi * k * n / N)
            dft_sum += signal[n] * complex_exp

        amplitude[k] = np.sqrt(dft_sum.real ** 2 + dft_sum.imag ** 2)
        phase[k] = np.arctan2(dft_sum.imag, dft_sum.real)

    # Save amplitude and phase to a text file
    with open('amplitude_and_phase.txt', 'w') as file:

        file.write("0\n")
        file.write("1\n")
        file.write(f"{N}\n")
        for k in range(N):
            file.write(f"{amplitude[k]:.4f} {phase[k]:.4f}\n")
        plt.figure(figsize=(8, 4))
    plt.stem(frequencies, phase, basefmt="", label='samples')
    plt.xlabel('freq')
    plt.ylabel('phase')
    plt.legend()
    plt.grid(True)
    plt.show()

    plt.stem(frequencies, amplitude, basefmt="", label='samples')
    plt.xlabel('freq')
    plt.ylabel('amplitude')
    plt.legend()
    plt.grid(True)
    plt.show()

    return frequencies, amplitude, phase


def idft(complex_nums):
    N = len(complex_nums)
    signal = np.zeros(N, dtype=complex)

    for n in range(N):
        idft_sum = 0
        for k in range(N):
            complex_exp = np.exp(2j * np.pi * k * n / N)
            idft_sum += complex_nums[k] * complex_exp

        signal[n] = idft_sum / N
    signal = np.round(np.real(signal)).astype(int)
    plt.figure(figsize=(8, 4))
    plt.plot(signal)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('IDFT: Reconstructed Signal')
    plt.show()
    return signal


def modify_signal_components():
    with open('amplitude_and_phase.txt', 'r') as file:
        lines = file.readlines()
        Amplitude = []
        Phase = []

        samples_num = int(lines[2].strip())
    for line in lines[3:]:
        amplitude, phase = line.strip().split()
        Amplitude.append(amplitude)
        Phase.append(phase)

    def modify_amplitude():
        index = int(index_entry.get())
        new_amplitude = float(amplitude_entry.get())
        if (0 <= index < len(lines)):
            Amplitude[index] = new_amplitude

    def modify_phase():
        index = int(index_entry.get())
        new_phase = float(phase_entry.get())
        if (0 <= index < len(lines)):
            Phase[index] = new_phase

    # Create the GUI window
    root = tk.Tk()
    root.title("Modify Signal Components")

    def save_modified_components():

        with open('amplitude_and_phase.txt', 'w') as file:
            file.write("0\n")
            file.write("1\n")
            file.write(f"{samples_num}\n")
            for amb in range(len(Amplitude)):
                file.write(f"{Amplitude[amb]}")
                file.write(" ")
                file.write(f"{Phase[amb]}")
                file.write("\n")
        messagebox.showinfo("Success", "Modified components saved to file.")

    modifay_frame = ttk.Frame(root)
    modifay_frame.grid(row=0, column=0, padx=30, pady=30)

    ttk.Label(modifay_frame, text="Index:", font=("Helvetica", 10)).grid(row=0, column=0)
    index_entry = ttk.Entry(modifay_frame)
    index_entry.grid(row=0, column=1)

    ttk.Label(modifay_frame, text="New Amplitude:", font=("Helvetica", 10)).grid(row=1, column=0)
    amplitude_entry = ttk.Entry(modifay_frame)
    amplitude_entry.grid(row=1, column=1)

    ttk.Label(modifay_frame, text="New Phase (in degrees):", font=("Helvetica", 10)).grid(row=2, column=0)
    phase_entry = ttk.Entry(modifay_frame)
    phase_entry.grid(row=2, column=1)

    ttk.Button(modifay_frame, text="Modify Amplitude", command=modify_amplitude,width=30,padding=2).grid(row=3,column=0,columnspan=2)

    ttk.Button(modifay_frame, text="Modify Phase", command=modify_phase,width=30,padding=2).grid(row=4,column=0,columnspan=2)


    ttk.Button(modifay_frame, text="Save Modified Components", command=save_modified_components,width=30,padding=2).grid(row=5,column=0,columnspan=2)


    root.mainloop()


# test dft
def dft_test(freq):
    co, signal = read_signal_from_file2()
    frequencies, amp, phase = dft(signal, float(freq))  # Convert freq to float
    print(amp)
    print(phase)


# test idft
def idft_test():
    co = read_signal_from_file2()
    signal = idft(co)
    print(signal)


# end of task 4
# --------------------------------------------------
# ------------------------------------------------



root = tk.Tk()
root.title("DSP Tasks")


root.configure(bg='#B5E6D6')

# Create a style
style = ttk.Style()
style.configure("TButton", font=('a', 20), background='#83C8B1',)


# -----------------------------------------------------------------------------------
# gui task4
task4_fram = ttk.Frame(root)
task4_fram.grid(row=0, column=0, padx=30, pady=30)

ttk.Label(task4_fram, text="Task 4", font=("Helvetica", 20)).grid(row=0, column=0, columnspan=2)

ttk.Label(task4_fram, text="Enter the sampling frequency:",font=("Helvetica", 10)).grid(row=1, column=0)
sampling_freq_entry = ttk.Entry(task4_fram)
sampling_freq_entry.grid(row=1, column=1)


ttk.Button(task4_fram, text="DFT", command=lambda: dft_test(sampling_freq_entry.get()),width=30,padding=2).grid(row=2,column=0,columnspan=2)

ttk.Button(task4_fram, text="IDFT ", command=idft_test,width=30,padding=2).grid(row=3,column=0,columnspan=2)

ttk.Button(task4_fram, text="Modify", command=modify_signal_components,width=30,padding=2).grid(row=4,column=0,columnspan=2)

# ---------------------------------------------------------------------------------------




# Start the GUI main loop
root.mainloop()