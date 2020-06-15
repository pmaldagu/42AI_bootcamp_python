import csv

class CsvReader():
    def __init__(self, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom

    def __enter__(self):
        self.fd = open(self.sep, 'r')
        self.reader = csv.reader(self.fd, delimiter = '\t')
        for row in self.reader:
            print(row)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fd.close()

    def getdata(self):
        return self.reader

if __name__ == "__main__":
    with CsvReader('good.csv') as file:
        data = file.getdata()
        #header = file.getheader()
