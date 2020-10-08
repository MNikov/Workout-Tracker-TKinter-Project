import os
import datetime

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
desktop_path = desktop + os.path.sep + 'MyWorkouts.txt'
time = datetime.datetime.now()


def submit_workout(exercises):
    with open(desktop_path, 'a') as report:
        report.write(f'{time.date()} {time.strftime("%A")}\n')
        for exercise in exercises:
            report.write(f'— {exercise}\n')
        report.write('-' * 20)


def get_values(vars):
    checked = []
    for v in vars:
        value = v.get()
        if value == 1:
            checked.append(v)
    return checked