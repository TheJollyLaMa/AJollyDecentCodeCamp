import calendar

year = int(input("Enter a year (e.g., 2023): "))
month = int(input("Enter a month (1-12): "))

if 1 <= month <= 12:
    print(calendar.month(year, month))
else:
    print("Invalid month. Please run the program again and enter a month between 1 and 12.")