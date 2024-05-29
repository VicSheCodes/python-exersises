import os

import pandas as pd


def analyze(factbook_pop: str, factbook_obesity: str) -> pd.DataFrame:
    # Read csv files using pandas function
    population = pd.read_csv(factbook_pop, usecols=["Name", "Value"])
    rate = pd.read_csv(factbook_obesity, usecols=["Name", "Value"])

    # Merge 2 dataframes by country name
    data = pd.merge(population, rate, on="Name")

    # Give names to dataframe columns
    data.columns = ["Country", "Population", "Obesity Rate"]

    # Filter data using given condition
    data_filter1 = data[data["Population"] > (10 ** 7)]
    data_filter2 = data_filter1[data_filter1["Obesity Rate"] > 20]

    # Sort Data using Obesity Rate Values
    data_sort = data_filter2.sort_values(by="Obesity Rate", ascending=0)

    # Get Top 10 Values
    top = data_sort.head(10)

    # Reset Index
    top.reset_index(inplace=True, drop=True)
    top.index += 1

    # Return Data Frame
    return top


path = os.path.join(os.path.dirname(__file__), 'data')
factbook_pop_path = os.path.join(path, 'c2119.csv')
factbook_obesity_path = os.path.join(path, 'c2228.csv')
print(path, factbook_pop_path, factbook_obesity_path)
print(analyze(factbook_pop_path, factbook_obesity_path))

# print(analyze('c2119.csv', 'c2228.csv'))
