
"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done using the appropriate functions in the module 'tui'
        any processing should be done using the appropriate functions in the module 'process'
        any visualisation should be done using the appropriate functions in the module 'visual'
"""


# Task 11: Import required modeules and create an empty list named 'reviews_data'.
# This will be used to store the data read from the source data file.

import csv 

reviews_data = []

def run():
    # Task 12: Call the function welcome of the module 'tui'.
    # This will display our welcome message when the program is executed.
 import process  
 import visual 
 import tui as tui

 tui.welcome()



    # Task 13: Load the data.
    # - Use the appropriate function in the module 'tui' to display a message to indicate that the data loading
    # operation has started.
    # - Load the data. Each line in the file should represent a review in the list 'reviews_data'.
    # You should appropriately handle the case where the file cannot be found or loaded.
    # - Use the appropriate functions in the module 'tui' to display a message to indicate how many reviews have
    # been loaded and that the data loading operation has completed.

 
 tui.display_message("Loading data...")
 try:
    with open('reviews.csv', 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader) # Skip the header row with labels
        for row in csv_reader:
            reviews_data.append(row)
    tui.display_num_reviews(len(reviews_data))
    tui.display_message("Data loaded.")



 # Task 14: Using the appropriate function in the module 'tui', display the main menu
        # Assign the value returned from calling the function to a suitable local variable
 # Task 15: Check if the user selected the option for processing data.  If so, then do the following:
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has started.
        # - Process the data (see below).
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has completed.
        #
        # To process the data, do the following:
        # - Use the appropriate function in the module 'tui' to display a sub-menu of options for processing the data
        # (menu variant 1).
        # - Check what option has been selected
        #
        #   - If the user selected the option to retrieve reviews by hotel name then
        #       - Use the appropriate function in the module 'tui' to indicate that the review retrieval process
        #       has started.
        #       - Use the appropriate function in the module 'process' to retrieve the review and then appropriately
        #       display it.
        #       - Use the appropriate function in the module 'tui' to indicate that the review retrieval process has
        #       completed.
        #
        #   - If the user selected the option to retrieve reviews by review dates then
        #       - Use the appropriate function in the module 'tui' to indicate that the reviews retrieval
        #       process has started.
        #       - Use the appropriate function in the module 'process' to retrieve the reviews
        #       - Use the appropriate function in the module 'tui' to display the retrieved reviews.
        #       - Use the appropriate function in the module 'tui' to indicate that the reviews retrieval
        #       process has completed.
        #
        #   - If the user selected the option to group reviews by nationality then
        #       - Use the appropriate function in the module 'tui' to indicate that the grouping
        #       process has started.
        #       - Use the appropriate function in the module 'process' to group the reviews
        #       - Use the appropriate function in the module 'tui' to display the groupings.
        #       - If required, you may add a suitable function to the module 'tui' to display the groupings
        #       - Use the appropriate function in the module 'tui' to indicate that the grouping
        #       process has completed.
        #
        #   - If the user selected the option to summarise the reviews then
        #       - Use the appropriate function in the module 'tui' to indicate that the summary
        #       process has started.
        #       - Use the appropriate function in the module 'process' to summarise the reviews.
        #       - Add a suitable function to the module 'tui' to display the summary
        #       - Use your function in the module 'tui' to display the summary
        #       - Use the appropriate function in the module 'tui' to indicate that the summary
        #       process has completed.

    selected_option = tui.display_main_menu()
    if selected_option == 1:
        tui.display_message("Processing data...")
        variant_selected = tui.display_sub_menu(1)
    if variant_selected == 1:
        tui.display_message("Retrieving reviews by hotel name...")
        hotel_name = tui.get_hotel_name()
        reviews = process.get_reviews_by_hotel(reviews_data, hotel_name)
        tui.display_reviews(reviews)
        tui.display_message("Review retrieval completed.")
    elif variant_selected == 2:
        tui.display_message("Retrieving reviews by dates...")
        review_dates = tui.get_review_dates()
        reviews = process.get_reviews_by_dates(reviews_data, review_dates)
        tui.display_reviews(reviews)
        tui.display_message("Review retrieval completed.")
    elif variant_selected == 3:
        tui.display_message("Grouping reviews by nationality...")
        groupings = process.group_reviews_by_nationality(reviews_data)
        tui.display_reviews_by_nationality(groupings)
        tui.display_message("Grouping completed.")
    elif variant_selected == 4:
        tui.display_message("Summarising reviews...")
        summary = process.summarize_reviews(reviews_data)
        tui.display_reviews_summary(summary)
        tui.display_message("Summary completed.")
    else:
        tui.display_message("Invalid selection.")
        tui.display_message("Data processing completed.")
 except FileNotFoundError:
        tui.display_message("Error: Could not find the file.")
 except:
        tui.display_message("Error: Could not load the data.")

        # Task 21: Check if the user selected the option for visualising data.
        # If so, then do the following:
        # - Use the appropriate function in the module 'tui' to indicate that the data visualisation operation
        # has started.
        # - Visualise the data by doing the following:
        #   - call the appropriate function in the module 'tui' to determine what visualisation is to be done.
        #   - call the appropriate function in the module 'visual' to display the visual
        # - Use the appropriate function in the module 'tui' to display a message to indicate that the
        # data visualisation operation has completed.
        if selected_option == 2:
            tui.display_message("Visualizing data...")
            variant_selected = tui.display_sub_menu(2)
        if variant_selected == 1:
            tui.display_message("Displaying Positive/Negative Pie Chart...")
            visual.display_positive_negative_pie_chart(reviews_data)
        elif variant_selected == 2:
            tui.display_message("Displaying Reviews Per Nationality Chart...")
            visual.display_reviews_per_nationality_chart(reviews_data)
        elif variant_selected == 3:
            tui.display_message("Displaying Animated Summary...")
            visual.display_animated_summary(reviews_data)
        else:
            tui.display_message("Invalid selection.")
        tui.display_message("Data visualization completed.")

       
        
        # Task 25: Check if the user selected the option for exporting reviews.  If so, then do the following:
        # - Use the appropriate function in the module 'tui' to retrieve what reviews are to be exported.
        # - Check what option has been selected
        #
        # - Use the appropriate function in the module 'tui' to indicate that the export operation has started.
        # - Export the reviews (see below)
        # - Use the appropriate function in the module 'tui' to indicate that the export operation has completed.
        #
        # To export the reviews, you should demonstrate the application of OOP principles including the concepts of
        # abstraction and inheritance.  You should create suitable classes with appropriate methods.
        # You should use these to write the reviews (either all or only those for a specific country/region) to a JSON file.       



class ReviewExporter:
    def __init__(self, reviews_data):
        self.reviews_data = reviews_data

    def export_all_reviews(self, file_name):
        pass

    def export_reviews_by_hotel(self, hotel_name, file_name):
        pass

class JSONReviewExporter(ReviewExporter):
    def export_all_reviews(self, file_name):
        # code to export all reviews to a JSON file
        pass

    def export_reviews_by_hotel(self, hotel_name, file_name):
        # code to export reviews for a specific hotel to a JSON file
        pass

def run():
    import tui as tui
    
    selected_option = tui.display_main_menu()
   
    exporter = JSONReviewExporter(reviews_data)
    if selected_option == 3:
        tui.display_message("Exporting Data...")
        variant_selected = tui.display_sub_menu(3)
    if variant_selected == 1:
        tui.display_message("Exporting All Reviews...")
        exporter.export_all_reviews("reviews.json")
    elif variant_selected == 2:
        hotel_name = tui.get_hotel_name()
        tui.display_message(f"Exporting Reviews for {hotel_name}...")
        exporter.export_reviews_by_hotel(hotel_name, "reviews.json")
    else:
        tui.display_message("Invalid selection.")
        tui.display_message("Data Export completed.")

        # Task 26: Check if the user selected the option for exiting the program.
        # If so, then break out of the loop

    while True:
        main_menu_option = tui.display_main_menu()
        if main_menu_option == 4:
            tui.display_message("Exiting program...")
            break

        # Task 27: If the user selected an invalid option then use the appropriate function of the
        # module tui to display an error message
        else:
            print("Error! The option selected is not valid!")

if __name__ == "__main__":
    run()
