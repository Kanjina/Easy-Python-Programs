# Import from the newly renamed official package
from ddgs import DDGS

searching_internet = True
reminders = True
variable = True

#This function prints out reminders to the user.
def print_reminders(reminders):
    if reminders == True:
        print("Note that you can't print more than 50 results")
        print('To exit the program, type in "exit"')
        print('To stop seeing these reminders, type in "stop"')
    else:
        print('Type in "remind" to print reminders')

#This checks if the user inputted number of search results is valid.
def is_valid_number(number):
    global searching_internet
    global reminders
    try:
        number = int(number)
        if number <= 50:
            return int(number)
        else:
            print("Please choose a number less than 50!")
            return 0
    except ValueError:
        if number.lower() == "stop":
            reminders = False
            return 0
        elif number.lower() == "remind":
            reminders = True
            return 0
        elif number.lower() == "exit":
            searching_internet = False
        else:
            print("Please choose an integer")
            return 0

#Internet searching function
def search_internet(query_string, max_results):
    print(f"Searching the internet for: '{query_string}'...\n")
    try:
        # Perform the search securely
        with DDGS() as ddgs:
            # Note: max_results must be a keyword argument
            results = ddgs.text(query_string, max_results=max_results)
            
            for i, result in enumerate(results, start=1):
                print(f"{i}. {result['title']}")
                print(f"   Link: {result['href']}\n")
                
    except Exception as e:
        print(f"An error occurred: {e}")

# Running the search in a while loop
while searching_internet == True:
    print_reminders(reminders)
    string_to_find = str(input("Enter what you want to search for: "))
    variable = True
    while variable == True:
        max_results = input("Enter how many results you want to display: ")
        result = is_valid_number(max_results)
        if result <= 50:
            search_internet(string_to_find, result)
            variable = False