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

import matplotlib.pyplot as plt
import numpy as np
import csv


data = np.read_csv('path/to/file.csv')

Positive_Reviews = data['Positive_Reviews']
Negative_Reviews = data['Negative_Reviews']


plt.pie(Positive_Reviews , Negative_Reviews, labels = Positive_Reviews + Negative_Reviews)

plt.show()
