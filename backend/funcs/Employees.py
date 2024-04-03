def GetAllEmpDetails(data: list, name: str) -> list:
    '''
      Function recieves the data list and gets all the employee details by name
      This function will mainly be reused with other functions
    '''
    for row in data:
        if row[0] == name:
            return row
    else:
        return []


def GenderExperienceDetails(data: list, name: str) -> tuple:
    '''
      Function That outputs only Gender and experience by employee name
    '''
    all_details = GetAllEmpDetails(data, name)
    return (all_details[1], all_details[4])


def PositionDetails(data: list, name: str) -> tuple:
    '''
      Function that outputs both employee position title and
      number
    '''
    all_details = GetAllEmpDetails(data, name)
    return (all_details[2], all_details[3])


def GetDetailsByPositionTitle(data: list, title: str) -> list:
    '''
      Function to return details of all employee by 
      employee title
    '''
    main_data = []
    for row in data:
        if row[2] == title:
            main_data.append(row)
    return main_data



