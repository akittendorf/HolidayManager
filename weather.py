import requests
import config
import datetime as dt
import time

def stringDate(date=dt.datetime.now(), delta=6): # takes in datetime.datetime object, timedelta int, returns tuple of start and end date strings
    end = str(date)[:10]
    start = str(date-dt.timedelta(delta))[:10]
    return start, end
    
def getWeather(start, end, api_key=config.api_key): # takes api_key and Unix int, 
    url = "https://weatherapi-com.p.rapidapi.com/history.json"
    querystring = {"q":"Milwaukee","dt":f"{start}","lang":"en","end_dt":f"{end}"}
    headers = {
        'x-rapidapi-host': "weatherapi-com.p.rapidapi.com",
        'x-rapidapi-key': f"{api_key}" # api_key is stored in a config.py file and not revealed for security reasons
        }
    response = requests.request("GET", url, headers=headers, params=querystring).json()
    # print(response.text)
    weather = [] # initialize weather list to store weather tuples
    for day in response['forecast']['forecastday']:#
        weather.append((day['date'],day['day']['condition']['text'].lower()))
    return weather

# # test
# dates = stringDate()
# print(type(dates[0]))
# weather = getWeather(dates[0], dates[1])
# print(type(weather[0][0]))
# print(weather)
