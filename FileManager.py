from dataclasses import dataclass, field
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
import os
import pandas as pd

@dataclass
class FileManager():
    filename : str = field(init=False, repr=False)

    def pickFile(self, sheet_name:str = "Sheet1"):
        Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
        self.filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
        
        file = self.openFile(sheet_name)
        
        return file
    
    def openFile(self, sheet_name:str = "Sheet1"):
        file_list = self.filename.split(".")
        file_extension = file_list[-1]

        file = None
        if file_extension == "xlsx" and sheet_name == "Sheet1":
            file = pd.read_excel(self.filename, header=0)
        elif file_extension == "xslx" and sheet_name != "Sheet1":
            file = pd.read_excel(self.filename, header=0, sheet_name=sheet_name)
        elif file_extension == "csv":
            file = pd.read_csv(self.filename, encoding='utf-8')
            file = file.fillna("")
        
        return file
    
    def formatLocalFilePath(self, filename):
        self.filename = os.path.abspath(filename)
    
    def writeFile(self, filename, file_extension, file):
        self.filename = os.path.abspath(filename)
        file_path = self.filename + "." + file_extension
        try:
            file.to_csv(file_path, encoding="utf-8", index=False)
        except Exception as e:
                print(f"Unexpected {e=}, {type(e)=}")
                raise
        return
