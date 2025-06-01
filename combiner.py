#!/usr/bin/env python3.11

import sys


# Student ID:3135194 

def emit():
    if current_title:
        # Only emit if count is not 0 to avoid division by zero error
        if count > 0:
            average_rating = sum_rating / count
            print(f"{current_year}\t{current_title}\t{average_rating}\t{count}")

current_year = None
current_title = None
sum_rating = 0.0
count = 0

for line in sys.stdin:
    parts = line.strip().split("\t")
    if len(parts) != 4:
        continue  # Skip malformed lines

    year, title, rating_str, count_str = parts

    try:
        rating = float(rating_str)
        increment_count = int(count_str)  # Count from the mapper, should always be 1 in this case
    except ValueError:
        continue  # Skip lines with invalid rating or count

    if year == current_year and title == current_title:
        sum_rating += rating * increment_count
        count += increment_count
    else:
        emit()  # Emit the average for the last movie before moving on to a new one
        current_year, current_title = year, title
        sum_rating = rating * increment_count  # Start summing ratings for the new movie
        count = increment_count  # Reset count for the new movie

# Emit for the last movie in the input
emit()
