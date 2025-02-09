"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilise any parameters and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""
import time
import csv 

def welcome():

    """
    Task 1: Display a welcome message.

    The welcome message should display the title 'Hotel Reviews'.
    The welcome message should contain dashes before and after the title.
    The number of dashes should be equivalent to the number of characters in the title.
    There should be a space between the dashes and the title i.e. a space before and after the title

    :return: Does not return anything.
    """


    title = "Hotel Reviews"
    print("-" * len(title))
    print(" " + title + " ")
    print("-" * len(title))

welcome()

def error(msg):
    """
    Task 2: Display an error message.

    The function should display a message in the following format:
    'Error! {error_msg}.'
    Where {error_msg} is the value of the parameter 'msg' passed to this function

    :param msg: a string containing an error message
    :return: does not return anything
    """

    print(f"Error!" + msg + ".")

error(msg= "{error_msg}")



def progress(operation, value):
    """
    Task 3: Display a message to indicate the progress of an operation.

    The function should display a message in the following format:
    'Operation: {operation} [{status}].'

    Where {operation} is the value of the parameter passed to this function
    and
    {status} is 'initiated' if the value of the parameter 'value' is 0
    {status} is 'in progress ({value}% completed)' if the value of the parameter 'value' is between,
    but not including, 0 and 100
    {status} is 'completed' if the value of the parameter 'value' is 100

    :param operation: a string indicating the operation being started
    :param value: an integer indicating the amount of progress made
    :return: does not return anything
    """



    if value == 0:
        status = "Loading initiated"
    elif value < 100:
        status = f"Loading in progress ({value}% completed)"
    elif value == 100:
        status = "Loading completed"
    print(f"Operation: {operation} [{status}].")
    time.sleep(1) 


for i in range(0, 101, 43 ):
    progress("Uploading Files", i)



def main_menu():
    """
    Task 4: Display the main menu and read the user's response.

    The following options should be displayed:

    '[1] Process Data', '[2] Visualise Data', '[3] Export Data' and '[4] Exit'

    In each of the above cases, the user's response should be read in and returned as an integer
    corresponding to the selected option.
    E.g. 1 for 'Process Data', 2 for 'Visualise Data' and so on.

    If the user enters a invalid option then a suitable error should be displayed and the user
    prompted to try again.

    :return: an integer for a valid selection
    """
    Option_count = 0
    Option_limit = 3
    out_of_option = False

    while True and not(out_of_option):
        print("Main Menu")
        print('[1] Process Data', '\n[2] Visualise Data', '\n[3] Export Data', '\n[4] Exit') 
        Option = int(input("Enter your choice: "))
        
        try:
            Option = int(Option)
            if Option in range(1,5):
                return Option
                Option_count += 1
           
            else:
                out_of_option = True
                break
                return main_menu
        except ValueError:
            print("Error! Invalid Choice")
            return main_menu

main_menu()



def sub_menu(variant):

    """
    Task 5: Display a sub menu of options and read the user's response.

    If no value or a zero is supplied for the parameter 'variant' then a suitable error should be displayed
    and the value 0 should be returned.

    If the value of the parameter 'variant' is 1 then a menu with the following options should be displayed:

    '[1] Reviews for Hotel', '[2] Reviews for Dates', '[3] Reviews for Nationality,
    '[4] Reviews Summary'

    If the value of the parameter 'variant' is 2 then a menu with the following options should be displayed:

    '[1] Positive/Negative Pie Chart', '[2] Reviews Per Nationality Chart', '[3] Animated Summary'

    If the value of the parameter 'variant' is 3 then a menu with the following options should be displayed:

    '[1] All Reviews', '[2] Reviews for Specific Hotel'

    In each of the above cases, the user's response should be read in and returned as an integer
    corresponding to the selected option.
    E.g. 1 for 'Reviews for Hotel', 2 for 'Reviews for Dates' and so on.

    If the user enters a invalid option then a suitable error message should be displayed

    :return: 0 if invalid selection otherwise an integer for a valid selection
    """

    if variant == 1:
        print('[1] Reviews for Hotel')
        print('[2] Reviews for Dates')
        print('[3] Reviews for Nationality')
        print('[4] Reviews Summary')
    elif variant == 2:
        print('[1] Positive/Negative Pie Chart')
        print('[2] Reviews Per Nationality Chart')
        print('[3] Animated Summary')
    elif variant == 3:
        print('[1] All Reviews')
        print('[2] Reviews for Specific Hotel')
    else:
        print("Please select Option 1 to 3")
        raise ValueError
        return 0

    Option = input ("Enter your choice: ")
      
    open("hotel_reviews.csv", "r")
    data = csv.reader ('path/to/file.csv')
    
    try:
        Option = int(input(Option))
        if (variant == 1 and Option in [1, 2, 3, 4]) or \
           (variant == 2 and Option in [1, 2, 3]) or \
           (variant == 3 and Option in [1, 2]):
           return Option
        else:
            print("Invalid choice. Please try again!")
            return sub_menu(variant)

    except ValueError:
        print("Invalid choice. Please select a valid option.")
        return sub_menu(variant)

sub_menu('variant')


def total_reviews(num_reviews):
    f"""
    Task 6: Display the total number of reviews in the data set.
    
    The function should display a message in the following format:

    "There are {num_reviews} reviews in the data set."

    Where {num_reviews} is the value of the parameter passed to this function
    
    :param num_reviews: the total number of reviews in the data set
    :return: Does not return anything
    """
    

    open("hotel_reviews.csv", "r")
    num_reviews = csv.count ('path/to/file.csv'[total_reviews])

    print(f'There are {num_reviews} reviews in the data set.')

total_reviews()

def hotel_name():
    """
    Task 7: Read in and return the name of a hotel.

    The function should ask the user to enter a hotel name e.g. Hotel Arena
    The function should then read in and return the user's response as a string.

    :return: the name of a hotel
    """
    

    hotel_name = input("Enter the hotel name: ")
    return hotel_name

hotel_name()


def review_dates():
    """
    Task 8: Read in and return a list of review dates.

    The function should ask the user to enter some review dates
    This should be entered in the format mm/dd/yyyy (same as that in the file)
    where dd is two-digit day, 
    mm is two digit month and 
    yyyy is a four digit year 
    e.g. 01/22/2020
    The function should return a list containing the specified review dates.

    :return: a list of review dates
    """
    

    Review_date = []
    while True:
        date = input("Please enter a review date in the format mm/dd/yyyy ")

        if date == "":
            break
        else: 
            open("hotel_reviews.csv", "r")
            csv.reader ('path/to/file.csv'[Review_date])
            review_dates.read(review_dates)
        print(date)
    return review_dates

review_dates()

def display_review(review, cols=None):
    """
    Task 9: Display a review. Only the data for the specified column indexes will be displayed.
    If no column indexes have been specified, then all the data for the review will be displayed.

    The parameter review is a list of values 
    e.g. ["08/03/2017", "Hotel Arena", "Russia", "I am so angry...", "Only the park...", 2.9,	7, "[' Leisure trip ', ' Couple ', ' Duplex Double Room ', ' Stayed 6 nights ']", "0 days"]
    [Note: in the above example, the ... is an ellipsis and is only included here as the text is long]

    The parameter cols is a list of column indexes e.g. [0,3,5]
    
    The function should display a list of values.
    The displayed list should only consist of those values whose column index is in cols.

    E.g. if cols is [1,3] then for the sample review above the following should be displayed:
    ["Hotel Arena", "I am so angry..."]

    E.g. if cols is [0,1,5] then for the sample review above the following should be displayed:
    ["08/03/2017", "Hotel Arena", 2.9]

    E.g. if cols is an empty list or None then all the values will be displayed
    ["08/03/2017", "Hotel Arena", "Russia", "I am so angry...", "Only the park...", 2.9,	7, "[' Leisure trip ', ' Couple ', ' Duplex Double Room ', ' Stayed 6 nights ']", "0 days"]

    :param review: A list of data values for a review
    :param cols: A list of integer values that represent column indexes
    :return: Does not return anything
    """
    
    
    open("hotel_reviews.csv", "r")
    review = csv.read.lines ('path/to/file.csv'[0, 1, 3, 4, 5, 6])
    
    if cols is None or not cols:
        print(review)

    else:
        print(next([review[i] for i in cols]))
display_review()


def display_reviews(reviews, cols):
    """
    Task 10: Display each review in the specified list of reviews.
    
    This function will display more than one review.
    Only the data for the specified column indexes will be displayed.
    If no column indexes have been specified, then all the data for a review will be displayed.

    The function should have two parameters as follows:

    reviews     which is a list of reviews where each reviews itself is a list of data values.
    cols        this is a list of integer values that represent column indexes.
    the default value for this is None.

    You will need to add these parameters to the function definition.

    The function should iterate through each review in reviews and display the relevant review data.

    Each review should be displayed as a list of values 
    e.g. ["08/03/2017", "Hotel Arena", "Russia", "I am so angry...", "Only the park...", 2.9,	7, "[' Leisure trip ', ' Couple ', ' Duplex Double Room ', ' Stayed 6 nights ']", "0 days"]
    
    Only the columns whose indexes are included in cols should be displayed for each review.

    If cols is an empty list or None then all values for the review should be displayed.

    :param reviews: A list of reviews
    :param cols: A list of integer values that represent column indexes
    :return: Does not return anything
    """
    for review in reviews:
        if cols is None or not cols:
            print(review)
        else:
            selected_data = [review[i] for i in cols]
            print(selected_data)


display_reviews()
