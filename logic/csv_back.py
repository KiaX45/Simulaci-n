import os 
import pandas as pd

class Csv_convert:
    def __init__(self, file_path) -> None:
        self.file_path = file_path 
        self.directory = os.path.dirname(file_path)
        self.file_name = os.path.basename(file_path)
        os.chdir(self.directory)
        
    def convert(self):
        data = pd.read_csv(self.file_path)
        name = self.file_name.split(".")[0]
        data.to_excel(f"{name}.xlsx", index=False)
        print("Archivo convertido a Excel") 
        
        
if __name__ == "__main__":
    file_path = r'E:\testOrdenamiento\Excel\CSV.csv'  # Sustituye con la ruta real de tu archivo
    converter = Csv_convert(file_path)
    converter.convert()