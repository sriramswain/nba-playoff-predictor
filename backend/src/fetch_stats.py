import pandas as pd

def load_merged_stats():
    path = "backend/data/"

    # Load all CSV files into DataFrames
    standings = pd.read_csv(path + "expandedstandings.csv")
    per_game = pd.read_csv(path + "pergamestats.csv")
    per_100 = pd.read_csv(path + "per100poss.csv")
    advanced = pd.read_csv(path + "advancedstats.csv")
    shooting = pd.read_csv(path + "shootingstats.csv")

    # this code combines all the dataframes into one dataframe using the Team column as the key
    # similar to a SQL inner join
    df = standings \
        .merge(per_game, on="Team") \
        .merge(per_100, on="Team") \
        .merge(advanced, on="Team") \
        .merge(shooting, on="Team")
    
    print(df.columns)
    print(df.head())

    return df