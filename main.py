import tkinter as tk
from exercises import exercises
import functions as fn

root = tk.Tk()
root.geometry('500x500')
root.resizable(False, False)
canvas = tk.Canvas(root, bg='grey')
canvas.pack()

background_image = tk.PhotoImage(file='background.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

upper_frame = tk.Frame(root, bg='snow4', bd=5)
upper_frame.place(relx=0.5, rely=0.01, relwidth=0.5, relheight=0.07, anchor='n')
upper_label = tk.Label(upper_frame, text='WORKOUT REPORT', bg='snow4', font=32, anchor='n')
upper_label.pack()

lower_frame = tk.Frame(root, bg='snow4', bd=5)
lower_frame.place(relx=0.5, rely=0.15, relwidth=0.82, relheight=0.7, anchor='n')
lower_label = tk.Label(lower_frame, text='SELECT EXERCISE:', bg='snow4')
lower_label.grid(row=10, column=1)

r, c = 0, 0
all_vars = []

for i in range(0, len(exercises)):
    var = tk.IntVar()
    all_vars.append(var)
    cb = tk.Checkbutton(lower_frame, text=exercises[i], variable=var, onvalue=1, offvalue=0,
                        height=1, width=15, anchor='w')
    cb.grid(row=r, column=c)
    c += 1
    if c == 3:
        r += 1
        c = 0

checked_exercises = [x for x in all_vars if x.get() == 1]

add_button = tk.Button(root, text='ADD', bd=5, padx=25, pady=2, command=fn.get_values(all_vars))
add_button.place(relx=0.5, rely=1, anchor='w', y=-30)

submit_button = tk.Button(root, text='SUBMIT', bd=5, padx=25, pady=2, command=fn.submit_workout(checked_exercises))
submit_button.place(relx=0.5, rely=1, anchor='e', y=-30)

root.mainloop()
