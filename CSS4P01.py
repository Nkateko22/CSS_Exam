# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 11:36:50 2024

@author: nkate
"""

import pandas as pd

file=pd.read_csv("C:/Users/nkate/Downloads/CSS_exam/movie_dataset.csv")

print(file)

print(file.columns)

print(file.isnull().sum())

missing_values = file[file['Metascore'].isnull()]
print(missing_values)

missing_values = file[file['Revenue (Millions)'].isnull()]
print(missing_values)

# Replace missing Metascore values with the mean
file['Metascore'].fillna(file['Metascore'].mean(), inplace=True)

# Replace missing Revenue values with the mean
file['Revenue (Millions)'].fillna(file['Revenue (Millions)'].mean(), inplace=True)

print(file)

# Assuming your DataFrame is named 'df'
rating_statistics = file['Rating'].describe()

print("Descriptive Statistics for the 'Rating' column:")
print(rating_statistics)

rating_max = file['Rating'].max()

# Assuming your DataFrame is named 'df' and 'Revenue (Millions)' is the column containing revenue
average_revenue = file['Revenue (Millions)'].mean()

print(f"The average revenue of all movies is: {average_revenue} million")


