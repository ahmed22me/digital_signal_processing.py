import numpy as np
import tkinter as tk
from CompareSignal import Compare_Signals

def conv(x, y, x1, y1):
    conv_length = len(y) + len(y1) - 1
    y = np.pad(y, (0, conv_length - len(y)), 'constant')
    y1 = np.pad(y1, (0, conv_length - len(y1)), 'constant')
    complexreal, compleximag, complexreal1, compleximag1 = [], [], [], []
    for n in range(conv_length):
        real = 0.0
        imag = 0.0
        for k in range(conv_length):
            amplitude = y[k]
            phase = np.pi * 2 * n * k / conv_length
            real += amplitude * np.cos(phase)
            imag += (-amplitude * np.sin(phase))
        complexreal.append(real)
        compleximag.append(imag)

    for n in range(conv_length):
        real = 0.0
        imag = 0.0
        for k in range(conv_length):
            amplitude = y1[k]
            phase = np.pi * 2 * n * k / conv_length
            real += amplitude * np.cos(phase)
            imag += (-amplitude * np.sin(phase))
        complexreal1.append(real)
        compleximag1.append(imag)

    indices = []
    min_n = int(np.min(x) + np.min(x1))
    max_n = int(np.max(x) + np.max(x1))
    con = min_n
    for i in range(conv_length):
        indices.append(con)
        con += 1

    arr, arrr, res = [], [], []
    for i in range(conv_length):
        arr.append(complex(complexreal[i], compleximag[i]))
        arrr.append(complex(complexreal1[i], compleximag1[i]))

    for i in range(conv_length):
        res.append(arr[i] * arrr[i])

    xn = np.fft.ifft(res)
    xn_real = np.real(xn)
    return indices, xn_real
def ReadingFile(file_path):
    file = open(file_path, "r")
    signal_data = file.readlines()
    ignored_lines = signal_data[3:]
    x0, y0 = [], []
    for l in ignored_lines:
        row = l.split()
        x0.append(float(row[0]))
        y0.append(float(row[1]))
    return x0, y0


def SetSpecificationsFilters(FileName):
    global FilterType, FS, StopBandAttenuation, FC, F1, F2, TransitionBand
    FilterType = 0
    FS = 0
    StopBandAttenuation = 0
    FC = 0
    F1 = 0
    F2 = 0
    TransitionBand = 0

    file = open(FileName, "r", encoding='utf-8')
    lines1 = file.readlines()
    file.close()

    x = []
    y = 0

    ignored_lines = lines1[1:]
    for l in ignored_lines:
        row = l.split()
        x.append(float(row[2]))

    for l in lines1:
        row = l.split()
        y = (row[2] + row[3])
        break

    if y == "Lowpass":
        FilterType = 1
    elif y == "Highpass":
        FilterType = 2
    elif y == "Bandpass":
        FilterType = 3
    elif y == "Bandstop":
        FilterType = 4

    if len(x) == 4:
        FS, StopBandAttenuation, FC, TransitionBand = x
    elif len(x) == 5:
        FS, StopBandAttenuation, F1, F2, TransitionBand = x
    return FilterType, FS, StopBandAttenuation, FC, F1, F2, TransitionBand


def CheckNOddOrEven(N):
    if (np.fmod(N, 2) == 1):
        return int(N)
    elif (np.fmod(N, 2) == 0 or (np.fmod(N, 2)) < 1):
        return int(N) + 1
    elif ((np.fmod(N, 2)) > 1):
        return int(N) + 2


def CalculateFC_new(Type, TransitionBand, FS, Fc=None, FC1=None, FC2=None):
    if (Type == 1):

        FC_Low_New = (Fc + (TransitionBand / 2)) / FS
        return FC_Low_New
    elif (Type == 2):

        FC_High_New = (Fc - (TransitionBand / 2)) / FS
        return FC_High_New
    elif (Type == 3):

        FC1_New = (FC1 - (TransitionBand / 2)) / FS
        FC2_New = (FC2 + (TransitionBand / 2)) / FS
        return FC1_New, FC2_New
    elif (Type == 4):

        FC1_New = (FC1 + (TransitionBand / 2)) / FS
        FC2_New = (FC2 - (TransitionBand / 2)) / FS
        return FC1_New, FC2_New


def No(StopBandAttenuation, TransitionBand, FS):
    if (StopBandAttenuation <= 21):
        N = 0.9 * FS / TransitionBand
    elif (StopBandAttenuation > 21 and StopBandAttenuation <= 44):
        N = 3.1 * FS / TransitionBand
    elif (StopBandAttenuation > 44 and StopBandAttenuation <= 53):
        N = 3.3 * FS / TransitionBand
    elif (StopBandAttenuation > 53 and StopBandAttenuation <= 74):
        N = 5.5 * FS / TransitionBand
    N_new = CheckNOddOrEven(N)
    return N_new


def Wn(StopBandAttenuation, N, n):
    if (StopBandAttenuation <= 21):
        return 1
    elif (StopBandAttenuation > 21 and StopBandAttenuation <= 44):
        eq = 0.5 + 0.5 * np.cos((2 * np.pi * n) / N)
        return eq
    elif (StopBandAttenuation > 44 and StopBandAttenuation <= 53):
        eq = 0.54 + 0.46 * np.cos((2 * np.pi * n) / N)
        return eq
    elif (StopBandAttenuation > 53 and StopBandAttenuation <= 74):
        eq = 0.42 + 0.5 * np.cos((2 * np.pi * n) / (N - 1)) + 0.08 * np.cos((4 * np.pi * n) / (N - 1))
        return eq


def CalculateWindowFunction(StopBandAttenuation, TransitionBand, FS, Index):
    N = No(StopBandAttenuation, TransitionBand, FS)
    n = - int(N / 2)
    wn = []
    for i in range(N):
        wn.append(Wn(StopBandAttenuation, N, n))
        Index.append(n)
        n = n + 1
    return wn


def Hn(FilterType, n, TransitionBand, FS, FC, F1, F2):
    if (FilterType == 1):
        if (n == 0):
            eq = 2 * CalculateFC_new(FilterType, TransitionBand, FS, Fc=FC)
            return eq
        else:
            f = CalculateFC_new(FilterType, TransitionBand, FS, Fc=FC)
            eq = 2 * f * np.sin(n * 2 * np.pi * f) / (n * 2 * np.pi * f)
            return eq

    elif (FilterType == 2):
        if (n == 0):
            eq = 1 - 2 * CalculateFC_new(FilterType, TransitionBand, FS, Fc=FC)
            return eq
        else:
            f = CalculateFC_new(FilterType, TransitionBand, FS, Fc=FC)
            eq = - 2 * f * np.sin(n * 2 * np.pi * f) / (n * 2 * np.pi * f)
            return eq
    elif (FilterType == 3):
        if (n == 0):
            f1, f2 = CalculateFC_new(FilterType, TransitionBand, FS, FC1=F1, FC2=F2)
            eq = 2 * (f2 - f1)
            return eq
        else:
            f1, f2 = CalculateFC_new(FilterType, TransitionBand, FS, FC1=F1, FC2=F2)
            eq = (2 * f2 * np.sin(n * 2 * np.pi * f2) / (n * 2 * np.pi * f2)) - (
                        2 * f1 * np.sin(n * 2 * np.pi * f1) / (n * 2 * np.pi * f1))
            return eq
    elif (FilterType == 4):
        if (n == 0):
            f1, f2 = CalculateFC_new(FilterType, TransitionBand, FS, FC1=F1, FC2=F2)
            eq = 1 - 2 * (f2 - f1)
            return eq
        else:
            f1, f2 = CalculateFC_new(FilterType, TransitionBand, FS, FC1=F1, FC2=F2)
            eq = (2 * f1 * np.sin(n * 2 * np.pi * f1) / (n * 2 * np.pi * f1)) - (
                        2 * f2 * np.sin(n * 2 * np.pi * f2) / (n * 2 * np.pi * f2))
            return eq


def CalculateFilter(FilterType, StopBandAttenuation, TransitionBand, FS, FC, F1, F2):
    N = No(StopBandAttenuation, TransitionBand, FS)
    n = -int(N / 2)
    hn = []
    for i in range(N):
        hn.append(Hn(FilterType, n, TransitionBand, FS, FC, F1, F2))
        n = n + 1
    return hn


def FIR(FilterType, StopBandAttenuation, TransitionBand, FS, FC, F1, F2):
    Index = []
    wn = CalculateWindowFunction(StopBandAttenuation, TransitionBand, FS, Index)
    hn = CalculateFilter(FilterType, StopBandAttenuation, TransitionBand, FS, FC, F1, F2)
    h = []
    N = No(StopBandAttenuation, TransitionBand, FS)
    for i in range(N):
        h.append(wn[i] * hn[i])
    return h, Index


def Testcases(testcase_entry):
    TestCase_no = int(testcase_entry.get())

    if TestCase_no == 1:
        # TestCase1
        SetSpecificationsFilters("Filter Specifications.txt")
        LowPass, Index = FIR(FilterType, StopBandAttenuation, TransitionBand, FS, FC, F1, F2)
        Compare_Signals("LPFCoefficients.txt", Index, LowPass)
    elif TestCase_no == 2:

        # TestCase2
        SetSpecificationsFilters("Filter Specifications.txt")
        LowPass0, Index0 = FIR(FilterType, StopBandAttenuation, TransitionBand, FS, FC, F1, F2)
        x0, y0 = ReadingFile("ecg400.txt")
        output = conv(x0, y0, Index0, LowPass0)
        outputx, outputy = output
        Compare_Signals("ecg_low_pass_filtered.txt", outputx, outputy)
    elif TestCase_no == 3:
        # TestCase3
        SetSpecificationsFilters("Filter Specifications.txt")
        HighPass, Index = FIR(FilterType, StopBandAttenuation, TransitionBand, FS, FC, F1, F2)
        Compare_Signals("HPFCoefficientshigh.txt", Index, HighPass)
    elif TestCase_no == 4:
        # TestCase4
        SetSpecificationsFilters("Filter Specifications.txt")
        HighPass, Index0 = FIR(FilterType, StopBandAttenuation, TransitionBand, FS, FC, F1, F2)
        x0, y0 = ReadingFile("ecg400.txt")
        output = conv(x0, y0, Index0, HighPass)
        outputx, outputy = output
        Compare_Signals("ecg_high_pass_filtered.txt", outputx, outputy)
    elif TestCase_no == 5:
        # TestCase5
        SetSpecificationsFilters("Filter Specifications.txt")
        BandPass, Index = FIR(FilterType, StopBandAttenuation, TransitionBand, FS, FC, F1, F2)
        Compare_Signals("BPFCoefficients.txt", Index, BandPass)
    elif TestCase_no == 6:
        # TestCase6
        SetSpecificationsFilters("Filter Specifications.txt")
        BandPass, Index0 = FIR(FilterType, StopBandAttenuation, TransitionBand, FS, FC, F1, F2)
        x0, y0 = ReadingFile("ecg400.txt")
        output = conv(x0, y0, Index0, BandPass)
        outputx, outputy = output
        Compare_Signals("ecg_band_pass_filtered.txt", outputx, outputy)
    elif TestCase_no == 7:
        # TestCase7
        SetSpecificationsFilters("Filter Specifications.txt")
        BandStop, Index = FIR(FilterType, StopBandAttenuation, TransitionBand, FS, FC, F1, F2)
        Compare_Signals("BSFCoefficients.txt", Index, BandStop)
    elif TestCase_no == 8:
        # TestCase8
        SetSpecificationsFilters("Filter Specifications.txt")
        BandStop, Index0 = FIR(FilterType, StopBandAttenuation, TransitionBand, FS, FC, F1, F2)
        x0, y0 = ReadingFile("ecg400.txt")
        output = conv(x0, y0, Index0, BandStop)
        outputx, outputy = output
        Compare_Signals("ecg_band_stop_filtered.txt", outputx, outputy)


def Resampling(m_entry, l_entry):
    file_path = "ecg400.txt"
    file = open(file_path, "r")
    signal_data = file.readlines()
    ignored_lines = signal_data[3:]
    x, y = [], []
    for l in ignored_lines:
        row = l.split()
        x.append(float(row[0]))
        y.append(float(row[1]))

    FilterType, FS, StopBandAttenuation, FC, F1, F2, TransitionBand = SetSpecificationsFilters(
        "Filter Specifications.txt")

    LowPass, Index = FIR(FilterType, StopBandAttenuation, TransitionBand, FS, FC, F1, F2)

    M = int(m_entry.get())
    L = int(l_entry.get())

    import math

    if M == 0 and L != 0:
        output, outputx, outputy = [], [], []
        y_upsampled, x_upsampled = [], []
        for i in range(len(y) - 1):
            y_upsampled.append(y[i])
            for j in range(L - 1):
                y_upsampled.append(0)
            for j in range(L):
                x_upsampled.append(x[i] + ((x[i + 1] - x[i]) / L) * j)

        y_upsampled.append(y[-1])
        x_upsampled.append(x[-1])

        output = conv(x_upsampled, y_upsampled, Index, LowPass)
        outputx, outputy = output

        Compare_Signals("Sampling_Up.txt", outputx, outputy)
    elif M != 0 and L == 0:
        output, outputx, outputy = [], [], []
        output = conv(x, y, Index, LowPass)
        outputx, outputy = output

        y_downsampled, x_downsampled = [], []
        y_downsampled = outputy[::M]
        for i in range(len(y_downsampled)):
            x_downsampled.append(outputx[i])
        Compare_Signals("Sampling_Down.txt", x_downsampled, y_downsampled)
    elif M != 0 and L != 0:
        output, outputx, outputy = [], [], []
        y_upsampled, x_upsampled = [], []
        for i in range(len(y) - 1):
            y_upsampled.append(y[i])
            for j in range(L - 1):
                y_upsampled.append(0)
            for j in range(L):
                x_upsampled.append(x[i] + ((x[i + 1] - x[i]) / L) * j)

        y_upsampled.append(y[-1])
        x_upsampled.append(x[-1])

        output = conv(x_upsampled, y_upsampled, Index, LowPass)
        outputx, outputy = output

        # Adjust the length of outputx and outputy to match the desired downsampling ratio
        target_length = len(outputx) // M * M  # Find the largest length divisible by M
        outputx = outputx[:target_length]
        outputy = outputy[:target_length]

        y_downsampled, x_downsampled = [], []
        for i in range(0, len(outputy), M):
            y_downsampled.append(outputy[i])
            x_downsampled.append(outputx[i])

        Compare_Signals("Sampling_Up_Down.txt", x_downsampled, y_downsampled)
    else:
        print("Error!!!!!!!")


def open_window1():
    window1 = tk.Tk()
    window1.title("Practical Task")
    window1.geometry('500x400')

    label1 = tk.Label(window1, text="Tasks Window", height=5, width=20)
    label1.pack()

    button1 = tk.Button(window1, text="Task1", height=5, width=20, command=Task1_window)
    button1.pack()

    window1.mainloop()


def Task1_window():
    window2 = tk.Tk()
    window2.title("Task1 window")
    window2.geometry('500x400')

    label2 = tk.Label(window2, text="Task1 window", height=5, width=20)
    label2.pack()

    button2 = tk.Button(window2, text="Task1_A", height=5, width=20, command=Task1_A_window)
    button2.pack()

    button3 = tk.Button(window2, text="Task1_B", height=5, width=20, command=Task1_B_window)
    button3.pack()

    button4 = tk.Button(window2, text="Back", command=open_window1, height=5, width=20)
    button4.pack()

    window2.mainloop()


def Task1_A_window():
    window2 = tk.Tk()
    window2.title("Filter")
    window2.geometry('500x400')

    label2 = tk.Label(window2, text="filter window", height=5, width=20)
    label2.pack()

    testcase_label = tk.Label(window2, text="Testcase Number:", height=5, width=20)
    testcase_label.pack()
    testcase_entry = tk.Entry(window2)
    testcase_entry.pack()
    button2 = tk.Button(window2, text="Test Cases", command=lambda: Testcases(testcase_entry))
    button2.pack()

    button4 = tk.Button(window2, text="Back", command=open_window1)
    button4.pack()

    window2.mainloop()


def Task1_B_window():
    window2 = tk.Tk()
    window2.title("Resampling window")
    window2.geometry('500x400')

    label2 = tk.Label(window2, text="Resampling window")
    label2.pack()

    m_label = tk.Label(window2, text="M Value:")
    m_label.pack()
    m_entry = tk.Entry(window2)
    m_entry.pack()

    l_label = tk.Label(window2, text="L Value:")
    l_label.pack()
    l_entry = tk.Entry(window2)
    l_entry.pack()

    button2 = tk.Button(window2, text="Resample", command=lambda: Resampling(m_entry, l_entry))
    button2.pack()

    button4 = tk.Button(window2, text="Back", command=open_window1)
    button4.pack()

    window2.mainloop()


open_window1()    