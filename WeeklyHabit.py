import sys
import os

# Get the absolute path of the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory (root directory) to the Python path
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)


from src.Habit import *
from datetime import timedelta

class WeeklyHabit(Habit):
    """
    Represents a habit that recurs weekly and can be tracked and marked as completed.

    Attributes:
        name (str): The name of the habit.
        start_date (datetime): The start date of the habit.
        weekdays (list): List of weekdays when the habit should be completed (0 for Monday, 1 for Tuesday, ..., 6 for Sunday).

    Methods:
        mark_completed(completion_date=None): Marks the habit as completed for the specified date.
        calculate_end_date(start_date, frequency): Calculates the end date of the habit based on the start date and frequency.
    """

    def __init__(self, name, start_date, weekdays):
        """
        Initializes a WeeklyHabit object.

        Args:
            name (str): The name of the habit.
            start_date (datetime): The start date of the habit.
            weekdays (list): List of weekdays when the habit should be completed (0 for Monday, 1 for Tuesday, ..., 6 for Sunday).
        """
        super().__init__(name, start_date)
        self.weekdays = weekdays
        self.end_date = start_date + timedelta(weeks=1)

    def mark_as_completed(self, completion_date=None):
        """
        Marks the weekly habit as completed for the specified date.

        Args:
            completion_date (datetime): The date on which the habit is completed. Defaults to the current date.

        Raises:
            ValueError: If the completion date is not on a specified weekday.
        """
        if completion_date is None:
            completion_date = datetime.now()
        if completion_date.weekday() in self.weekdays:
            super().mark_as_completed(completion_date)
        else:
            raise ValueError("Completion date is not on a specified weekday.")

    def end_date(self, start_date, frequency):
        """
        Calculates the end date of the weekly habit based on the start date and frequency.

        Args:
            start_date (datetime): The start date of the habit.
            frequency (int): The frequency of the habit.

        Returns:
            datetime: The calculated end date of the habit.
        """
        return start_date + timedelta(weeks=frequency)
