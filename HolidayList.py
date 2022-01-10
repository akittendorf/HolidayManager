import datetime as dt
import json
import scraping as s
import Holiday as h
import weather as w

# -------------------------------------------
# The HolidayList class acts as a wrapper and container
# For the list of holidays
# Each method has pseudo-code instructions
# --------------------------------------------
class HolidayList:
    def __init__(self):
       self.innerHolidays = []
   
    def addHoliday(self, holidayObj): # takes a Holiday, returns none, has side effects on self.innerHolidays
        if isinstance(holidayObj, h.Holiday): # validate holidayObj type
            self.innerHolidays.append(holidayObj) # append self.innerHolidays
            return 1 # indicate success
        else:
            return 3 # indicate error

    def findHoliday(self, name, date):
        try:
            name = name.lower()
            date = dt.datetime.strptime(date, '%Y-%m-%d')
            for holiday in self.innerHolidays:
                if holiday.name == name and holiday.date == date: # in list
                    return h.Holiday(name, date)
                else:
                    continue
            return None
        except: # error
            return 3

    def removeHoliday(self, name, date):
        holiday = self.findHoliday(name, date) # try to find holiday
        if holiday != None and holiday != 3: # if holiday found
            for day in self.innerHolidays:
                if holiday.name == day.name and holiday.date == day.date:
                    self.innerHolidays.remove(day) # remove holiday from innerHolidays
            return True # indicate success
        else:
            return False # indicate failure

    def read_json(self, file):
        with open(file) as infile:
            jsonObj = json.load(infile)
        for x in jsonObj['holidays']: # where x is an item in the jsonObj['holidays'] list
            holiday = h.Holiday(x['name'], x['date'])
            self.addHoliday(holiday)
            
    def save_to_json(self, filename='listHolidays.json'):
        lst = [holiday.__dict__() for holiday in self.innerHolidays]
        jsonObj = json.dumps(str(lst))
        with open(filename, 'w') as outfile:
            outfile.write(jsonObj)
        
    def scrapeHolidays(self, year=dt.datetime.now().year):
        for i in range(year-2, year+3): # get range of 5 years
            try:
                s.getHolidays('https://www.timeanddate.com/holidays/us/', self.innerHolidays, i)
            except:
                continue 
        return   

    def numHolidays(self):
        return len(self.innerHolidays)
    
    def filterHolidays(self, year=dt.datetime.now().year, weekNumber=dt.datetime.now().isocalendar().week):
        holidays = filter(lambda x: x.date.isocalendar().week == weekNumber and x.date.year == year, self.innerHolidays) # lambda filter
        holidays = list(holidays) # cast as list
        return holidays # return list

    def displayHolidays(self, holidays):
        for holiday in holidays: # iterate through list
            print(holiday) # print each item
        if holidays == []:
            print('No holidays found in this week.')
        return

    def getWeather(self):
        dates = w.stringDate() # returns tuple of (start, end)
        try:
            weather = w.getWeather(dates[0], dates[1]) # returns list of weather tuples (date, condition)
        except:
            weather = [] # empty list
        return weather

    def viewHolidays(self, year=dt.datetime.now().year, weekNumber=dt.datetime.now().isocalendar().week):
        filteredHolidays = self.filterHolidays(year, weekNumber)
        self.displayHolidays(filteredHolidays)
    
    def viewCurrentWeather(self):
        forecasts = w.getWeather()
        for forecast in forecasts:
            print(f"{forecast[0]} - {forecast[1]}")
            
        
        # Use your displayHolidaysInWeek function to display the holidays in the week
        # Ask user if they want to get the weather
        # If yes, use your getWeather function and display results