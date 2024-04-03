from rich.console import Console
from rich.prompt import Prompt
from rich.markdown import Markdown
from rich.text import Text
from rich.table import Table
from time import sleep
import json
import socket

console = Console()


def EndUI():
    console.print("\nGOODBYE!", style="bold blue")
    sleep(0.5)
    console.clear()
    exit(0)


def EmpDetailsUI(s: socket.socket):
    console.clear()
    message = Text("Enter Employee Name", style="Bold green")
    name = Prompt.ask(message)

    s.sendto(
        f"GET full-employee-Details {name}".encode('ascii'), ('127.0.0.1', 8080))

    row = json.loads(s.recvfrom(4096)[0])

    if row == []:
        console.print("404 Employee Not Found", style="bold red")
    else:
        table = Table()
        table.add_column("Employee Name")
        table.add_column("Gender")
        table.add_column("Position Title")
        table.add_column("Position #")
        table.add_column("Experience")
        table.add_column("2023 Performance")

        table.add_row(row[0], row[1], row[2], row[3], row[4], row[5])
        console.print(table)
        input()
        UI(s)


def GenderExperienceUI(s: socket.socket):
    console.clear()
    message = Text("Enter Employee Name", style="Bold green")
    name = Prompt.ask(message)

    s.sendto(
        f"GET gender-experience {name}".encode('ascii'), ('127.0.0.1', 8080))

    row = json.loads(s.recvfrom(4096)[0])

    if row == []:
        console.print("404 Employee Not Found", style="bold red")
    else:
        table = Table()
        table.add_column("Gender")
        table.add_column("Experience")

        table.add_row(row[0], row[1])
        console.print(table)
        input()
        UI(s)


def PositionDetailsUI(s: socket.socket):
    console.clear()
    message = Text("Enter Employee Name", style="Bold green")
    name = Prompt.ask(message)

    s.sendto(f"GET title-# {name}".encode('ascii'), ('127.0.0.1', 8080))

    row = json.loads(s.recvfrom(4096)[0])

    if row == []:
        console.print("404 Employee Not Found", style="bold red")
    else:
        table = Table()
        table.add_column("Position Title")
        table.add_column("Position #")

        table.add_row(row[0], row[1])
        console.print(table)
        input()
        UI(s)


def GetListByTitleUI(s: socket.socket):
    console.clear()
    message = Text("Enter Position Title", style="Bold green")
    title = Prompt.ask(message)

    s.sendto(f"GET list-title {title}".encode('ascii'), ('127.0.0.1', 8080))

    rows = json.loads(s.recvfrom(4096)[0])

    if rows == []:
        console.print("404 Employee Not Found", style="bold red")
    else:
        table = Table()
        table.add_column("Position Title")
        table.add_column("Position #")

        for row in rows:
            table.add_row(row[0], row[1])

        console.print(table)
        input()
        UI(s)


def UI(s: socket.socket):
    console.clear()

    initialMenu = Markdown("""
# Employee UDP Client
#### Done By Abdulrahman Idrees - 202200729

1. Ask for full information about a single employee (ask by the Employee Name).
2. Ask for the Gender and the Experience of an employee (ask by the Employee Name)
3. Ask for the Position Title and Position # of an employee (ask by the Employee Name)
4. Ask for a list of employee names and their Position # by specified Position Title.
5. Exit
""")

    console.print(initialMenu)
    try:
        op = int(input("\nWhat is Your Option: "))
        match op:
            case 1:
                EmpDetailsUI(s)
            case 2:
                GenderExperienceUI(s)
            case 3:
                PositionDetailsUI(s)
            case 4:
                GetListByTitleUI(s)
            case _:
                EndUI()
    except KeyboardInterrupt:
        EndUI()
