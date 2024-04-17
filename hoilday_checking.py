from datetime import date, timedelta

def solution(X, H):
    """
    Calculate the total number of rest days in the year 2023 given the day of the week for January 1st
    and a list of public holidays. If a public holiday falls on a weekend, it is not counted as an extra rest day.

    :param start_day: Day of the week for January 1st (1 for Monday, ... 7 for Sunday)
    :param holidays: List of tuples representing public holidays (e.g., [(1, 1), (5, 5)] for Jan 1 and May 5)
    :return: Total number of rest days considering weekends and non-weekend holidays
    """
    # Start by adding the total number of holidays to the rest days count
    rest_days = len(H)
    day_of_week = X  # 1 for Monday, ... 7 for Sunday
    
    # Calculate the total number of days in the year
    days_in_year = 365  # 2023 is not a leap year
    
    # Iterate through each day of the year
    for day in range(1, days_in_year + 1):
        # Check if it's a weekend
        if day_of_week == 6 or day_of_week == 7:
            rest_days += 1
        
        # Move to the next day of the week
        day_of_week = 1 if day_of_week == 7 else day_of_week + 1
    
    # Subtract for holidays that fall on weekends
    for month, day in H:
        if date(2023, month, day).weekday() in [5, 6]:  # 5=Saturday, 6=Sunday
            rest_days -= 1

    return rest_days