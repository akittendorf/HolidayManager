# modules
import requests
from bs4 import BeautifulSoup as bs
import datetime as dt
import Holiday as h
# scraping url: https://www.timeanddate.com/holidays/us/
# credit for select_one() code on line 32:
# https://www.skytowner.com/explore/getting_nth_child_element_in_beautiful_soup#:~:text=To%20get%20the%202nd%20child%20element%20in%20Beautiful,get%20the%20second%20element%20under%20the%20div%20tag%3A

# functions
def getHTML(url): # takes a string url, returns HTML contents as text
    response = requests.get(url)
    html = response.text
    return html

def getSoup(html): # takes a string url, returns a soup object
    soup = bs(html, 'html.parser')
    return soup

def getHolidays(url, lst, year=2022, clas=h.Holiday): # takes a string url, a list to append, an int year, returns none
    if year < 2000 or year > 2030: # validate year
        print('Error: invalid year. This function expects a year between 2000 and 2030.')
        return 
    else:
        year = str(year) # convert year to string type   
        html = getHTML(url+year) # get html and append chosen year to url
        soup = getSoup(html) # turn html into soup object
        holiday_data = soup.tbody # store descendants of tbody tag 
        for entry in holiday_data:
            try:
                if entry.select_one(":nth-child(4)").text == 'Federal Holiday': # if type Federal Holiday 
                    name = entry.a.string.lower()
                    date = entry.th.string # date is bs4 object
                    date = str(date) # convert date to str
                    date = dt.datetime.strptime(f'{date}{year}', '%b %d%Y') # convert date string to date 
                    holiday = clas(name, date)
                    if holiday not in lst: # check for duplicates
                        lst.append(clas(name, date))
            except: 
                continue
        return 
