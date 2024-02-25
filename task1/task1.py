import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk



# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
# start of task1

def SignalSamplesAreEqual(file_name, indices, samples):
    # Your existing function code
    expected_indices = []
    expected_samples = []
    with open(file_name, 'r') as f:
        for _ in range(3):  # Skip the first three lines
            f.readline()
        for line in f:
            L = line.strip().split(' ')
            if len(L) < 2:
                print("Invalid line format in the file:", line)
                continue
            V1 = int(L[0])
            V2 = float(L[1])
            expected_indices.append(V1)
            expected_samples.append(V2)

    if len(expected_samples) != len(samples):
        print("Test case failed, your signal has a different length from the expected one")
        return False
    for i in range(len(expected_samples)):
        if abs(samples[i] - expected_samples[i]) < 0.01:
            continue
        else:
            print("Test case failed, your signal has different values from the expected one")
            return False
    print("Test case passed successfully")
    return True


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


def display_signal_continuous(ax, indices, samples):
    # Your existing function code
    ax.plot(indices, samples)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Amplitude')
    ax.set_title('Continuous Signal')

def display_signal_discrete(ax, indices, samples):
    # Your existing function code
    ax.stem(indices, samples)
    ax.set_xlabel('Sample Index (n)')
    ax.set_ylabel('Amplitude')
    ax.set_title('Discrete Signal')

def generate_signal(wave_type, amplitude, phase_shift, analog_frequency, sampling_frequency, duration=1.0):
    # Your existing function code
    if wave_type == 'sin':
        t = np.arange(0, duration, 1 / sampling_frequency)
        signal = amplitude * np.sin(2 * np.pi * analog_frequency * t + phase_shift)
    elif wave_type == 'cos':
        t = np.arange(0, duration, 1 / sampling_frequency)
        signal = amplitude * np.cos(2 * np.pi * analog_frequency * t + phase_shift)
    else:
        print("Invalid wave type. Please choose either 'sin' or 'cos'.")
        return None

    indices = np.arange(len(signal))
    return indices, signal

def generate_and_display_sine_wave():
    # Function to handle sine wave generation and display
    amplitude = float(amp_entry.get())
    phase_shift = float(phase_shift_entry.get())
    analog_frequency = float(analog_freq_entry.get())
    sampling_frequency = float(sampling_freq_entry.get())
    indices, signal = generate_signal('sin', amplitude, phase_shift, analog_frequency, sampling_frequency)
    display_signal_continuous1(indices,signal)
    display_signal_discrete1(indices, signal)

def generate_and_display_cosine_wave():
    # Function to handle cosine wave generation and display
    amplitude = float(amp_entry.get())
    phase_shift = float(phase_shift_entry.get())
    analog_frequency = float(analog_freq_entry.get())
    sampling_frequency = float(sampling_freq_entry.get())
    indices, signal = generate_signal('cos', amplitude, phase_shift, analog_frequency, sampling_frequency)
    display_signal_continuous1(indices, signal)
    display_signal_discrete1(indices, signal)


def read_and_display_signal_samples():
    file_path = "signal.txt"  # Specify the file name "signal1.txt"
    indices, samples = [], []
    with open(file_path, 'r') as f:
        for _ in range(3):  # Skip the first three lines
            f.readline()
        for line in f:
            values = line.strip().split()
            if len(values) == 2:
                indices.append(int(values[0]))
                samples.append(float(values[1]))

    # Create subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

    # Display continuous and discrete plots on subplots
    display_signal_continuous(ax1, indices, samples)
    display_signal_discrete(ax2, indices, samples)

    SignalSamplesAreEqual(file_path, indices, samples)

    plt.show()

# end of task1
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------

root = tk.Tk()
root.title("DSP Tasks")

root.configure(bg='#B5E6D6')

# Create a style
style = ttk.Style()
style.configure("TButton", font=('a', 20), background='#83C8B1',)



# -----------------------------------------------------
# Task 1 Frame
task1_frame = ttk.Frame(root)
task1_frame.grid(row=0, column=0, padx=40, pady=40)

ttk.Label(task1_frame, text="Task 1",font=("Helvetica", 30)).grid(row=0, column=0, columnspan=2)

ttk.Label(task1_frame, text="Amplitude (A):",font=("Helvetica", 20)).grid(row=1, column=0)
amp_entry = ttk.Entry(task1_frame)
amp_entry.grid(row=1, column=1)

ttk.Label(task1_frame, text="Phase Shift (radians):",font=("Helvetica", 20)).grid(row=2, column=0)
phase_shift_entry = ttk.Entry(task1_frame)
phase_shift_entry.grid(row=2, column=1)

ttk.Label(task1_frame, text="Analog Frequency (Hz):",font=("Helvetica", 20)).grid(row=3, column=0)
analog_freq_entry = ttk.Entry(task1_frame)
analog_freq_entry.grid(row=3, column=1)

ttk.Label(task1_frame, text="Sampling Frequency (Hz):",font=("Helvetica", 20)).grid(row=4, column=0)
sampling_freq_entry = ttk.Entry(task1_frame)
sampling_freq_entry.grid(row=4, column=1)

sine_button = ttk.Button(task1_frame, text="Generate and Display Sine Wave", command=generate_and_display_sine_wave,width=40,padding=2)
sine_button.grid(row=5, column=0, columnspan=2)

cosine_button = ttk.Button(task1_frame, text="Generate and Display Cosine Wave", command=generate_and_display_cosine_wave,width=40,padding=2)
cosine_button.grid(row=6, column=0, columnspan=2)

read_button = ttk.Button(task1_frame, text="Read and Display Signal Samples", command=read_and_display_signal_samples,width=40,padding=2)
read_button.grid(row=7, column=0, columnspan=2)


# Start the GUI main loop
root.mainloop()
