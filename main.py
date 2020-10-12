import tkinter as tk
import os
from datetime import date


def submit_workout(exercise_dict):
    with open(desktop_path, 'a') as report:
        report.write(f'{">" * 3} {today.strftime("%d/%m/%Y")}\n')
        for exercise in exercise_dict:
            if exercise_dict[exercise].get() == 1:
                report.write(f'— {exercise}\n')
        report.write('\n')


desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
desktop_path = desktop + os.path.sep + 'MyWorkouts.txt'
today = date.today()

exercises = sorted([
    'Pull ups',
    'Squats',
    'Dips',
    'Lunges',
    'Deadlifts',
    'Push ups',
    'Bench press',
    'Biceps curls',
    'Triceps extensions',
    'Roman deadlift',
    'Front squats',
    'Military press',
    'Running',
    'Calf raises',
    'Sit ups',
    'Plank',
    'Muscle ups',
    'Front lever',
    'OAPs',
    'Swimming',
    'Rope skipping',
    'Rows',
    'Ring muscle ups',
    'Back lever',
    'Planche',
    'Leg press',
    'Nordic curls',
    'HSPUs',
    'Ring dips',
    'Isometric holds',

])

root = tk.Tk()
root.title('Workout Tracker')
# root.iconbitmap('icon.ico')
window_w = 500
window_h = 500
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
x = (screen_w / 2) - (window_w / 2)
y = (screen_h / 2) - (window_h / 2) - 25
root.geometry('%dx%d+%d+%d' % (window_w, window_h, x, y))
root.resizable(False, False)

# background_image = tk.PhotoImage(
#     file='background.png')
background_label = tk.Label(root)
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
                        height=1, width=15, anchor='w', bg='snow4', relief='raised')
    cb.grid(row=r, column=c)
    c += 1
    if c == 3:
        r += 1
        c = 0

submit_button = tk.Button(root, text='SUBMIT', bd=5, padx=25, pady=2, bg='snow4',
                          activebackground='orangered', command=lambda: submit_workout(all_vars_dict))
submit_button.place(relx=0.5, rely=1, anchor='s', y=-50)

root.mainloop()
