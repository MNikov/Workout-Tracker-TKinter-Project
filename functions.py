import os
from datetime import date

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
desktop_path = desktop + os.path.sep + 'MyWorkouts.txt'
today = date.today()


def submit_workout(exercise_dict):
    with open(desktop_path, 'a') as report:
        report.write(f'{">" * 3} {today.strftime("%d/%m/%Y")}\n')
        for exercise in exercise_dict:
            if exercise_dict[exercise].get() == 1:
                report.write(f'— {exercise}\n')
        report.write('\n')
