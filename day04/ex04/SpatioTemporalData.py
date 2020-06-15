import pandas as pd
from FileLoader import FileLoader

class SpatioTemporalData:
    def __init__(self, df):
        self.df = df

    def when(self, location):
        lst = []
        new = self.df[self.df['City'] == location]
        for year in new['Year'].drop_duplicates():
            lst.append(year)
        return lst

    def where(self, date):
        lst = []
        new = self.df[self.df['Year'] == date]
        for place in new['City'].drop_duplicates():
            lst.append(place)
        return lst

if __name__ == "__main__":
    path = "./athlete_events.csv"
    fl = FileLoader()
    df = fl.load(path)
    stp = SpatioTemporalData(df)
    print(stp.when('Athina'))
    print(stp.where(1896))
