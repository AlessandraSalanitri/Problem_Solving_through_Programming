"""
This module is responsible for processing the data.  Each function in this module will take a list of reviews,
process it and return the desired result.
"""

"""
Task 16 - 20: Write suitable functions to process the data.

Each of the functions below should follow the pattern:
- Take a list of reviews (where each review is a list of data values) as a parameter.
- Process the list of reviews appropriately.  You may use the module 'tui' to retrieve any additional information 
required from the user to complete the processing.
- Return a suitable result

The required functions are as follows:
- Retrieve the total number of reviews that have been loaded.
- Retrieve the reviews for a hotel where the hotel name is specified by the user.
- Retrieve the reviews for the dates specified by the user.
- Retrieve all the reviews grouped by the reviewer’s nationality.
- Retrieve a summary of all the reviews. This should include the following information for each date in ascending order:
    - the total number of negative reviews on that date
    - the total number of positive reviews on that date
    - the average rating on that date
"""
import tui
import csv
import process

def retrieve_review_count(reviews):
    return len(reviews)

def retrieve_reviews_by_hotel(reviews):
    hotel_name = tui.get_hotel_name()
    reviews_by_hotel = process.filter_reviews_by_hotel(reviews, hotel_name)
    return reviews_by_hotel

def retrieve_reviews_by_dates(reviews):
    review_dates = tui.get_review_dates()
    reviews_by_dates = process.filter_reviews_by_dates(reviews, review_dates)
    return reviews_by_dates

def retrieve_reviews_by_nationality(reviews):
    grouped_reviews = process.group_reviews_by_nationality(reviews)
    return grouped_reviews

def retrieve_reviews_summary(reviews):
    summary = process.summarize_reviews(reviews)
    return summary
