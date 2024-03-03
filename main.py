import warnings

from datetime import datetime, timedelta
from src.statistics_1 import *
from src.DailyHabit import *
from src.WeeklyHabit import *
from src.MonthlyHabit import *
from src.habit_tracker import *
from src.Habit import *


# Suppress all warnings
warnings.filterwarnings("ignore")

def start_new():
    """
    This function demonstrates adding and tracking habits.

    It creates instances of DailyHabit, WeeklyHabit, and MonthlyHabit,
    checks off some habits, and demonstrates various methods.

    Example:
    - To mark a habit as completed:
      brushteath_daily.mark_as_completed(start_date + timedelta(days=1))
      brushteath_daily.mark_as_completed(start_date + timedelta(days=2))
      Exercise_weekly.mark_as_completed(datetime(2024, 1, 15))

    - To check the break status of a habit:
      print(anycourse_study_weekly.check_break())

    - To check the streak with a specific target:
      print(brushteath_daily.check_streak(target_streak=5))

    - To get the streak count:
      print(brushteath_daily.get_streak_count())

    - Save habits to a JSON file:
      save_habits_to_json([brushteath_daily, cleaningroom_daily, Exercise_weekly, anycourse_study_weekly, skills_monthly, visiting_firends_Monthly], 'habits.json')
    """
    start_date = datetime(2023, 11, 1)  

    brushteath_daily = DailyHabit('Brush Teath Daily', start_date)
    cleaningroom_daily = DailyHabit('Cleaning room Daily', start_date)

    Exercise_weekly = WeeklyHabit('Exercise Weekly', start_date, weekdays=[0, 2])
    anycourse_study_weekly = WeeklyHabit('Read Weekly', start_date, weekdays=[0, 2])

    skills_monthly = MonthlyHabit('Skills Monthly', start_date, target_days=[1, 15])
    visiting_firends_Monthly = MonthlyHabit('Visiting Friends Monthly', start_date, target_days=[1, 15])

    
    # To mark a habit as completed : 
    brushteath_daily.mark_as_completed(start_date + timedelta(days=1)) 
    brushteath_daily.mark_as_completed(start_date + timedelta(days=2)) 
    Exercise_weekly.mark_as_completed(datetime(2024, 1, 15))

    # To check the break status of a habit : 
    print(anycourse_study_weekly.check_break())   

    # To check the streak with a specific target : 
    print(brushteath_daily.check_streak(target_streak=5)) 

    # To get the streak count : 
    print(brushteath_daily.get_streak_count())

    # Save habits to JSON file
    save_habits_to_json_file([brushteath_daily, cleaningroom_daily, Exercise_weekly, anycourse_study_weekly, skills_monthly, visiting_firends_Monthly], 'habits.json')


def show_statistics():
    """
    This function demonstrates habit statistics.

    It loads habits from a JSON file, showcases different statistics,
    and visualizes completed dates, streak count, and broken status using Pandas and Matplotlib.

    Example:
    - To find the longest habit streak:
      print(longest_streak(habits))

    - To find current daily habits:
      print(current_daily_habits(habits))
    
    - To find habits struggled last month:
      habits_struggled_last_month(habits)
    
    - To find all tracked habits:
      print(all_habits(habits))

    - To find habits with the same periodicity (Enter DailyHabit, MonthlyHabit, or WeeklyHabit):
      print(habits_same_frequency(habits , DailyHabit))

    - To visualize completed dates:
      visualize_completed_dates(habit_df)

    - To visualize streak count for daily habits:
      visualize_streak_count(daily_habits_df)

    - To visualize broken status:
      visualize_broken_status(habit_df)
    """
    # Load habits
    habits = load_habits_from_json_file('habits.json')

    # To find the longest habit streak 
    print(daily_habits_longest_streak(habits))

    # To find current daily habits 
    print(current_daily_habits(habits))
    
    # To find all tracked habits 
    print(all_habits(habits))

    # To find habits with the same periodicity (Enter DailyHabit, MonthlyHabit, or WeeklyHabit)
    print(habits_with_same_frequency(habits , DailyHabit))

    # Create DataFrame
    data_frame_habit = create_dataframe_of_habit(habits)

    # Visualize completed dates
    view_completed_habits_calender(data_frame_habit)

    # Visualize streak count for daily habits
    daily_habits_df = data_frame_habit[data_frame_habit['Type'] == 'DailyHabit']
    view_daily_habits_streak_count(daily_habits_df)

    # Visualize broken status
    view_broken_habit(data_frame_habit)

if __name__ == "__main__":

    """Uncomment the below code to add habit and track them."""
    start_new()
    """Uncomment the below code to show statistics."""
    show_statistics()