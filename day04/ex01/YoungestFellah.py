import pandas as pd
from FileLoader import FileLoader

def youngestFellah(df, year):
    new_dic = {}
    test = df.loc[df['Year'] == year]
    new_dic['f'] = test['Age'].loc[df['Sex'] == 'F'].min()
    new_dic['m'] = test['Age'].loc[df['Sex'] == 'M'].min()
    print (new_dic)

if __name__ == "__main__":
    path = "./athlete_events.csv"
    fl = FileLoader()
    df = fl.load(path)
    youngestFellah(df, 2004) 
