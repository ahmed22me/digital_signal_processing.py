import tkinter as tk
from tkinter import ttk
import subprocess


def task1():
    subprocess.run(["python", "task1/task1.py"], check=True)

def task2():
    subprocess.run(["python", "task2/task2.py"], check=True)

def task3():
    subprocess.run(["python", "task3/task3.py"], check=True)


def task4():
    subprocess.run(["python", "task4/task4.py"], check=True)


def task5():
    subprocess.run(["python", "task5/task5.py"], check=True)


def task6():
    subprocess.run(["python", "task6/task6.py"], check=True)


def task7():
    subprocess.run(["python", "task7/task7.py"])


def task8():
    subprocess.run(["python", "task8/task8.py"], check=True)

def task9():
    subprocess.run(["python", "task9/practical.py"])



def set_background_color(widget, color):
    widget.configure(bg=color)


root = tk.Tk()
root.title("DSP Tasks")

root.configure(bg='#B5E6D6')


# Create a style
style = ttk.Style()
style.configure("TButton", font=('a', 20), background='#83C8B1',)


# -----------------------------------------------------
# Task 1 Frame
task1_frame = ttk.Frame(root)
task1_frame.grid(row=0, column=0, padx=30, pady=30)
ttk.Button(task1_frame, text="Task1",width=10, padding=10,command=lambda :task1()).grid(row=0, column=0, columnspan=2)
# -------------------------------------------------------


# -------------------------------------------------------
# Task 2 Frame
task2_frame = ttk.Frame(root)
task2_frame.grid(row=0, column=1, padx=30, pady=30)
ttk.Button(task2_frame, text="Task2",width=10, padding=10,command=lambda :task2()).grid(row=0, column=1,columnspan=2)
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
# gui task 3
task3_frame = ttk.Frame(root)
task3_frame.grid(row=1, column=0, padx=30, pady=30)
ttk.Button(task3_frame, text="Task3",width=10, padding=10,command=lambda :task3()).grid(row=1, column=0, columnspan=2)
# -------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------
# gui task4
task4_fram = ttk.Frame(root)
task4_fram.grid(row=1, column=1, padx=30, pady=30)
ttk.Button(task4_fram, text="Task4",width=10, padding=10,command=lambda :task4()).grid(row=1,column=1,columnspan=2)
# ---------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------
# gui task 5
task5_frame = ttk.Frame(root)
task5_frame.grid(row=2, column=0, padx=30, pady=30)
ttk.Button(task5_frame, text="Task5",width=10, padding=10,command=lambda :task5()).grid(row=2,column=0,columnspan=2)
# ----------------------------------------------------------------------------------------


# -----------------------------
# gui task 6
task6_frame = ttk.Frame(root)
task6_frame.grid(row=2, column=1, padx=30, pady=30)
ttk.Button(task6_frame, text="Task6",width=10, padding=10,command=lambda :task6()).grid(row=2, column=1,columnspan=2)
# ---------------------------


# ------------------------
# gui task7
task7_frame = ttk.Frame(root)
task7_frame.grid(row=3, column=0, padx=30, pady=30)
ttk.Button(task7_frame, text="Task7",width=10, padding=10,command=lambda :task7()).grid(row=3, column=0,columnspan=2)
# ------------------------


# ------------------------
# gui task8
task8_frame = ttk.Frame(root)
task8_frame.grid(row=3, column=1, padx=30, pady=30)
ttk.Button(task8_frame, text="Task8",width=10, padding=10,command=lambda :task8()).grid(row=3, column=1,columnspan=2)
# ------------------------


# ------------------------
# gui task9
task9_frame = ttk.Frame(root)
task9_frame.grid(row=4, column=0, padx=30, pady=30)
ttk.Button(task9_frame, text="Task9",width=10, padding=10,command=lambda :task9()).grid(row=4, column=0,columnspan=2)
# ----------------------------------------------



# Start the GUI main loop
root.mainloop()
