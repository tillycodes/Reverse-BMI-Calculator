import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Reverse BMI Calculator")

window_width = 300
window_height = 200

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

message = tk.Label(root, text="Reverse BMI Calculator")
message.pack()

height = tk.Label(root, text="Enter your height in metres.")
height.pack()

textbox = ttk.Entry(root, textvariable="height")
textbox.pack()

bmi = tk.Label(root, text="Enter your desired BMI.")
bmi.pack()

textbox1 = ttk.Entry(root, textvariable="bmi")
textbox1.pack()

def callback():
    height = float(textbox.get())
    bmi = float(textbox1.get())
    goal_weight = (bmi * (height * height))
    print_label = ttk.Label(root, text="Your goal weight (in kilograms) is:")
    print_label.pack()
    print_goal_weight = ttk.Label(text=goal_weight)
    print_goal_weight.pack()

button = ttk.Button(root, text="Calculate my goal weight!", command=callback)
button.pack()

root.mainloop()