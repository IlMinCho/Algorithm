from datetime import date, timedelta

def solution(X, H):
    # current_year = date.today().year
    # start_date = date(current_year, 1, 1)
    
    # days_to_adjust = (X- start_date.isoweekday()) % 7
    # start_date += timedelta(days=days_to_adjust)

   
    # rest_days = 0
    # while start_date.year == current_year:
    #     if start_date.isoweekday() in [6, 7]: 
    #         rest_days += 1
    #     start_date += timedelta(days=1)
    
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    rest_days = 0  # Total number of rest days
    day_of_week = X  # 1 for Monday, ... 7 for Sunday

    # Set to keep track of holidays that have been accounted for to avoid double-counting
    counted_holidays = set()

    for month_index, days_in_month in enumerate(months):
        for day in range(1, days_in_month + 1):
            current_date = (month_index + 1, day)
            # Check for weekends and increment rest_days
            if day_of_week in [6, 7]:  # 6 for Saturday, 7 for Sunday
                rest_days += 1
                # If it's a Sunday, and the next day is a public holiday, skip it to avoid double-counting
                if day_of_week == 7 and (month_index + 1, day + 1) in H:
                    counted_holidays.add((month_index + 1, day + 1))
            # Check for public holidays not on weekends and not already counted
            elif current_date in H and current_date not in counted_holidays:
                rest_days += 1
                # If the holiday is on a Sunday, the following Monday is a substitute holiday
                if day_of_week == 7:
                    counted_holidays.add((month_index + 1, day + 1))
            # Update the day of the week, wrapping back to 1 (Monday) after 7 (Sunday)
            day_of_week = 1 if day_of_week == 7 else day_of_week + 1
    
    return rest_days