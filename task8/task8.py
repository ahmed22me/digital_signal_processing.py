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


# ----------------------
# ---------------------
# task8

def read_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])

    with open(file_path, 'r') as file:
        lines = file.readlines()
    x = []
    y = []
    for line in lines[3:]:
        index, amplitude = map(float, line.strip().split())
        x.append(index)
        y.append(amplitude)

    return x, y


def dft(x):
    N = len(x)
    X = np.zeros(N, dtype=np.complex128)

    for k in range(N):
        # X[k] = np.round(sum(x[n] * cmath.exp(-2j * np.pi * k * n / N) for n in range(N)))
        X[k] = sum(x[n] * cmath.exp(-2j * np.pi * k * n / N) for n in range(N))

    return X


def idft(X):
    real = []
    N = len(X)
    x = np.zeros(N)

    for n in range(N):
        x[n] = np.round(sum(X[k] * cmath.exp(2j * np.pi * k * n / N) for k in range(N)).real / N)
        # x[n] = sum(X[k] * cmath.exp(2j * np.pi * k * n / N) for k in range(N)).real / N

    return x


def fast_convolution():
    indices1, samples1 = read_file()
    indices2, samples2 = read_file()

    N1 = len(samples1)
    N2 = len(samples2)

    desired_length = N1 + N2 - 1

    samples1 += [0] * (desired_length - N1)
    samples2 += [0] * (desired_length - N2)

    X1 = dft(samples1)
    X2 = dft(samples2)

    result = X1 * X2

    convolution_result = idft(result)

    ind = []

    if indices1[0] < 0 or indices2[0] < 0:
        for i in range(desired_length):
            if indices1[0] > indices2[0]:
                ind.append(i + indices2[0])
            else:
                ind.append(i + indices1[0])

    # ConvTest(ind, convolution_result)

    print(convolution_result)


def fast_correlation():
    indices1, samples1 = read_file()
    indices2, samples2 = read_file()

    X1 = dft(samples1)
    X2 = dft(samples2)

    X1_star = np.conj(X1)
    result = X1_star * X2

    correlation_result = idft(result) / len(samples1)

    print(correlation_result)


# end of task8
# ----------------------------
# ------------------------------






root = tk.Tk()
root.title("DSP Tasks")

root.configure(bg='#B5E6D6')

# Create a style
style = ttk.Style()
style.configure("TButton", font=('a', 20), background='#83C8B1',)

# ------------------------
# gui task8

task8_frame = ttk.Frame(root)
task8_frame.grid(row=1, column=3, padx=5, pady=5)
ttk.Label(task8_frame, text="Task 8", font=("Helvetica", 20)).grid(row=0, column=0, columnspan=2)


ttk.Button(task8_frame, text="Fast Convolution", command=fast_convolution, width=50, padding=2).grid(row=1, column=0)

ttk.Button(task8_frame, text="Fast Correlation", command=fast_correlation, width=50, padding=2).grid(row=2, column=0)


# ------------------------

# Start the GUI main loop
root.mainloop()