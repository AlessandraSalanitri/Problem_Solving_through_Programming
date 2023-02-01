"""
This module is responsible for visualising the data using Matplotlib.
"""

"""
Task 22 - 24: Write suitable functions to visualise the data as follows:

- Display a pie chart showing the total number of positive and negative reviews for a specified hotel.
- Display the number of reviews per the nationality of a reviewer. This should by ordered by the number of reviews, highest first, and should show the top 15 + “Other” nationalities.
- Display a suitable animated visualisation to show how the number of positive reviews, negative reviews and the average rating change over time.

Each function should visualise the data using Matplotlib.
"""

import matplotlib.animation as animation
import csv
import matplotlib.pyplot as plt

def plot_pie_chart_for_hotel(hotel_name):
    pos_count = 0
    neg_count = 0
    with open("hotel_reviews.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["hotel_name"] == hotel_name:
                if row["review_type"] == "positive":
                    pos_count += 1
                elif row["review_type"] == "negative":
                    neg_count += 1
    labels = ['Positive', 'Negative']
    sizes = [pos_count, neg_count]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
plt.show()

def plot_reviews_per_nationality():
    nationalities = {}
    with open("hotel_reviews.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            nationality = row["nationality"]
            if nationality in nationalities:
                nationalities[nationality] += 1
            else:
                nationalities[nationality] = 1

    # sort the nationalities by the number of reviews
    nationalities = sorted(nationalities.items(), key=lambda x: x[1], reverse=True)
    # get the top 15 nationalities and sum the rest as "Other"
    top_15 = nationalities[:15]
    other = sum([item[1] for item in nationalities[15:]])
    if other > 0:
        top_15.append(("Other", other))
    # plot the bar chart
    names, values = zip(*top_15)
    plt.barh(names, values)
    plt.xlabel("Number of Reviews")
    plt.ylabel("Nationality")
plt.show()


def animate_reviews_over_time():
    reviews = {}
    with open("hotel_reviews.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            date = row["date"]
            if date in reviews:
                review = reviews[date]
                if row["review_type"] == "positive":
                    review[0] += 1
                elif row["review_type"] == "negative":
                    review[1] += 1
                review[2] += float(row["rating"])
                review[3] += 1
            else:
                if row["review_type"] == "positive":
                    reviews[date] = [1, 0, float(row["rating"]), 1]
                elif row["review_type"] == "negative":
                    reviews[date] = [0, 1, float(row["rating"]), 1]
    
    dates = sorted(reviews.keys())
    pos_reviews = []
    neg_reviews = []
    avg_ratings = []
    for date in dates:
        review = reviews[date]
        pos_reviews.append(review[0])
        neg_reviews.append(review[1])
        avg_ratings.append(review[2] / review[3])
    
    fig, ax = plt.subplots()
    ax.set_xlabel("Date")
    ax.set_ylabel("Count")
    ax.set_ylim(0, max(pos_reviews + neg_reviews + avg_ratings))
    ax.set_title("Positive and Negative Reviews and Average Rating Over Time")
    line1, = ax.plot([], [], label="Positive Reviews")
    line2, = ax.plot([], [], label="Negative Reviews")
    line3, = ax.plot([], [], label="Average Rating")
    ax.legend(loc="upper left")
    ax.grid()

    def animate(i):
        line1.set_data(dates[:i], pos_reviews[:i])
        line2.set_data(dates[:i], neg_reviews[:i])
        line3.set_data(dates[:i], avg_ratings[:i])
        return line1, line2, line3

    ani = animation.FuncAnimation(fig, animate, frames=len(dates), interval=200, blit=True)
    plt.show()

















































































































































































































































































































































































































































































































































































































