def GetAllEmpDetails(data: list, name: str) -> list:
    '''
      Function recieves the data list and gets all the employee details by name
    '''
    for row in data:
        if row[0] == name:
            return row
    else:
        return []