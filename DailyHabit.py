from datetime import datetime, timedelta
from src.Habit import Habit

class DailyHabit(Habit):
    """
    Represents a habit that users can track and mark as completed on a daily basis.

    Attributes:
        name (str): The name of the habit.
        start_date (datetime): The start date of the habit.
        end_date (datetime): The end date of the habit.
        streak_count (int): The current streak count of consecutive completions.

    Methods:
        calculate_end_date(start_date, frequency): Calculates the end date of the daily habit based on the start date and frequency.
        mark_completed(completion_date=None): Marks the habit as completed for the specified date.
        check_streak(target_streak): Checks if the habit has a streak of at least the specified number of consecutive days.
        get_streak_count(): Gets the current streak count of the habit.
    """

    def __init__(self, name, start_date):
        """
        Initializes a DailyHabit object.

        Args:
            name (str): The name of the habit.
            start_date (datetime): The start date of the habit.
        """
        super().__init__(name, start_date)
        self.streak_counter = 0
        self.calculate_end_date(start_date, frequency=1)  # Assuming frequency is 1 (daily)

    def calculate_end_date(self, start_date, frequency):
        """
        Calculates the end date of the daily habit based on the start date and frequency.

        Args:
            start_date (datetime): The start date of the habit.
            frequency (int): The frequency of the habit.

        Returns:
            datetime: The calculated end date of the habit.
        """
        self.end_date = start_date + timedelta(days=frequency)
        
    def mark_completed(self, completion_date=None):
        """
        Marks the daily habit as completed for the specified date.

        Args:
            completion_date (datetime): The date on which the habit is completed. Defaults to the current date.

        Raises:
            ValueError: If the completion date is outside the habit period.
        """
        if completion_date is None:
            completion_date = datetime.now().date()

        if completion_date == self.end_date:
            self.streak_counter += 1
        elif completion_date > self.end_date:
            # Check if the completion date is the day after the current end date (consecutive day)
            if (completion_date - self.end_date).days == 1:
                self.streak_counter += 1
                self.end_date = completion_date
            else:
                self.streak_counter = 1  # Reset streak count if not consecutive
                self.end_date = completion_date  # Update the end date to the new completion date
        else:
            raise ValueError("Completion date is outside the habit period.")

    def check_streak(self, target_streak):
        """
        Checks if the habit has a streak of at least the specified number of consecutive days.

        Args:
            target_streak (int): The minimum required streak count.

        Returns:
            bool: True if the habit has a streak equal to or greater than the target_streak, False otherwise.
        """
        return self.streak_counter >= target_streak

    def get_streak_count(self):
        """
        Gets the current streak count of the habit.

        Returns:
            int: The current streak count of the habit.
        """
        return self.streak_counter
