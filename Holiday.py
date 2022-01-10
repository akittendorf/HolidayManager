import datetime as dt

class Holiday(object):
    def __new__(cls, name: str, date: dt.date):
        try:
            name = str(name).lower()
        except:
            print('Unable to create Holiday - name should be a str.')
            return 
        if isinstance(date, dt.datetime): # if datetime object
            date = date
            return object.__new__(cls)
        else:
            try:
                if type(date) == tuple: # if tuple
                    date = dt.datetime(*date)
                    return object.__new__(cls)
                else: # if str
                    date = dt.datetime.strptime(date, '%Y-%m-%d')
                    return object.__new__(cls)
            except: # all others
                print(f'Unable to create Holiday for {name} ({date})  - date should be a tuple (yyyy, m, d),datetime object, or str "yyyy-m-d".')
                return
    
    def __init__(self, name, date):
        self.__name = name
        if isinstance(date, dt.datetime): # if datetime object
            self.__date = date
        elif type(date) == tuple:
            self.__date = dt.datetime(*date)
        else:
            self.__date = dt.datetime.strptime(date, '%Y-%m-%d')

    def __str__ (self):
        return f'{self.__name} ({str(self.__date)[:10]})'

    def __repr__(self):
       return f'Holiday({self.__name}, {str(self.__date)[:10]})'
    
    def __dict__(self):
        return {'name': self.__name, 'date': str(self.__date)[:10]}
   
    @property
    def date(self):
        return self.__date
    
    @property
    def name(self):
        return self.__name
    