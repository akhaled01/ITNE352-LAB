import sys
import subprocess
from rich import console

c = console.Console()

try:
    if len(sys.argv) != 2:
        c.print("Usage: py run.py <server/client>", style="bold green")
        sys.exit(1)
    if sys.argv[1] == "server":
        subprocess.run(["python", "./internal/server.py"])
    elif sys.argv[1] == "client":
        subprocess.run(["python", "./internal/client.py"])
    else:
        c.print_exception("Invalid script")

except IndexError:
    c.print("Usage: py run.py <server/client>", style="bold green")
    sys.exit(1)
