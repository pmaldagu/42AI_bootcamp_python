import pandas as pd
from FileLoader import FileLoader

def howManyMedalsByCountry(data, name):
    new = data[data['Team'] == name]
    for games in new['Games']:
         new['Medal'].drop_duplicates() 
    new_dico = {}
    for year in new['Year'] :
        new_dico[year] = {'G': 0, 'S': 0, 'B': 0}
    for year, medal in zip(new['Year'], new['Medal']) :
        if medal == 'Gold' :
            new_dico[year]['G'] += 1
        if medal == 'Silver' :
            new_dico[year]['S'] += 1
        if medal == 'Bronze' :
            new_dico[year]['B'] += 1
    return(new_dico)


if __name__ == "__main__":
    path = "./athlete_events.csv"
    fl = FileLoader()
    df = fl.load(path)
    print(howManyMedalsByCountry(df, "Norway"))
