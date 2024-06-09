import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class ExcelDataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
    
    def load_data(self):
        self.data = pd.read_excel(self.file_path)
        return self.data
    
    def display_data(self, rows=5):
        if self.data is not None:
            print(self.data.head(rows))
        else:
            print("No data loaded yet. Please call load_data() first.")
    
    def plot_line_chart(self, date_col, value_col):
        plt.figure(figsize=(12, 6))
        plt.plot(self.data[date_col], self.data[value_col], marker='o', linestyle='-', linewidth=2, markersize=6)
        plt.title('Gráfico de Líneas Mejorado', fontsize=16)
        plt.xlabel(date_col, fontsize=14)
        plt.ylabel(value_col, fontsize=14)
        plt.xticks(rotation=45)
        plt.grid(True, which='both', linestyle='--', linewidth=0.5)
        plt.tight_layout()
        plt.show()
    
    def plot_bar_chart(self, date_col, value_col):
        plt.figure(figsize=(12, 6))
        sns.barplot(x=date_col, y=value_col, data=self.data, ci=None)
        plt.title('Gráfico de Barras Mejorado', fontsize=16)
        plt.xlabel(date_col, fontsize=14)
        plt.ylabel(value_col, fontsize=14)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        
    def get_head(self, rows=5):
        return self.data.head(rows) 

# Ejemplo de uso
if __name__ == "__main__":
    file_path = r'E:\testOrdenamiento\Excel\Excel.xlsx'  # Sustituye con la ruta real de tu archivo
    loader = ExcelDataLoader(file_path)
    data = loader.load_data()
    loader.display_data()

    date_col, value_col = loader.get_head()

    # Gráfico de líneas
    loader.plot_line_chart(date_col, value_col)

    # Gráfico de barras
    loader.plot_bar_chart(date_col, value_col)
