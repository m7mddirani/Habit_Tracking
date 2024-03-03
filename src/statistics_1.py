import pandas as pd
import matplotlib.pyplot as plt
import timedelta 
import sys
import os

# Get the absolute path of the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory (root directory) to the Python path
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)

from src.habit_tracker import load_habits_from_json_file
from src.Habit import *
from src.DailyHabit import DailyHabit

def daily_habits_longest_streak(habits):
    """
    Finds the longest streak among daily habits.

    Args:
        habits (list): List of Habit objects.

    Returns:
        int: Length of the longest streak among daily habits.
    """
    max_streak = 0
    for habit in habits:
        if isinstance(habit, DailyHabit):
            streak = habit.streak_counter
            if streak is not None:
                max_streak = max(max_streak, streak)
    return max_streak

def current_daily_habits(habits):
    """
    Retrieves names of currently tracked daily habits.

    Args:
        habits (list): List of Habit objects.

    Returns:
        list: Names of currently tracked daily habits.
    """
    current_daily_habits = [habit.name for habit in habits if isinstance(habit, DailyHabit)]
    return current_daily_habits

def find_habits_strugled_last_month(habits):
    """
    Finds habits that were struggled with last month.

    Args:
        habits (list): List of Habit objects.

    Returns:
        list: Names of habits that were struggled with last month.
    """
    last_month = datetime.now().replace(day=1) - timedelta(days=1)
    struggling_habits = []

    for habit in habits:
        if isinstance(habit, DailyHabit):
            last_month_completed_dates = [date for date in habit.completed_dates if date.month == last_month.month]
            if len(last_month_completed_dates) < habit.streak_counter():
                struggling_habits.append(habit.name)

    return struggling_habits

def all_habits(habits):
    """
    Retrieves names of all currently tracked habits.

    Args:
        habits (list): List of Habit objects.

    Returns:
        list: Names of all currently tracked habits.
    """
    return [habit.name for habit in habits]

def habits_with_same_frequency(habits, habit_type):
    """
    Retrieves names of habits with the same periodicity.

    Args:
        habits (list): List of Habit objects.
        habit_type (type): Type of Habit (DailyHabit, WeeklyHabit, MonthlyHabit).

    Returns:
        list: Names of habits with the specified periodicity.
    """
    return [habit.name for habit in habits if isinstance(habit, habit_type)]

def find_longest_run_streak_among_all_habits(habits):
    """
    Finds the longest run streak among all habits.

    Args:
        habits (list): List of Habit objects.

    Returns:
        int: Length of the longest run streak among all habits.
    """
    max_streak = 0
    for habit in habits:
        streak = habit.streak_counter()
        max_streak = max(max_streak, streak)
    return max_streak

def find_longest_run_streak_for_specific_habit(habit):
    """
    Finds the longest run streak for a specific habit.

    Args:
        habit (Habit): A specific Habit object.

    Returns:
        int: Length of the longest run streak for the specified habit.
    """
    return habit.streak_counter()

def load_habits_from_json_file():
    """
    Loads habits from a JSON file.

    Returns:
        list: List of Habit objects.
    """
    return load_habits_from_json_file('habits.json')

def create_dataframe_of_habit(habits):
    """
    Creates a pandas DataFrame containing information about each habit.

    Args:
        habits (list): List of Habit objects.

    Returns:
        pd.DataFrame: DataFrame with habit information.
    """
    habit_data_list = []
    for habit in habits:
        habit_data = {
            'Name': habit.name,
            'Type': type(habit).__name__,
            'Start Date': habit.start_date,
            'End Date': habit.end_date,
            'Completed Dates': len(habit.completed_dates),
            'Streak Count': getattr(habit, 'streak_count', None),
            'Broken': habit.check_break()
        }
        habit_data_list.append(habit_data)
    return pd.DataFrame(habit_data_list)

def view_completed_habits_calender(data_frame_habit):
    """
    Visualizes the number of completed dates for each habit using a bar chart.

    Args:
        data_frame_habit (pd.DataFrame): DataFrame with habit information.
    """
    data_frame_habit.plot(kind='bar', x='Name', y='Completed Dates', legend=False)
    plt.title('Number of Completed Dates for Each Habit')
    plt.xlabel('Habit Name')
    plt.ylabel('Number of Completed Dates')
    plt.show()

def view_daily_habits_streak_count(data_frame_daily_habits):
    """
    Visualizes the streak count for daily habits using a bar chart.

    Args:
        data_frame_daily_habits (pd.DataFrame): DataFrame with daily habit information.
    """
    data_frame_daily_habits['Streak Count'] = data_frame_daily_habits['Streak Count'].apply(lambda x: 0 if x is None else x)
    
    data_frame_daily_habits.plot(kind='bar', x='Name', y='Streak Count', legend=False)
    plt.title('Streak Count for Daily Habits')
    plt.xlabel('Habit Name')
    plt.ylabel('Streak Count')
    plt.show()


def view_broken_habit(data_frame_habit):
    """
    Visualizes the broken status for each habit using a bar chart.

    Args:
        data_frame_habit (pd.DataFrame): DataFrame with habit information.
    """
    data_frame_habit['Broken'] = data_frame_habit['Broken'].astype(int)
    data_frame_habit.plot(kind='bar', x='Name', y='Broken', legend=False)
    plt.title('Broken Status for Each Habit')
    plt.xlabel('Habit Name')
    plt.ylabel('Broken (1 for True, 0 for False)')
    plt.show()
