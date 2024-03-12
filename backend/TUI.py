from backend.Employees import GetAllEmpDetails
from rich.table import Table
from rich.text import Text
from backend.CSVIO import *
from rich.console import Console
from rich.prompt import Prompt
from rich.markdown import Markdown
from rich.traceback import install
from time import sleep
install()

console = Console()
edata = ReadCSV("Employee_data.csv")

def EndUI():
  console.print("\nGOODBYE!", style="bold blue")
  sleep(0.5)
  console.clear()
  exit(0)

def EmpDetailsUI(data: list):
    '''
      Main Terminal UI for record by employee name (task 1)
    '''
    console.clear()
    message = Text("Enter Employee Name", style="Bold green")
    name = Prompt.ask(message)
    row = GetAllEmpDetails(data=data, name=name)

    if row == []:
        console.print("404 Employee Not Found", style="bold red")
    else:
        table = Table(title=f"Details of %s" % name)
        table.add_column("Employee Name")
        table.add_column("Gender")
        table.add_column("Position Title")
        table.add_column("Position #")
        table.add_column("Experience")
        table.add_column("2023 Performance")

        table.add_row(row[0], row[1], row[2], row[3], row[4], row[5])
        console.print(table)
        input()
        UI()


def SpecifcEmpDetailsUI(data: list):
    console.clear()
    message = Text("Enter Employee Name", style="Bold green")
    name = Prompt.ask(message)
    row = GetAllEmpDetails(data=data, name=name)
    if row == []:
        console.print("404 Employee Not Found", style="bold red")
    else:
        dataList = {1: "Employee Name", 2: "Gender", 3: "Position Title",
                    4: "Position #", 5: "Experience", 6: "2023 Performance"}

        for field in dataList:
            console.print(str(field) + ". " + dataList[field])

        flist: str = Prompt.ask("Input Desired Fields (one space per number)")
        chosenOnes = flist.split(" ")
        [print(dataList[int(num)] + ": " + row[int(num)-1])
         for num in chosenOnes]

        input()
        UI()


def PrintNumRecords():
    console.print(f"\nThere Are Currently %d Employee Records" %
                  GetNumberOfRecords(edata))
    input()
    UI()


def AddRecordUI():
    row = []
    row.append(Prompt.ask("Enter Employee Name"))
    row.append(Prompt.ask("Enter Employee Gender"))
    row.append(Prompt.ask("Enter Employee Position Title"))
    row.append(Prompt.ask("Enter Employee Position #"))
    row.append(Prompt.ask("Enter Employee Experience"))
    row.append(Prompt.ask("Enter Employee's Performance in 2023"))

    edata.append(row)
    WriteCSV(fname="Employee_data.csv", data=row)

    table = Table(title=f"Details of %s" % row[0])
    table.add_column("Employee Name")
    table.add_column("Gender")
    table.add_column("Position Title")
    table.add_column("Position #")
    table.add_column("Experience")
    table.add_column("2023 Performance")

    table.add_row(row[0], row[1], row[2], row[3], row[4], row[5])

    console.print(table)
    input()
    UI()


def UI():
    '''
      Main Application UI Entrypoint
    '''
    console.clear()
    initialMenu = Markdown("""
# Employee CSV Parser
#### Done By Abdulrahman Idrees

1. Get Specific Employee 
2. Specific Info About Employee
3. Get Number Of records Stored 
4. Add a Employee
5. Exit
""")
    console.print(initialMenu)
    try:
        op = int(input("\nWhat is Your Option: "))
        match op:
            case 1:
                EmpDetailsUI(edata)
            case 2:
                SpecifcEmpDetailsUI(edata)
            case 3:
                PrintNumRecords()
            case 4:
                AddRecordUI()
            case _:
              EndUI()
    except KeyboardInterrupt:
        EndUI()
