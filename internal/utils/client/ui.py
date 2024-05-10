from rich.markdown import Markdown
from rich.prompt import Prompt
from rich.console import Console
import sys

c = Console()
menu = Markdown(
    """
## TCP File Server by Abdulrahman Idrees - 202200729

1. Get list of files
2. select file
3. Quit
4. Quit and shutdown server
"""
)


def UI() -> int:
    """Main UI render function for the client

    Returns:
        int: Option Chosen by client
    """
    c.clear()
    c.print(menu)
    try:
        option = int(Prompt.ask("[bold magenta] \nPlease pick a valid option"))
        if option < 1 or option > 4:
            raise ValueError
        return option
    except ValueError:
        c.print("please enter a valid option", style="bold red")
        sys.exit(0)


def FileChooseUI(filenames: list[str]) -> int:
    """UI render function for the client to choose files
    
    Returns:
        int: Option Chosen by client
    """
    c.clear()
    for i, filename in enumerate(filenames):
        c.print(i, filename)
    try:
        option = int(Prompt.ask("[bold orange] \nPlease pick a valid option"))
        if option < 1 or option > len(filenames)+1:
            raise ValueError
        return option
    except ValueError:
        c.print("please enter a valid option", style="bold red")
        sys.exit(0)
