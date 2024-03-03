from datetime import datetime

class Habit:
    """
    Represents a habit that users can track and mark as completed.

    Attributes:
        name (str): The name of the habit.
        start_date (datetime): The start date of the habit.
        completed_dates (set): Dates on which the habit was completed.
        broken (bool): Indicates whether the habit has been broken.

    Methods:
        mark_completed(completion_date=None): Marks the habit as completed for the specified date.
        mark_incomplete(completion_date): Marks the habit as incomplete for the specified date.
        calculate_end_date(start_date, frequency): Calculates the end date of the habit.
        check_break_status(): Checks if the habit has been broken.
    """

    def __init__(self, name, start_date):
        """
        Initializes a Habit instance.

        Parameters:
            name (str): The name of the habit.
            start_date (datetime): The start date of the habit.
        """
        self.name = name
        self.start_date = start_date
        self.completed_dates = set()
        self.broken = False

    def mark_as_completed(self, completion_date=None):
        """
        Marks the habit as completed for the specified date.

        Parameters:
            completion_date (datetime, optional): The date on which the habit is completed. Defaults to the current date.
        """
        completion_date = completion_date or datetime.now()

        if self.start_date <= completion_date:
            self.completed_dates.add(completion_date.date())
            self.broken = False
        else:
            raise ValueError("Completion date cannot be earlier than the start date.")

    def mark_as_incomplete(self, completion_date):
        """
        Marks the habit as incomplete for the specified date.

        Parameters:
            completion_date (datetime): The date on which the habit is marked incomplete.
        """
        self.completed_dates.discard(completion_date.date())

    def end_date(self, start_date, frequency):
        """
        Calculates the end date of the habit based on the start date and frequency.

        Parameters:
            start_date (datetime): The start date of the habit.
            frequency (int): The frequency of the habit.
        """
        raise NotImplementedError("Subclasses must implement the end_date method.")

    def check_break(self):
        """
        Checks if the habit has been broken based on completion status.

        Returns:
            bool: True if the habit is broken (not completed at all), False otherwise.
        """
        self.broken = not self.completed_dates
        return self.broken
