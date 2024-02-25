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




# ------------------------------------------
# --------------------------------------------
# task 6

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


def read_signal_from_file(file_path):
    indices, samples = [], []
    with open(file_path, 'r') as f:
        for _ in range(3):  # Skip the first three lines
            f.readline()
        for line in f:
            values = line.strip().split()
            if len(values) == 2:
                indices.append(int(values[0]))
                samples.append(float(values[1]))
    return indices, samples


def open_signal_file():
    file_path = filedialog.askopenfilename(title="Select a Signal File")
    if file_path:
        indices, samples = read_signal_from_file(file_path)

        return file_path, indices, samples
    return None, None, None


def apply_operation(operation):
    signal = read_signal_from_file_task5()
    result = operation(signal)

    # Display the result
    plt.figure(figsize=(8, 4))
    plt.plot(result)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('Result of Operation')
    plt.show()




# Function to compute moving average
def moving_average(window_size):
    filepath , indeses , samples = open_signal_file()
    window_size = int(window_size)
    result = np.zeros(len(samples) - window_size + 1)
    for i in range(len(result)):
        result[i] = np.sum(samples[i:i+window_size]) / window_size

    # SignalSamplesAreEqual("OutMovAvgTest1.txt",indeses,result)
    #SignalSamplesAreEqual("OutMovAvgTest2.txt",indeses,result)

    return result


def DerivativeSignal():
    InputSignal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                   28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
                   53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77,
                   78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    expectedOutput_first = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                            1, 1, 1, 1, 1, 1]
    expectedOutput_second = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                             0, 0, 0, 0, 0, 0, 0, 0]

    """
    Write your Code here:
    Start
    """
    import numpy as np
    def first_derivative(signal):
        result = np.zeros(len(signal) - 1)
        for i in range(len(result)):
            result[i] = signal[i + 1] - signal[i]
        return result

    # Function to compute second derivative
    def second_derivative(signal):
        result = np.zeros(len(signal) - 2)
        for i in range(len(result)):
            result[i] = signal[i + 2] - 2 * signal[i + 1] + signal[i]
        return result

    FirstDrev = first_derivative(InputSignal)
    SecondDrev = second_derivative(InputSignal)

    """
    End
    """

    """
    Testing your Code
    """
    if ((len(FirstDrev) != len(expectedOutput_first)) or (len(SecondDrev) != len(expectedOutput_second))):
        print("mismatch in length")
        return
    first = second = True
    for i in range(len(expectedOutput_first)):
        if abs(FirstDrev[i] - expectedOutput_first[i]) < 0.01:
            continue
        else:
            first = False
            print("1st derivative wrong")
            return
    for i in range(len(expectedOutput_second)):
        if abs(SecondDrev[i] - expectedOutput_second[i]) < 0.01:
            continue
        else:
            second = False
            print("2nd derivative wrong")
            return
    if (first and second):
        print("Derivative Test case passed successfully")
    else:
        print("Derivative Test case failed")
    return

# Function to compute first derivative
def first_derivative(signal):
    result = np.zeros(len(signal) - 1)
    for i in range(len(result)):
        result[i] = signal[i+1] - signal[i]
    DerivativeSignal()
    return result


# Function to compute second derivative
def second_derivative(signal):
    result = np.zeros(len(signal) - 2)
    for i in range(len(result)):
        result[i] = signal[i+2] - 2 * signal[i+1] + signal[i]

    DerivativeSignal()

    return result



def Shift_Fold_Signal(file_name,Your_indices,Your_samples):
    expected_indices=[]
    expected_samples=[]
    with open(file_name, 'r') as f:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        while line:
            # process line
            L=line.strip()
            if len(L.split(' '))==2:
                L=line.split(' ')
                V1=int(L[0])
                V2=float(L[1])
                expected_indices.append(V1)
                expected_samples.append(V2)
                line = f.readline()
            else:
                break
    print("Current Output Test file is: ")
    print(file_name)
    print("\n")
    if (len(expected_samples)!=len(Your_samples)) and (len(expected_indices)!=len(Your_indices)):
        print("Shift_Fold_Signal Test case failed, your signal have different length from the expected one")
        return
    for i in range(len(Your_indices)):
        if(Your_indices[i]!=expected_indices[i]):
            print("Shift_Fold_Signal Test case failed, your signal have different indicies from the expected one")
            return
    for i in range(len(expected_samples)):
        if abs(Your_samples[i] - expected_samples[i]) < 0.01:
            continue
        else:
            print("Shift_Fold_Signal Test case failed, your signal have different values from the expected one")
            return
    print("Shift_Fold_Signal Test case passed successfully")

def delay_advance_signal(k):
    filepath, indeses, samples = open_signal_file()

    k = int(k)
    shifted_signal = [k + indeses for indeses in indeses]
    return shifted_signal


# Function to fold a signal without using np.flip
def fold_signal():
    filepath , indeses , samples = open_signal_file()
    length = len(samples)
    result = [0] * length

    for i in range(length):
        result[i] = samples[length - 1 - i]
    print(result)
    print(indeses)
    return result



def delay_advance_folded_signal(k):
    filepath , indeses , samples = open_signal_file()

    k = int(k)

    length = len(samples)
    result = [0] * length

    for i in range(length):
        result[i] = samples[length - 1 - i]

    shifted_signal = [k + indeses for indeses in indeses]

    Shift_Fold_Signal("Output_ShifFoldedby500.txt",shifted_signal,result)
    #Shift_Fold_Signal("Output_ShiftFoldedby-500.txt",shifted_signal,result)


    return shifted_signal


def DFT(signal):
    signal_length = len(signal)
    amplitude_spectrum = np.zeros(signal_length)
    phase_spectrum = np.zeros(signal_length)
    for k in range(signal_length):
        exponential = sum(signal * np.exp(-1j * 2 * np.pi * k * np.arange(signal_length) / signal_length))
        amplitude_spectrum[k] = np.sqrt(np.real(exponential) ** 2 + np.imag(exponential) ** 2)
        phase_spectrum[k] = np.arctan2(exponential.imag, exponential.real)
    return amplitude_spectrum, phase_spectrum


def Idft(amplitude, phase):
    N = len(amplitude)
    t = np.arange(N)
    real_signal = np.zeros(N)
    imag_signal = np.zeros(N)
    for k in range(N):
        complex_exp = amplitude[k] * np.exp(1j * (2 * np.pi * k * t / N + phase[k]))
        real_signal += complex_exp.real
        imag_signal += complex_exp.imag
    complex_signal = real_signal + 1j * imag_signal
    complex_signal /= N
    return complex_signal.real


def remove_dc_frequency_domain(signal):
    amplitude, phase = DFT(signal)
    amplitude[0] = 0
    dc_removed_signal = Idft(amplitude, phase)
    dc_removed_signal_rounded = np.round(dc_removed_signal, 3)
    return dc_removed_signal_rounded

# # Function to remove DC component in frequency domain
# def remove_dc_frequency_domain(signal):
#     frequencies, amp, phase = dft(signal, 1.0)  # Assuming a sampling frequency of 1.0
#     amp[0] = 0  # Set DC component to zero
#     return idft(amp)


# Function to convolve two signals


def ConvTest(Your_indices, Your_samples):
    """
    Test inputs
    InputIndicesSignal1 =[-2, -1, 0, 1]
    InputSamplesSignal1 = [1, 2, 1, 1 ]

    InputIndicesSignal2=[0, 1, 2, 3, 4, 5 ]
    InputSamplesSignal2 = [ 1, -1, 0, 0, 1, 1 ]
    """
    expected_indices = [-2, -1, 0, 1, 2, 3, 4, 5, 6]
    expected_samples = [1, 1, -1, 0, 0, 3, 3, 2, 1]

    if (len(expected_samples) != len(Your_samples)) and (len(expected_indices) != len(Your_indices)):
        print("Conv Test case failed, your signal have different length from the expected one")
        return
    for i in range(len(Your_indices)):
        if (Your_indices[i] != expected_indices[i]):
            print("Conv Test case failed, your signal have different indicies from the expected one")
            return
    for i in range(len(expected_samples)):
        if abs(Your_samples[i] - expected_samples[i]) < 0.01:
            continue
        else:
            print("Conv Test case failed, your signal have different values from the expected one")
            return
    print("Conv Test case passed successfully")

def convolve_signals():
    filepath1 , indeses1 , samples1 = open_signal_file()
    filepath2 , indeses2 , samples2 = open_signal_file()

    newsamples = np.zeros(len(samples1) + len(samples2) - 1)
    for i in range(len(samples1)):
        for j in range(len(samples2)):
            newsamples[i+j] += samples1[i] * samples2[j]


    newindeses = []

    current_index = indeses1[0]

    while len(newindeses) < len(newsamples):
        newindeses.append(current_index)
        current_index += 1

    ConvTest(newindeses,newsamples)


    return newsamples



# end of task 6
# -----------------------------------------------
# -----------------------------------------------




root = tk.Tk()
root.title("DSP Tasks")


root.configure(bg='#B5E6D6')

# Create a style
style = ttk.Style()
style.configure("TButton", font=('a', 20), background='#83C8B1',)



# -----------------------------
# gui task 6
task6_frame = ttk.Frame(root)
task6_frame.grid(row=1, column=2, padx=5, pady=5)
ttk.Label(task6_frame, text="Task 6", font=("Helvetica", 20)).grid(row=0, column=0, columnspan=2)

ttk.Label(task6_frame, text="number of points for smoothing:", font=("Helvetica", 15)).grid(row=1, column=0)
smoothing_points = ttk.Entry(task6_frame)
smoothing_points.grid(row=1, column=1)

ttk.Button(task6_frame, text="Compute moving average", command=lambda: moving_average(smoothing_points.get()), width=50, padding=2).grid(row=2, column=0)

ttk.Button(task6_frame, text="First Derivative of signal", command=lambda: apply_operation(lambda signal: first_derivative(signal)), width=50, padding=2).grid(row=3, column=0)
ttk.Button(task6_frame, text="Second Derivative of signal", command=lambda: apply_operation(lambda signal: second_derivative(signal)), width=50, padding=2).grid(row=4, column=0)

ttk.Label(task6_frame, text="number of steps:", font=("Helvetica", 15)).grid(row=5, column=0)
steps = ttk.Entry(task6_frame)
steps.grid(row=5, column=1)
ttk.Button(task6_frame, text="Delay/Advance Signal", command=lambda: delay_advance_signal( steps.get()), width=50, padding=2).grid(row=6, column=0)
ttk.Button(task6_frame, text="Folding a signal", command= fold_signal, width=50, padding=2).grid(row=7, column=0)

ttk.Button(task6_frame, text="Delay/Advance Folded Signal", command=lambda:  delay_advance_folded_signal(steps.get()), width=50, padding=2).grid(row=8, column=0)

ttk.Button(task6_frame, text="Remove DC Component (Frequency Domain)", command=lambda: apply_operation(lambda signal: remove_dc_frequency_domain(signal)), width=50, padding=2).grid(row=9, column=0)

ttk.Button(task6_frame, text="Convolve two signals", command=convolve_signals, width=50, padding=2).grid(row=10, column=0)

# ---------------------------





# Start the GUI main loop
root.mainloop()