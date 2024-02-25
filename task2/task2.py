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



# -------------------------------------------------------------------------
# --------------------------------------------------------------------------
# start of task2


def display_signal_continuous1(indices, samples):
    # Your existing function code
    plt.plot(indices, samples)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Continuous Signal')
    plt.show()

def display_signal_discrete1(indices, samples):
    # Your existing function code
    plt.stem(indices, samples)
    plt.xlabel('Sample Index (n)')
    plt.ylabel('Amplitude')
    plt.title('Discrete Signal')
    plt.show()



# !/usr/bin/env python
# coding: utf-8

# In[5]:


def ReadSignalFile(file_name):
    expected_indices = []
    expected_samples = []
    with open(file_name, 'r') as f:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        while line:
            # process line
            L = line.strip()
            if len(L.split(' ')) == 2:
                L = line.split(' ')
                V1 = int(L[0])
                V2 = float(L[1])
                expected_indices.append(V1)
                expected_samples.append(V2)
                line = f.readline()
            else:
                break
    return expected_indices, expected_samples


# In[6]:


def AddSignalSamplesAreEqual(userFirstSignal, userSecondSignal, Your_indices, Your_samples):
    if (userFirstSignal == 'Signal1.txt' and userSecondSignal == 'Signal2.txt'):
        file_name = "Signal1+signal2.txt"  # write here path of signal1+signal2
    elif (userFirstSignal == 'Signal1.txt' and userSecondSignal == 'Signal3.txt'):
        file_name = "signal1+signal3.txt"  # write here path of signal1+signal3
    expected_indices, expected_samples = ReadSignalFile(file_name)
    if (len(expected_samples) != len(Your_samples)) and (len(expected_indices) != len(Your_indices)):
        print("Addition Test case failed, your signal have different length from the expected one")
        return
    for i in range(len(Your_indices)):
        if (Your_indices[i] != expected_indices[i]):
            print("Addition Test case failed, your signal have different indicies from the expected one")
            return
    for i in range(len(expected_samples)):
        if abs(Your_samples[i] - expected_samples[i]) < 0.01:
            continue
        else:
            print("Addition Test case failed, your signal have different values from the expected one")
            return
    print("Addition Test case passed successfully")


# In[ ]:


def SubSignalSamplesAreEqual(userFirstSignal, userSecondSignal, Your_indices, Your_samples):
    if (userFirstSignal == 'Signal1.txt' and userSecondSignal == 'Signal2.txt'):
        file_name = "signal1-signal2.txt"  # write here path of signal1-signal2
    elif (userFirstSignal == 'Signal1.txt' and userSecondSignal == 'Signal3.txt'):
        file_name = "signal1-signal3.txt"  # write here path of signal1-signal3

    expected_indices, expected_samples = ReadSignalFile(file_name)

    if (len(expected_samples) != len(Your_samples)) and (len(expected_indices) != len(Your_indices)):
        print("Subtraction Test case failed, your signal have different length from the expected one")
        return
    for i in range(len(Your_indices)):
        if (Your_indices[i] != expected_indices[i]):
            print("Subtraction Test case failed, your signal have different indicies from the expected one")
            return
    for i in range(len(expected_samples)):
        if abs(Your_samples[i] - expected_samples[i]) < 0.01:
            continue
        else:
            print("Subtraction Test case failed, your signal have different values from the expected one")
            return
    print("Subtraction Test case passed successfully")


# In[ ]:


def NormalizeSignal(MinRange, MaxRange, Your_indices, Your_samples):
    if (MinRange == -1 and MaxRange == 1):
        file_name = "normalize of signal 1 -- output.txt"  # write here path of normalize signal 1 output.txt
    elif (MinRange == -1 and MaxRange == 1):
        file_name = "normlize signal 2 -- output.txt"  # write here path of normalize signal 2 output.txt

    expected_indices, expected_samples = ReadSignalFile(file_name)

    if (len(expected_samples) != len(Your_samples)) and (len(expected_indices) != len(Your_indices)):
        print("Normalization Test case failed, your signal have different length from the expected one")
        return
    for i in range(len(Your_indices)):
        if (Your_indices[i] != expected_indices[i]):
            print("Normalization Test case failed, your signal have different indicies from the expected one")
            return
    for i in range(len(expected_samples)):
        if abs(Your_samples[i] - expected_samples[i]) < 0.01:
            continue
        else:
            print("Normalization Test case failed, your signal have different values from the expected one")
            return
    print("Normalization Test case passed successfully")


# In[ ]:


def MultiplySignalByConst(User_Const, Your_indices, Your_samples):
    if (User_Const == 5):
        file_name = "MultiplySignalByConstant-Signal1 - by 5.txt"  # write here path of MultiplySignalByConstant-Signal1 - by 5.txt
    elif (User_Const == 10):
        file_name = "MultiplySignalByConstant-signal2 - by 10.txt"  # write here path of MultiplySignalByConstant-Signal2 - by 10.txt

    expected_indices, expected_samples = ReadSignalFile(file_name)
    if (len(expected_samples) != len(Your_samples)) and (len(expected_indices) != len(Your_indices)):
        print(
            "Multiply by " + str(User_Const) + " Test case failed, your signal have different length from the expected one")
        return
    for i in range(len(Your_indices)):
        if (Your_indices[i] != expected_indices[i]):
            print(
                "Multiply by " + str(User_Const) + " Test case failed, your signal have different indicies from the expected one")
            return
    for i in range(len(expected_samples)):
        if abs(Your_samples[i] - expected_samples[i]) < 0.01:
            continue
        else:
            print(
                "Multiply by " + str(User_Const) + " Test case failed, your signal have different values from the expected one")
            return
    print("Multiply by " + str(User_Const) + " Test case passed successfully")


# In[ ]:


def ShiftSignalByConst(Shift_value, Your_indices, Your_samples):
    if (Shift_value == 500):
        file_name = "output shifting by add 500.txt"  # write here path of output shifting by add 500.txt
    elif (Shift_value == -500):
        file_name = "output shifting by minus 500.txt"  # write here path of output shifting by minus 500.txt

    expected_indices, expected_samples = ReadSignalFile(file_name)
    if (len(expected_samples) != len(Your_samples)) and (len(expected_indices) != len(Your_indices)):
        print(
            "Shift by " + str(Shift_value) + " Test case failed, your signal have different length from the expected one")
        return
    for i in range(len(Your_indices)):
        if (Your_indices[i] != expected_indices[i]):
            print(
                "Shift by " + str(Shift_value) + " Test case failed, your signal have different indicies from the expected one")
            return
    for i in range(len(expected_samples)):
        if abs(Your_samples[i] - expected_samples[i]) < 0.01:
            continue
        else:
            print(
                "Shift by " + str(Shift_value) + " Test case failed, your signal have different values from the expected one")
            return
    print("Shift by " + str(Shift_value) + " Test case passed successfully")


# In[ ]:


# use this twice one for Accumlation and one for Squaring
# Task name when call ACC or SQU
def SignalSamplesAreEqual1(TaskName, file_name, Your_indices, Your_samples):
    expected_indices = []
    expected_samples = []
    with open(file_name, 'r') as f:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        while line:
            # process line
            L = line.strip()
            if len(L.split(' ')) == 2:
                L = line.split(' ')
                V1 = int(L[0])
                V2 = float(L[1])
                expected_indices.append(V1)
                expected_samples.append(V2)
                line = f.readline()
            else:
                break
    if (len(expected_samples) != len(Your_samples)) and (len(expected_indices) != len(Your_indices)):
        print(TaskName + " Test case failed, your signal have different length from the expected one")
    return
    for i in range(len(Your_indices)):
        if (Your_indices[i] != expected_indices[i]):
            print(TaskName + " Test case failed, your signal have different indicies from the expected one")
            return
    for i in range(len(expected_samples)):
        if abs(Your_samples[i] - expected_samples[i]) < 0.01:
            continue
        else:
            print(TaskName + " Test case failed, your signal have different values from the expected one")
            return
    print(TaskName + " Test case passed successfully")




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

def perform_addition():
    file_path1, indices1, samples1 = open_signal_file()
    file_path2, indices2, samples2 = open_signal_file()

    if file_path1 and file_path2:
        if len(samples1) == len(samples2):
            result_samples = np.array(samples1) + np.array(samples2)
            display_signal_continuous1(indices1, result_samples)

            print("Result of Addition sample1 , sample2 :")
            print(indices1)
            print(result_samples)
            AddSignalSamplesAreEqual('Signal1.txt', 'Signal2.txt', indices1, result_samples)


        else:
            print("Signal lengths are not equal; addition cannot be performed.")
    else:
        print("Signal files not selected.")




def perform_subtraction():
    file_path1, indices1, samples1 = open_signal_file()
    file_path2, indices2, samples2 = open_signal_file()

    if file_path1 and file_path2:
        if len(samples1) == len(samples2):
            result_samples = abs(np.array(samples1) - np.array(samples2))
            display_signal_continuous1(indices1, result_samples)

            print("Result of subtraction sample1 , sample2 :")
            print(indices1)
            print(result_samples)
            SubSignalSamplesAreEqual('Signal1.txt','Signal2.txt', indices1, result_samples)


        else:
            print("Signal lengths are not equal; subtraction cannot be performed.")
    else:
        print("Signal files not selected.")

def perform_multiplication():
    file_path1, indices1, samples1 = open_signal_file()
    constant_str = constant_entry.get()  # Get the constant from the input field
    try:
        constant1 = float(constant_str)
    except ValueError:
        print("Invalid constant value.")
        return
    # Perform multiplication
    if file_path1:
        result_samples = np.array(samples1) * constant1
        display_signal_continuous1(indices1, result_samples)

        print("Result of multiplication sample1 , sample2 :")
        print(indices1)
        print(result_samples)
        MultiplySignalByConst(constant1, indices1, result_samples)

    else:
        print("Signal files not selected.")


def perform_squaring():
    file_path1, indices1, samples1 = open_signal_file()

    # Perform squaring
    if file_path1:
        result_samples = np.array(samples1) ** 2
        display_signal_continuous1(indices1, result_samples)

        print("Result of squaring:")
        print(indices1)
        print(result_samples)
        SignalSamplesAreEqual1("SQU", "Output squaring signal 1.txt", indices1, result_samples)

    else:
        print("Signal files not selected.")


def perform_shifting():
    file_path1, indices1, samples1 = open_signal_file()
    shift_value_str = shift_value_entry.get()  # Get the shift value from the input field
    try:
        shift_value = int(shift_value_str)
    except ValueError:
        print("Invalid shift value.")
        return

    # Perform shifting
    if file_path1:
        result_indices1 = np.array(indices1) - shift_value
        display_signal_continuous1(result_indices1, samples1)

        print("Result of shifting:")
        print(result_indices1)
        print(samples1)
        ShiftSignalByConst(shift_value, result_indices1, samples1)

    else:
        print("Signal files not selected.")


def perform_normalization(normalize_to_zero_one):
    file_path1, indices1, samples1 = open_signal_file()

    if file_path1:
        if normalize_to_zero_one:
            result_samples1 = (np.array(samples1) - np.min(samples1)) / (np.max(samples1) - np.min(samples1))

        else:
            result_samples1 = (2 * (np.array(samples1) - np.min(samples1)) / (np.max(samples1) - np.min(samples1))) - 1

        display_signal_continuous1(indices1, result_samples1)

        print("Result of normalization:")
        print(indices1)
        print(result_samples1)
        NormalizeSignal(-1, 1, indices1, result_samples1)

    else:
        print("Signal files not selected.")



def Accumulation(input_signal):

    accumulated_signal = [0.0] * len(input_signal)
    for i in range(len(input_signal)):
        accumulated_signal[i] = accumulated_signal[i - 1] + input_signal[i]

    return accumulated_signal

def perform_accumulation():
    file_path1, indices1, samples1 = open_signal_file()

    if file_path1:
        result_samples = Accumulation(samples1)
        display_signal_continuous1(indices1, result_samples)
        print("Result of Accumulation:")
        print(indices1)
        print(result_samples)
        SignalSamplesAreEqual1('ACC', 'output accumulation for signal1.txt', indices1, result_samples)

    else:
        print("Signal files not selected.")

# end of task 2
# --------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------






root = tk.Tk()
root.title("DSP Tasks")


root.configure(bg='#B5E6D6')

# Create a style
style = ttk.Style()
style.configure("TButton", font=('a', 20), background='#83C8B1',)



# -------------------------------------------------------
# Task 2 Frame
task2_frame = ttk.Frame(root)
task2_frame.grid(row=0, column=0, padx=30, pady=30)

ttk.Label(task2_frame, text="Task 2",font=("Helvetica", 40)).grid(row=0, column=0, columnspan=3)

addition_button = ttk.Button(task2_frame, text="Perform Addition", command=perform_addition,width=30,padding=2)
addition_button.grid(row=1, column=1,columnspan=2)

subtraction_button = ttk.Button(task2_frame, text="Perform Subtraction", command=perform_subtraction,width=30,padding=2)
subtraction_button.grid(row=2, column=1,columnspan=2)

multiplication_button = ttk.Button(task2_frame, text="Perform Multiplication", command=perform_multiplication,width=30,padding=2)
multiplication_button.grid(row=3, column=1,columnspan=2)

ttk.Label(task2_frame, text="Constant of Multiplication:" , font=("Helvetica", 15)).grid(row=4, column=1)
constant_entry = ttk.Entry(task2_frame)
constant_entry.grid(row=4, column=2)

squaring_button = ttk.Button(task2_frame, text="Perform Squaring", command=perform_squaring,width=30,padding=2)
squaring_button.grid(row=5, column=1,columnspan=2)

shifting_button = ttk.Button(task2_frame, text="Perform Shifting", command=perform_shifting,width=30,padding=2)
shifting_button.grid(row=6, column=1,columnspan=2)

ttk.Label(task2_frame, text="Value of Shifting:",font=("a",15)).grid(row=7, column=1)
shift_value_entry = ttk.Entry(task2_frame)
shift_value_entry.grid(row=7, column=2)

normalizing_button1 = ttk.Button(task2_frame, text="Perform Normalization 0 to 1", command=lambda: perform_normalization(True),width=30,padding=2)
normalizing_button1.grid(row=8, column=1,columnspan=2)

normalizing_button2 = ttk.Button(task2_frame, text="Perform Normalization -1 to 1", command=lambda: perform_normalization(False),width=30,padding=2)
normalizing_button2.grid(row=9, column=1,columnspan=2)

accumulation_button = ttk.Button(task2_frame, text="Perform Accumulation", command=perform_accumulation,width=30,padding=2)
accumulation_button.grid(row=10, column=1,columnspan=2)
# ----------------------------------------------------------------------------

# Start the GUI main loop
root.mainloop()