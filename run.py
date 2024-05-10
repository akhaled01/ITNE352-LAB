from rich import console
import subprocess
import sys

c = console.Console()

'''
  The subprocess module allows us to exec a command with
  its own process. It is used to launch the server and client 
  from one command (with a simple CLI argument). This allows us 
  to remove the tedious process of going to the `internal` 
  directory and running each one seperately.
'''

try:
    if len(sys.argv) != 2:
        raise IndexError
    if sys.argv[1] == "server":
        subprocess.run(["python", "./internal/server.py"])
    elif sys.argv[1] == "client":
        subprocess.run(["python", "./internal/client.py"])
    else:
        c.print_exception("Invalid script")
except IndexError:
    c.print("Usage: python run.py <server/client>", style="bold green")
    sys.exit(1)
except KeyboardInterrupt:
    sys.exit(0)
