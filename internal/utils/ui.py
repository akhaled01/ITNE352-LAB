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
        op = int(Prompt("Please choose an option").ask())
        if op < 1 or op > 3:
            raise ValueError
        return op
    except ValueError:
        c.print("please enter a valid option", style="bold red")
        sys.exit(0)
