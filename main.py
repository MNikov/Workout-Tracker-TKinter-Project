import tkinter as tk
from exercises import exercises
import functions as fn

root = tk.Tk()
root.geometry('500x500')
root.resizable(False, False)

background_image = tk.PhotoImage(file='background.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

upper_frame = tk.Frame(root, bg='snow4', bd=5)
upper_frame.place(relx=0.5, rely=0.02, relwidth=0.34, relheight=0.07, anchor='n')
upper_label = tk.Label(upper_frame, text='WORKOUT REPORT', bg='snow4', font=32)
upper_label.pack()

lower_frame = tk.Frame(root, bg='snow4', bd=5)
lower_frame.place(relx=0.5, rely=0.15, relwidth=0.82, relheight=0.56, anchor='n')
lower_label = tk.Label(lower_frame, text='SELECT EXERCISE/S:', bg='snow4')
lower_label.grid(row=1, column=1)

all_vars_dict = {}
r, c = 4, 0
for i in range(0, len(exercises)):
    var = tk.IntVar()
    all_vars_dict[exercises[i]] = var
    cb = tk.Checkbutton(lower_frame, text=exercises[i], variable=var, onvalue=1, offvalue=0,
                        height=1, width=15, anchor='w')
    cb.grid(row=r, column=c)
    c += 1
    if c == 3:
        r += 1
        c = 0

submit_button = tk.Button(root, text='SUBMIT', bd=5, padx=25, pady=2, bg='snow4', activebackground='orangered', command=fn.submit_workout(all_vars_dict))
submit_button.place(relx=0.5, rely=1, anchor='s', y=-50)

root.mainloop()
