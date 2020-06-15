import pandas as pd

class FileLoader:
    def load(self, path):
        data = pd.read_csv(path)
        dimension = data.shape
        print("Loading dataset of dimension {0} X {1}".format(dimension[0], dimension[1]))
        return data

    def display(self, df, n):
        if n >= 0:
            print(df.head(n))
        elif n < 0:
            print(df.tail(n * -1))

if __name__ == "__main__":
    path = "./athlete_events.csv"
    fl = FileLoader()
    dt = fl.load(path)
    fl.display(dt, -5)
