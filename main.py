import tkinter as tk
from exercises import exercises

HEIGHT = 500
WIDTH = 500
root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='grey')
canvas.pack()

background_image = tk.PhotoImage(file='background.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

upper_frame = tk.Frame(root, bg='gray', bd=5)
upper_frame.place(relx=0.5, rely=0.01, relwidth=0.5, relheight=0.07, anchor='n')
label = tk.Label(upper_frame, text='WORKOUT REPORT', bg='gray', font=24, anchor='n')
label.pack()

lower_frame = tk.Frame(root, bg='gray', bd=5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.4, anchor='n')

# entry = tk.Entry(lower_frame, font=40)
# entry.place(relwidth=0.25, relheight=0.15)

exercise_menu = tk.Menubutton(lower_frame, text="Exercises", relief='raised')
exercise_menu.place()
exercise_menu.menu = tk.Menu(exercise_menu, tearoff=0)
exercise_menu["menu"] = exercise_menu.menu

for ex in exercises:
    exercise_menu.menu.add_checkbutton(label=ex, variable=ex)

exercise_menu.pack()

button = tk.Button(lower_frame, text='Submit')
# TODO make the button get all the selected exercises and pass them to the function
button.place(relx=0.5, rely=1, anchor='s')
root.mainloop()
#check name update