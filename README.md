# HolidayManager
WHAT:
This project creates a text-based Holiday Manager that allows the user to store and modify a list of holidays and save this list as a JSON file. Techniques included in this project include: file i/o, classes, lambda, webscraping, API usage.

MAINTENANCE:
This was created for an assignment and will likely not be updated after 1/10/2022.

REPOSITORY FILES:
README.md                 
.gitignore
plan.txt    
startercode.py    
 holidays.json
 Holiday.py
 HolidayList.py
 scraping.py
 weather.py
 main.py
 menuText.txt
 uiFunctions.py
 listHolidays.json               

MODULES USED:
bs4
requests
datetime
json

DESIGN:
startercode.py and holidays.json were provided in the assignment details.
plan.txt is the basic approach to the project and is found in the "plans" folder.
Holiday.py and HolidayList.py contain the class definitions and methods for the Holiday and HolidayList classes, respecively.
HolidayList acts as a wrapper and container for a list of holidays.
scraping.py contains code to scrape holiday data from https://www.timeanddate.com/holidays/us/.
weather.py contains code to get weather data from https://rapidapi.com/weatherapi/api/weatherapi-com/. 
main.py contains code for the UI text and flow of the application as a whole. It synthesizes nearly all the files.
menuText.txt contains the string for the main menu used in main.py.
uiFunctions.py contains code that connects Holiday.py, HolidayList.py, scraping.py, and weather.py to main.py.
listHolidays.json is a sample list of holidays that can be saved by this application.

USAGE:
All files should be loaded into the same directory and the application should be run from the directory in which the output listHolidays.json should be saved. As is currently written, webscraping is only performed once during set up of the application to gather the current year's federal holidays plus 2 years' prior and 2 years' after data, for a total of 5 years of federal holiday data. Using the command line, the user may choose to add, remove, or view holidays, as well as save the current list to listHolidays.json and exit the program. With the free subscription to the weatherapi, weather data can only be gathered for the current week. 

*NOTE* an api_key is required in order for weather.py to function. My personal api_key was contained in a config.py file that was not pushed to github for confidentiality reasons. An api_key can currently be obtained for free by visiting the api. *END NOTE*