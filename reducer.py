#!/usr/bin/env python3

# Student ID: 3135194

import sys
from decimal import Decimal
from collections import defaultdict

min_votes = 10

def process_movies(movies):
    # Calculate the average rating for each movie in a year
    for movie, values in movies.items():
        total_rating, count = values
        if count >= min_votes:  # Ensure movie has at least min_votes
            average_rating = total_rating / count
            yield movie, average_rating

# Dictionary to hold year, movie title and their ratings and count
movies_data = defaultdict(lambda: defaultdict(lambda: [0, 0]))  # year -> movie -> [total_rating, count]

for line in sys.stdin:
    parts = line.strip().split("\t")
    if len(parts) == 4:  # Adjusted to expect 4 parts: year, movie_title, rating, count
        year, movie_title, rating, count = parts
        rating = float(rating)
        count = int(count)
    else:
        continue  # Skip lines that do not conform to expected format

    # Aggregate ratings and counts
    movies_data[year][movie_title][0] += rating * count  # Use rating * count for weighted sum
    movies_data[year][movie_title][1] += count

for year in sorted(movies_data.keys()):
    # Find the movie(s) with the highest average rating for each year
    movies = movies_data[year]
    highest_avg_rating = 0
    best_movies = []

    for movie, avg_rating in process_movies(movies):
        if avg_rating > highest_avg_rating:
            highest_avg_rating = avg_rating
            best_movies = [movie]
        elif avg_rating == highest_avg_rating:
            best_movies.append(movie)

    for movie in best_movies:
        print(f"{year}\t{movie}\t{Decimal(highest_avg_rating).quantize(Decimal('0.01'))}")