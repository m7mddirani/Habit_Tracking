import sys
import os

# Get the absolute path of the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory (root directory) to the Python path
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)


from src.Habit import *
from datetime import timedelta

class MonthlyHabit(Habit):
    """
    Represents a habit that repeats monthly and can be tracked and marked as completed.

    Args:
        name (str): The name of the habit.
        start_date (datetime): The start date of the habit.
        target_days (list): List of days in the month when the habit should be completed.

    Attributes:
        target_days (list): List of days in the month when the habit should be completed.

    Inherits from:
        Habit

    Methods:
        mark_completed(completion_date=None): Marks the habit as completed for the specified date.
        calculate_end_date(start_date, frequency): Calculates the end date of the habit based on the start date and frequency.
    """

    def __init__(self, name, start_date, target_days):
        """
        Initializes a MonthlyHabit object.

        Args:
            name (str): The name of the habit.
            start_date (datetime): The start date of the habit.
            target_days (list): List of days in the month when the habit should be completed.
        """
        super().__init__(name, start_date)
        self.target_days = target_days
        next_month = start_date.replace(day=28) + timedelta(days=4)
        self.end_date = (next_month.replace(day=1) - timedelta(days=1)).replace(hour=23, minute=59, second=59)

    def mark_completed(self, completion_date=None):
        """
        Marks the monthly habit as completed for the specified date.

        Args:
            completion_date (datetime): The date on which the habit is completed. Defaults to the current date.

        Raises:
            ValueError: If the completion date is not on a specified day.
        """
        if completion_date is None:
            completion_date = datetime.now()
        if completion_date.day in self.target_days:
            super().mark_as_completed(completion_date)
        else:
            raise ValueError("Completion date is not on a specified day.")

    def end_date(self, start_date, frequency):
        """
        Calculates the end date of the monthly habit based on the start date and frequency.

        Args:
            start_date (datetime): The start date of the habit.
            frequency (int): The frequency of the habit.

        Returns:
            datetime: The calculated end date of the habit.
        """
        next_month = start_date.replace(day=28) + timedelta(days=4)
        return (next_month.replace(day=1) - timedelta(days=1)).replace(hour=23, minute=59, second=59)
