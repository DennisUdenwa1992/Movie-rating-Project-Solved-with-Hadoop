#!/usr/bin/env python3.11

import sys


# Student ID:3135194


# Function to load years of interest
def load_years(file_path):
    years = set()
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Splitting each line by spaces and adding each year to the set
                for year in line.strip().split():
                    years.add(year)
    except FileNotFoundError:
        print("years.txt file not found.", file=sys.stderr)
    return years

# Load years from years.txt
years_of_interest = load_years("years.txt")


for line in sys.stdin:
    # Split the input line into its components
    parts = line.strip().split()
    if len(parts) < 5:
        continue  # Skip lines that don't have enough parts

    reviewer_id, movie_title, genres, year, rating = parts[0], " ".join(parts[1:-3]), parts[-3], parts[-2], parts[-1]

    # Split genres and emit each genre separately with the same rating
    for genre in genres.split("|"):
        # To check if the year is in the filtered years list, if years.txt is not empty
        if not years_of_interest or year in years_of_interest:
            # Emit year, movie_title, and rating
            print(f"{year}\t{movie_title}\t{rating}\t1")