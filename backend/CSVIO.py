import csv


def ReadCSV(filename: str) -> list:
    """
      Function to parse a CSV file and return its contents.
    """
    data = []
    with open(filename, 'r') as csvfile:
        csv_reader = csv.reader(csvfile, skipinitialspace=True)
        for row in csv_reader:
            data.append(row)
    return data[1:]


def GetNumberOfRecords(d: list) -> int:
    return len(d)


def WriteCSV(data: list, fname: str):
    '''
      Write CSV Row to file
    '''
    with open(fname, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)
