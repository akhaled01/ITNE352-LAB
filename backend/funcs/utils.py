import csv

def ReadCSV(filename: str) -> list:
    '''
      Function to parse a CSV file and return its contents.
    '''
    data = []
    with open(filename, 'r') as csvfile:
        csv_reader = csv.reader(csvfile, skipinitialspace=True)
        for row in csv_reader:
            data.append(row)
    return data[1:]


def ParseCommand(command: str) -> str:
    '''
      Function to extract name / title of employee 
      from a command with format "GET <action> <data>"
    '''
    words = command.split() 

    if len(words) >= 3 and words[0] == "GET":
        name_title = ' '.join(words[2:])
        return name_title
    else:
        return ""
