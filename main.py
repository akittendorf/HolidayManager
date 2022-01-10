import Holiday as h
import HolidayList as hl    
import uiFunctions as f

def main():
    print(".-----------------.\n| Holiday Manager |\n'-----------------'")
    print('Starting up...')
    with open('menuText.txt') as infile: # read in menu text from txt file and save as menuText
        menuText = infile.read()
    holidays = hl.HolidayList() # initialize HolidayList obj
    holidays.read_json('holidays.json') # load starter holidays from holidays.json
    holidays.scrapeHolidays() # scrape current year +- 2 years' holiday data
    print('Base holidays loaded.')
    print(f'There are {holidays.numHolidays()} holidays stored in the system.')
    exited = False
    while exited == False:
        invalidChoice = True
        while invalidChoice == True:
            print(menuText)
            choice = input('What would you like to do? Enter a number [1-5]: ')
            if choice not in [str(i) for i in range(1,6)]:
                print('Invalid entry - please enter a number 1 - 5.')
                continue
            else:
                invalidChoice = False
                if choice == '1': 
                    status = f.addition(holidays)
                    if status == 1:
                        print('Success! The holiday has been added.')
                        continue
                    elif status == 2:
                        print('That holiday is already in the list.')
                        print('Returning to menu...')
                        continue
                    elif status == 3:
                        print('Invalid entry - please follow the provided date format [yyyy-m-d].')
                elif choice == '2':
                    status = f.removal(holidays)
                    if status == True:
                        print('Success! The holiday has been removed.')
                    else:
                        print('Holiday not found.')
                    continue
                elif choice == '3':
                   f.save(holidays) 
                elif choice == '4':
                    f.view(holidays)
                elif choice == '5':
                    comparison = f.exit(holidays)
                    invalid = True
                    while invalid == True:
                        if comparison[0] != comparison[1]:
                            print('You have unsaved changes that will be lost if you exit.')
                        else:
                            pass
                        choice = input('Are you sure you want to exit? [Y/N]: ').lower()
                        if choice == 'y':
                            invalid = False
                            print('Goodbye!')
                            exited = True
                            break
                        elif choice == 'n':
                            invalid = False
                            print('Okay. Returning to menu...')
                            continue
                        else:
                            print('Invalid entry - please enter Y or N')
                            continue

if __name__ == "__main__":
    main()
