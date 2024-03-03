# Habits_Tracker
The Habit Tracker is a Python application that allows users to track their daily, weekly, and monthly habits. Users can create, monitor, and mark habits as completed, enabling them to build and maintain positive habits over time.

Features
- **Daily Habits:** Users can create habits that need to be completed daily.
- **Weekly Habits:** Users can create habits that need to be completed on specific days of the week.
- **Monthly Habits:** Users can create habits that need to be completed on specific days of the month.
- **Streak Tracking:** The application tracks streaks for daily habits, encouraging users to maintain consistency.
- **JSON Data Storage:** Habits and their completion data are stored in JSON format, allowing for easy retrieval and persistence.
- **Documentation:** The project includes documentation generated using Doxygen.

Installation
Clone the repository to your local machine:

```bash
git clone https://github.com/mhmddirani/habit-tracker.git
```

Navigate to the project directory:

```bash
cd habit-tracker
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Usage
To start a new habit tracker session:

```bash
python main.py
```

Follow the on-screen instructions to add and track your habits.

Unit Tests
To run unit tests for the Habit Tracker:

```bash
python -m unittest discover unit_test
```

Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature`)
6. Create a new Pull Request

Documentation
The project includes documentation generated using Doxygen. You can find the HTML documentation in the `docs` directory.

```
