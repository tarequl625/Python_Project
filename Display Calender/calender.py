# -------------------------------
# Display Calendar for a Given Month
# -------------------------------

# Import calendar module
import calendar

# Take year and month input from user
year = int(input("Enter year : "))
month = int(input("Enter month (1-12) : "))

# Get the calendar for the specified month
month_calendar = calendar.month(year, month)

# Print the calendar
print(month_calendar)

# -------------------------------
# Example Run - 1:
# Input : Year = 2025, Month = 9
# Output: (Calendar of September 2025)
#
# Example Run - 2:
# Input : Year = 2023, Month = 2
# Output: (Calendar of February 2023)
# -------------------------------