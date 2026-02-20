import json
import os

class FileManager:
 def load_data(file_path):
    if not os.path.exists(file_path):
      return []
    try:
        with open(file_path,"r",encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {file_path}")
        return []
    except IOError as error:
        print(f"I/O error: {error}")
        return []

 def save_data(file_path,data):
    try:
        with open(file_path,"w",encoding="utf-8") as file:
         json.dump(data,file,indent=4)
    except IOError as error:
        print(f"I/O error: {error}")
