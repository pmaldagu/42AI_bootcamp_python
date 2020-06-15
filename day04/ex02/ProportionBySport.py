import pandas as pd
from FileLoader import FileLoader

def proportionBySport(data, year, sport, sex):
    new = data[data['Sex'] == sex]
    new = new[new['Year'] == year].drop_duplicates('Name')
    total = len(new)
    new = new[new['Sport'] == sport]
    print(len(new) / total)

if __name__ == "__main__":
    path = "./athlete_events.csv"
    fl = FileLoader()
    df = fl.load(path)
    print(proportionBySport(df, 2004, 'Tennis', 'F'))
