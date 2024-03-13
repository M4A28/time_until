from datetime import datetime
from termcolor import colored
import argparse


def calculate_time_difference(date1, date2):
    # Convert the dates into datetime objects
    date1 = datetime.strptime(date1, "%Y-%m-%d")
    date2 = datetime.strptime(date2, "%Y-%m-%d")

    # Calculate the difference between the two dates
    difference = date2 - date1

    # Calculate the difference in various units
    difference_in_seconds = difference.total_seconds()
    difference_in_minutes, difference_in_seconds = divmod(difference_in_seconds, 60)
    difference_in_hours, difference_in_minutes = divmod(difference_in_minutes, 60)
    difference_in_days, difference_in_hours = divmod(difference_in_hours, 24)
    difference_in_months, difference_in_days = divmod(difference_in_days, 30)
    difference_in_years, difference_in_months = divmod(difference_in_months, 12)

    result = {
        "years": difference_in_years,
        "months": difference_in_months,
        "days": difference_in_days
        # "hours": difference_in_hours,
        # "minutes": difference_in_minutes,
        # "seconds": difference_in_seconds
    }

    return result

def main():
    parser = argparse.ArgumentParser(description='Calculate difference between two dates')
    parser.add_argument('-start', type=str , help='The first date.', nargs='?', default=str(datetime.now().date()))
    parser.add_argument('-end', type=str,  help='The second date')
    args = parser.parse_args()

    dates_diff = calculate_time_difference(args.start, args.end)
    print(f"The time from {args.start} to {args.end} is:")

    for time in dates_diff:
         print(colored(f"{dates_diff[time]} {time}.", "green"))

if __name__ == '__main__':
    main()
