
import json
import sys
import os

# Get the absolute path of the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory (root directory) to the Python path
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)


from datetime import datetime
from src.DailyHabit import DailyHabit
from src.WeeklyHabit import WeeklyHabit
from src.MonthlyHabit import MonthlyHabit

def save_habits_to_json_file(habits, filename):
    """
    Saves a list of habit objects to a JSON file.

    Args:
        habits (list): List of Habit objects to be saved.
        filename (str): The name of the JSON file.

    Returns:
        None
    """
    habit_data = []
    for habit in habits:
        habit_data.append({
            'name': habit.name,
            'start_date': habit.start_date.isoformat(),
            'completed_dates': [date.isoformat() for date in habit.completed_dates],
            'broken': habit.broken,
            'streak_count': getattr(habit, 'streak_count', None)
        })

    with open(filename, 'w') as file:
        json.dump(habit_data, file)

def load_habits_from_json_file(filename):
    """
    Loads a list of habit objects from a JSON file.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        list: List of loaded Habit objects.
    """
    habits = []
    with open(filename, 'r') as file:
        habit_data = json.load(file)
        for data in habit_data:
            if data.get('weekdays'):
                habit = WeeklyHabit(data['name'], datetime.fromisoformat(data['start_date']), data['weekdays'])
            elif data.get('target_days'):
                habit = MonthlyHabit(data['name'], datetime.fromisoformat(data['start_date']), data['target_days'])
            else:
                habit = DailyHabit(data['name'], datetime.fromisoformat(data['start_date']))

            habit.completed_dates = {datetime.fromisoformat(date).date() for date in data['completed_dates']}
            habit.broken = data['broken']
            setattr(habit, 'streak_counter', data.get('streak_counter', 0))
            habits.append(habit)

    return habits
