My very first project created. 


⦁	Task 1: 
This code simply displays a welcome message through python print function.
It creates a variable in this case called "title" and assigns it the value "Hotel Reviews". 
Then, it uses the "*" operator to repeat the character "-" equal to the length of the title. Finally, it prints the dashes, the title with spaces before and after, and the dashes again.


⦁	Task 2: 
This code stores a string containing an error message inside a variable called “msg”. 
Then it uses string concatenation to combine the string "Error! " with the value of the "msg" parameter, and the string "." to create the final error message, and then prints it.

⦁	Task 3: 
The function takes in two parameters: "operation", which is a string indicating the operation being started, and "value", which is an integer indicating the amount of progress.
The function uses an if-elif statement to check the value of the "value" parameter and determine the appropriate status message to display. While checking if the value is 0, the loading results "initiated"; if the value is between 1 and 99, the loading is "in progress" with the percentage of completion included; and if the value is 100, the status is "completed". Finally, the function uses the print() function to display the message in the desired format.

⦁	Task 4: 
The function uses a while loop to repeatedly display the main menu options to the user until a valid selection is made. The options are displayed using the print() function. 
The function uses the input() function to read the user's response and stores it as a string in the variable "option". It then uses a try-except block to attempt to convert the "choice" string to an integer using the int() function. The function then uses an if statement to check if the choice is in the range of 1 to 4. If it is, the function returns the choice as an integer. If the choice is not in the range, or if the int() function raises a ValueError exception, the function prints an error message and continues to the next iteration of the while loop to prompt the user to try again for times 3 attempts.

⦁	Task 5: 
The function checks if the variant passed as a parameter is in the range of 1 to 3, if not it returns 0 and displays an error message. 
Then, it uses an if-elif statement to check the variant and display the corresponding options using the print() function.
The function uses the input() function to read the user's response and stores it as a string in the variable "choice". It then uses a try-except block to attempt to convert the "choice" string to an integer using the int() function.
The function then uses an if-elif statement to check if the choice is in the range of the corresponding variant. If it is, the function returns the choice as an integer. If the choice is not in the range, or if the int() function raises a ValueError exception, the function prints an error message and returns 0.

⦁	Task 6: 
The function takes in one parameter "num_reviews" which is the total number of reviews in the data set. With the “open” function, it opens the csv file where the number of reviews are, counts them and, finally uses the print() function to display the message in the desired format. It uses the f-string to insert the value of num_reviews in the message.
The function doesn't return anything, it just displays the message on the console.

⦁	Task 7: 

The function uses the input() function to ask the user to enter a hotel name and stores the response in a variable "hotel_name". It then returns the "hotel_name" variable as a string.


⦁	Task 8: 
The function uses a while loop to repeatedly ask the user to enter a review date in the specified format. The user can enter multiple dates, one at a time, until they are finished. The function open and reads from the csv files the dates and it prints it to the user.
When the user finishes the loop is broken and the function returns the list of dates. 


⦁	Task 9: 
The function takes in two parameters: "review" , a list of values for a review, and "cols", which is a list of column indexes.
The program first checks if cols is None or an empty list, if so it prints the entire review. If cols is not None or not empty it uses list comprehension to filter the values in the csv file and only print the values in the column index which is in cols. It doesn't return anything, it just displays the filtered values on the console.
In this function next is used to skip the first row that usually has the descriptive name of data.

⦁	Task 10: 
This function takes in two parameters, "reviews" and "cols". "reviews" is a list of reviews where each review itself is a list of data values, while "cols" is a list of integer values that represent column indexes. If no column indexes are specified, the default value is None.
The function iterates through each review in the "reviews" list, and checks if "cols" is None. If it is, it prints the entire review, otherwise, it uses list comprehension to select the columns whose indexes are included in "cols" and assigns it to the selected_data variable. The selected_data is then printed.

⦁	Process

Explain the functionality implemented in this module. Relevant guidelines mentioned in the previous section should also be followed here. If you have added additional functions (e.g. to improve code readability and reuse) or utilised additional constructs (e.g. exception handling) then this should be discussed here.


⦁	Task 11:
For this module process, 5 functions to process the data are created:
retrieve_review_count function takes a list of reviews as a parameter and returns the total number of reviews.
retrieve_reviews_by_hotel function takes a list of reviews as a parameter, prompts the user to enter a hotel name using the get_hotel_name function of the tui module, and returns a list of reviews for that hotel using the filter_reviews_by_hotel function of the process module. 
retrieve_reviews_by_dates function takes a list of dates review as a parameter, prompts the user to enter a dates using the get_review_dates function of the tui module, and returns a list of review dates using the filter_review_by_dates.
Retrieve_reviews_by_nationality function takes a list of review as a parameter, prompts the user to enter a nationality using the group_reviews_by_nationality from the tui module and, return a list of grouped_reviews_by_nationality.
Retrieve_reviews_summary function takes a list of review as a parameter and return summary reviews when the option is execute.



⦁	Visual

Explain the functionality implemented in this module. Relevant guidelines mentioned in the previous sections should also be followed here.  You should include suitable screenshots of the final visualisations.

If you have developed additional modules then you should include an additional sub-section here related the additional modules.
⦁	
⦁	
⦁	 Task 22-24:

In this visual.py module, a pie chart with positive and negative review is required.
In order to create a chart, the csv “hotel_review” file is imported, along with matplotlib.pyplot and animation. 
Matplotlib.pyplot is a sub library within the matplotlib library in Python, which provides a convenient interface for plotting and visualization. It allows users to create various types of charts, plots, and other visualizations based on their data, including line plots, scatter plots and bar charts. With matplotlib.pyplot, users can easily customize aspects of their visualizations, such as colors, labels, and axis ranges, and save or display their plots.
The import matplotlib.animation as animation statement is importing the animation module from the matplotlib library. The matplotlib.animation module provides classes and functions for creating animations using Matplotlib. The as animation part of the statement is renaming the module as animation for easier use in the cod


In the first pie chart code, the autopct argument specifies the format of the value labels on each pie slice. The %1.1f%% format will display the values as floating point numbers with 1 digit after the decimal point and with a percent sign at the end. The startangle argument specifies the angle in degrees at which the first pie slice will be drawn. A value of 90 will start the first slice at the top of the chart.

In the code for the bar chart, the line nationalities = sorted(nationalities.items(), key=lambda x: x[1], reverse=True) sorts the nationalities dictionary based on the number of reviews for each nationality. The key argument to the sorted function specifies a custom sorting key. In this case, it is a lambda function that takes a tuple (nationality, count) and returns count, so that the dictionary is sorted based on the number of reviews. The reverse argument is set to True to sort the dictionary in descending order, so that the nationalities with the most reviews are displayed first.

The last function uses the Matplotlib animation module to create an animated line graph that shows how the number of positive and negative reviews, as well as the average rating, change over time. The animation is displayed using the plt.show() function.



⦁	Main

Explain the functionality implemented in this module. Relevant guidelines mentioned in the previous sections should also be followed here.  It may be useful to include an example or two of how the main module utilises the other modules to deliver a function.  You may, for example, present this as a diagram or a series of annotated function calls.


⦁	Task 11: 
In python exist a keyword called “import” which will import external files into your python program file or folder. For the final result of this “main” module: “hotel_review.csv”, ”process module”, “visual module”, “tui module” have been imported.
Finally, the program has created an empty list used to store the data read from the source data file. 

⦁	Task 12:
Importing function from module to module is beneficial when creating a project and you want to use a variable or a function previously created in another module. Python allows you to import that specific function or variable inside another project or another module.
In this task, in order to import the function welcome that was previously created in “tui” model, we need to call the file where the function is and add the function name that we want to use: 
        tui.welcome()
The next(csv_reader) function is used to skip the first row of the file, which is assumed to be the header row.


⦁	Task 13:
This function uses the TUI module to display messages indicating when the data loading operation starts and when it's completed, and how many reviews have been loaded. It also uses the python's built-in open() function to read the reviews.csv file, using a try-except block to handle the case where the file cannot be found or loaded. 

⦁	Task 14 and 15.
To complete Task 14 and Task 15, it is required to import a function from the "tui" module, to display the main menu, return the user's selection and, assign the return value to a variable.
Then, thanks to a series of if-elif statements create to check the user's choice and perform the appropriate requested actions. Depending on the user's selection, other functions from the "tui" and "process" modules are used to display messages, retrieve reviews, group reviews, and summarize reviews.


⦁	Task 21
In this example, after main menu is selected and if the selected option is 2(Visualise Data) tui.display_message("Visualizing data...") is called which will display a message indicating that the data visualisation operation has started.Then tui.display_sub_menu(2) is called which will display a sub-menu of options for visualising the data(menu variant 2) and returns the selected option.
Based on the selected option, appropriate function is called from the visual module to display the visual and the results are displayed using the appropriate functions in the tui module. The final tui.display_message("Data visualization completed.") will indicate that the data visualisation operation has completed.


⦁	Task 25 
In this example, a base class ReviewExporter with two methods export_all_reviews and export_reviews_by_hotel which will be overridden by the child class JSONReviewExporter. The child class JSONReviewExporter implements the abstract methods of the base class ReviewExporter and exports the reviews to a JSON file.
In the run() function, after main menu is selected and if the selected option is 3(Export Data) JSONReviewExporter(reviews_data) object is created and after sub menu is selected and based on the selected option, appropriate method of the object is called which will export the reviews to a JSON file.
This way, we can create different classes for exporting reviews to different formats (e.g CSV, Excel, PDF, etc.) and use appropriate class to export the reviews based on the requirements.


⦁	Task 26:
In the above code snippet, after the main menu is displayed, the selected option is assigned to the variable main_menu_option. Then, using an infinite while loop, the program checks if the selected option is 4 (Exit). If it is, it displays a message "Exiting program..." and breaks out of the loop, terminating the program.

           while True:
               main_menu_option = tui.display_main_menu()
               if main_menu_option == 4:
                   tui.display_message("Exiting program...")
                   break

⦁	Task 27:
After the main menu is displayed, the selected option is assigned to the variable main_menu_option. Then, using an infinite while loop, the program checks if the selected option is 1, 2, 3, or 4. If it is any of these, it proceeds with the corresponding task (processing, visualising, exporting data, or exiting the program). If the selected option is none of these, it calls the appropriate function of the module tui to display an error message "Invalid option selected. Please try again." And return in main menu option which display the main menu.
