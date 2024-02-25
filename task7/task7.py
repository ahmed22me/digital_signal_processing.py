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


# -----------------------------------------
# -----------------------------------------
# task 7

test1 =np.loadtxt("Test1.txt")
test2 =np.loadtxt("Test2.txt")

def Template_matching(av_class1, av_class2, test_signal):
    result1 = calc_correlation(av_class1 ,test_signal ,False)
    result2 = calc_correlation(av_class2 ,test_signal ,False)
    if (result1 > result2):
        print("test signal class 1")
    elif (result1 < result2):
        print("test signal class 2")






def avg_template_matching():
    cls1_s1 =np.loadtxt("down1.txt")
    cls1_s2 =np.loadtxt("down2.txt")
    cls1_s3 =np.loadtxt("down3.txt")
    cls1_s4 =np.loadtxt("down4.txt")
    cls1_s5 =np.loadtxt("down5.txt")
    avg_cls1 =(cls1_s1 +cls1_s2 +cls1_s3 +cls1_s4 +cls1_s5 )/5

    cls2_s1 =np.loadtxt("up1.txt")
    cls2_s2 =np.loadtxt("up2.txt")
    cls2_s3 =np.loadtxt("up3.txt")
    cls2_s4 =np.loadtxt("up4.txt")
    cls2_s5 =np.loadtxt("up5.txt")
    avg_cls2 =(cls2_s1 +cls2_s2 +cls2_s3 +cls2_s4 +cls2_s5 )/5

    return avg_cls1 ,avg_cls2


av_class1 ,av_class2 = avg_template_matching()

def read_signal_data(filename):
    list1 = []
    list2 = []

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split()
                if len(parts) == 2:
                    try:
                        value1, value2 = map(float, parts)
                        list1.append(value1)
                        list2.append(value2)
                    except ValueError:
                        print(f"Skipping invalid data in '{filename}': {line}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

    return list1, list2



x1, y1 = read_signal_data("Corr_input signal1.txt")
x2, y2 = read_signal_data("Corr_input signal2.txt")


def calc_correlation(signal1, signal2, normalized):
    sqr_signal1_sum = 0
    sqr_signal2_sum = 0

    correlation = []
    r = 0

    for i in range(len(signal1)):
        sqr_signal1_sum += signal1[i] ** 2
        sqr_signal2_sum += signal2[i] ** 2
    for j in range(len(signal1)):
        for n in range(len(signal1)):
            r += (1 / len(signal1)) * (signal1[n] * signal2[(n + j) % len(signal1)])

        if normalized:
            result = r / ((1 / len(signal1)) * (math.sqrt(sqr_signal1_sum * sqr_signal2_sum)))
            correlation.append(round(result, 8))
        else:
            correlation.append(round(r, 8))

        r = 0
    return correlation


def do_corr():
    result = calc_correlation(y1, y2, True)
    print(result)


x3, y3 = read_signal_data("TD_input signal1.txt")
x4, y4 = read_signal_data("TD_input signal2.txt")


def calc_time_delay(signal1, signal2, SF):
    delay = 0
    correlation = []
    correlation = calc_correlation(signal1, signal2, False)
    lag = correlation.index(max(correlation))
    delay = lag / SF
    print("Delay amout : ", delay)


def do_calc_time_delay():
    calc_time_delay(y3, y4, 100)

def do_test1():
    Template_matching(av_class1, av_class2, test1)

def do_test2():
    Template_matching(av_class1, av_class2, test2)


# end of task 7
# -----------------------------------------
# -----------------------------------------




root = tk.Tk()
root.title("DSP Tasks")


root.configure(bg='#B5E6D6')

# Create a style
style = ttk.Style()
style.configure("TButton", font=('a', 20), background='#83C8B1',)



# ------------------------
# gui task7

task7_frame = ttk.Frame(root)
task7_frame.grid(row=0, column=3, padx=5, pady=5)
ttk.Label(task7_frame, text="Task 7", font=("Helvetica", 20)).grid(row=0, column=0, columnspan=2)


ttk.Button(task7_frame, text="Correlation", command=do_corr, width=50, padding=2).grid(row=1, column=0)

ttk.Button(task7_frame, text="Calculate time delay", command=do_calc_time_delay, width=50, padding=2).grid(row=2, column=0)

ttk.Button(task7_frame, text="Class Test1", command=do_test1, width=50, padding=2).grid(row=3, column=0)

ttk.Button(task7_frame, text="Class Test2", command=do_test2, width=50, padding=2).grid(row=4, column=0)

# ------------------------



# Start the GUI main loop
root.mainloop()