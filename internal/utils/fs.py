import json
import os


def GetFS() -> list[str]:
    """
      Gets a list of files from the `internal/files` dir
    """
    return os.listdir("internal/files")


def EncodeFile(index: int) -> str:
    '''
      Encodes a file into json. 

      Sample JSON response:

      ```
      {
        filename : hello.txt,
        content: hi there!
      }

    '''
    with open("internal/files/"+GetFS()[index], "r") as file:
        return json.dumps({
            "filename": GetFS()[index],
            "content": file.read()
        })
