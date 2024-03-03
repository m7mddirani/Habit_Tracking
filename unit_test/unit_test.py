import sys
import os

# Get the absolute path of the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory (root directory) to the Python path
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)

from datetime import datetime, timedelta

from src.habit_tracker import load_habits_from_json_file, save_habits_to_json_file
from src.DailyHabit import DailyHabit
from src.WeeklyHabit import WeeklyHabit
from src.MonthlyHabit import MonthlyHabit

def test_streak_count_update():
    # Create a temporary JSON file for testing
    test_json_filename = 'test_habits.json'

    # Test case 1: Daily habit with a streak count of 2
    daily_habit_data = {"name": "Brush Teeth Daily", "start_date": "2023-11-01T00:00:00", "completed_dates": ["2023-11-02", "2023-11-03"], "broken": False, "streak_count": 0}
    daily_habit = DailyHabit(daily_habit_data['name'], datetime.fromisoformat(daily_habit_data['start_date']))
    daily_habit.completed_dates = {datetime.fromisoformat(date).date() for date in daily_habit_data['completed_dates']}
    daily_habit.broken = daily_habit_data['broken']
    daily_habit.streak_counter = daily_habit_data['streak_count']

    # Save the daily habit to the temporary JSON file
    save_habits_to_json_file([daily_habit], test_json_filename)

    # Load the daily habit from the temporary JSON file
    loaded_daily_habit = load_habits_from_json_file(test_json_filename)[0]
    
    # Check if the streak count of the daily habit is updated correctly
    assert loaded_daily_habit.streak_counter == 0

    # Test case 2: Weekly habit with no completed dates
    weekly_habit_data = {"name": "Exercise Weekly", "start_date": "2024-03-01T00:00:00", "weekdays": [0, 2, 4], "completed_dates": [], "broken": True, "streak_count": 0}
    weekly_habit = WeeklyHabit(weekly_habit_data['name'], datetime.fromisoformat(weekly_habit_data['start_date']), weekly_habit_data['weekdays'])
    weekly_habit.completed_dates = {datetime.fromisoformat(date).date() for date in weekly_habit_data['completed_dates']}
    weekly_habit.broken = weekly_habit_data['broken']
    weekly_habit.streak_counter = weekly_habit_data['streak_count']


    # Save the weekly habit to the temporary JSON file
    save_habits_to_json_file([weekly_habit], test_json_filename)

    # Load the weekly habit from the temporary JSON file
    loaded_weekly_habit = load_habits_from_json_file(test_json_filename)[0]
    
    # Check if the streak count of the weekly habit is updated correctly
    assert loaded_weekly_habit.get_streak_count() == 0  # The streak count is expected to be 0 for a habit with no completed dates

    # Test case 3: Monthly habit with a broken streak
    monthly_habit_data = {"name": "Read Monthly", "start_date": "2024-03-01T00:00:00", "target_days": [5, 15, 25], "completed_dates": ["2024-03-02"], "broken": True, "streak_count": 0}
    monthly_habit = MonthlyHabit(monthly_habit_data['name'], datetime.fromisoformat(monthly_habit_data['start_date']), monthly_habit_data['target_days'])
    monthly_habit.completed_dates = {datetime.fromisoformat(date).date() for date in monthly_habit_data['completed_dates']}
    monthly_habit.broken = monthly_habit_data['broken']
    monthly_habit.streak_count = monthly_habit_data['streak_count']

    # Save the monthly habit to the temporary JSON file
    save_habits_to_json_file([monthly_habit], test_json_filename)

    # Load the monthly habit from the temporary JSON file
    loaded_monthly_habit = load_habits_from_json_file(test_json_filename)[0]
    
    # Check if the streak count of the monthly habit is updated correctly
    assert loaded_monthly_habit.get_streak_count() == 0  # The streak count is expected to be 0 for a habit with a broken streak

    # Print a success message if all test cases pass
    print("All unit tests passed successfully!")

    # Clean up: Remove the temporary JSON file after testing
    import os
    os.remove(test_json_filename)

# Run the test
test_streak_count_update()

