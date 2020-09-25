"""
You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""


def month_in_year(day, year):
    """simple cal for identifying month from the sqeuential day in the year."""

    if day < 0 or day > 365:
        if day == 366 and (year % 4 == 0):
            pass
        else:
            raise ValueError("The day entered '" + str(day) + "' is invalid for year '" + str(year) + "'")

    if is_leap_year(year):
        day_map = month_days_dictionary_leap
    else:
        day_map = month_days_dictionary_non_leap    
    
    running_count = 0
    i = 0
    while running_count < day:
        i += 1
        running_count += day_map[i]

    day_of_month = day - (running_count - day_map[i])  

    print("The month is " + str(i) + ". and the day of the month is " + str(day_of_month))


month_days_dictionary_non_leap = {  1 : 31,
                                    2 : 28,
                                    3 : 31,
                                    4 : 30,
                                    5 : 31,
                                    6 : 30,
                                    7 : 31,
                                    8 : 31,
                                    9 : 30,
                                    10 : 31,
                                    11 : 30,
                                    12 : 31 }

month_days_dictionary_leap = {  1 : 31,
                                2 : 29,
                                3 : 31,
                                4 : 30,
                                5 : 31,
                                6 : 30,
                                7 : 31,
                                8 : 31,
                                9 : 30,
                                10 : 31,
                                11 : 30,
                                12 : 31 }

month_map = { 1: "Jan",
              2: "Feb",
              3: "Mar",
              4: "Apr",
              5: "May",
              6: "Jun",
              7: "Jul",
              8: "Aug",
              9: "Sep",
              10: "Oct",
              11: "Nov",
              12: "Dec",}


written_day = {1: "monday",
               2: "tuesday",
               3: "wednesday",
               4: "thursday",
               5: "friday",
               6: "saturday",
               0: "sunday"}

def is_leap_year(year):
    if year % 4 == 0:
        if year % 1000 != 0 or (year % 1000 == 0 and year % 400 == 0):
            return True
    return False


def first_sundays_since_1_jan_1900(month,day,year):
    cumulative_total_days = 0
    current_year = 1900
    current_day = 1
    current_month = 2
    number_of_1st_sundays = 0
    day_in_week = (month_days_dictionary_non_leap[current_month-1]) %7 # sunday is 0

    while current_year < year or (current_year==year and current_month <= month) or (current_year==year and current_month == month and current_day <= day):
        
        if day_in_week % 7 == 0:
            number_of_1st_sundays += 1
            print("First",written_day[day_in_week],"found on " + month_map[current_month] + " 1 " + str(current_year))
        
        #jump month by month
        if is_leap_year(current_year):
            day_map = month_days_dictionary_leap
        else:
            day_map = month_days_dictionary_non_leap

        #add the days in the previous month
        cumulative_total_days += day_map[current_month]
        day_in_week = (day_in_week + day_map[current_month]) % 7

        current_month += 1
        current_day += 1
        if current_month % 13 == 0:
            current_month = 1
            current_year += 1
        
    
    print("There are " + str(number_of_1st_sundays) + " first Sundays between Jan 1, 1900 and " + month_map[month] + " " + str(day) + " " + str(year))
    return number_of_1st_sundays


if __name__ == '__main__':
    #month_in_year(31+29,2001)
    #month_in_year(365,2000)
    #month_in_year(366,2000)
    first_sundays_since_1_jan_1900(12,31,2020)
    print(first_sundays_since_1_jan_1900(1,1,2001) - first_sundays_since_1_jan_1900(12,31,1900)) #SOLUTION 171
    