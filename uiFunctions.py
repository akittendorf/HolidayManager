import Holiday as h
import HolidayList as hl
import datetime as dt
import json


def addition(HolidayListObj):
    print(".-------------.\n| Add Holiday |\n'-------------'")
    name = input('Holiday Name: ').lower()
    date = input('Holiday Date [yyyy-m-d]: ')
    try: 
        if HolidayListObj.findHoliday(name, date) == None: # not duplicate
            holiday = h.Holiday(name, date)
            status = HolidayListObj.addHoliday(holiday)
            return status
        elif HolidayListObj.findHoliday(name, date) == 3:
            return 3
        else:
            return 2
    except:
        return 3


def removal(HolidayListObj):
    print(".----------------.\n| Remove Holiday |\n'----------------'")
    name = input('Holiday Name: ').lower()
    date = input('Holiday Date [yyyy-m-d]: ')
    status = HolidayListObj.removeHoliday(name, date)
    return status

def save(HolidayListObj):
    print(".-------------------.\n| Save Holiday List |\n'-------------------'")
    invalid = True
    while invalid == True:
        choice = input('Are you sure you want to save your changes? [Y/N]: ').lower()
        if choice == 'y':
            invalid = False
            HolidayListObj.save_to_json()
            print('Success! Changes have been saved as "listHolidays.json" in the current directory.')
            print('Returning to menu...')
        elif choice == 'n':
            invalid = False
            print('Canceled:\nHoliday list has not been saved.')
            print('Returning to menu...')
        else:
            print('Invalid entry - please enter Y or N')
            continue

def view(HolidayListObj):
    print(".---------------.\n| View Holidays |\n'---------------'")
    invalidYear = True
    while invalidYear == True:
        year = input('Year [1970-2030]: ')
        try:
            year = int(year)
            if year in range(1970, 2031):
                invalidYear = False
                totalWeeks = dt.datetime(year, 12, 28).isocalendar().week # get total number weeks for given year
                invalidWeek = True
                while invalidWeek == True:
                    week = input(f'Week [1-{totalWeeks}, Leave blank for current week]: ')
                    if week == '': # current week
                        invalidWeek = False
                        if year == dt.datetime.now().year: # current year
                            HolidayListObj.viewHolidays(year)
                            invalidChoice = True
                            while invalidChoice == True:
                                w = input('Would you like to see weather in Milwaukee, WI for this week? [Y/N]: ').lower()
                                if w == 'y':
                                    invalidChoice = False
                                    for item in HolidayListObj.getWeather():
                                        print(item)
                                    print('Returning to menu...')
                                elif w == 'n':
                                    print('Okay')
                                    print('Returning to menu...')
                        else: # different year
                            HolidayListObj.viewHolidays(year, week)
                            print('Returning to menu...')
                    else: # different week
                        try:
                            week = int(week)
                            if week in range(1, totalWeeks+1):
                                invalidWeek = False
                                HolidayListObj.viewHolidays(year, week) 
                                print('Returning to menu...')       
                        except: 
                            continue     
        except:
            print('Please enter a valid year [yyyy]')
            continue
        
def exit(HolidayListObj):
    print(".------.\n| Exit |\n'------'")
    try:
        with open('listHolidays.json') as infile:
            saved = infile.read()
    except:
        saved = 1
    lst = [holiday.__dict__() for holiday in HolidayListObj.innerHolidays]
    current = json.dumps(str(lst))
    return (saved, current)


    