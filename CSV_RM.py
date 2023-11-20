import csv
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import os

class CSVAnalyzer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()

    def choose_file(self):
        try:
            file_path = filedialog.askopenfilename(title="Sélectionnez un fichier")
            if file_path:
                return file_path
        except Exception as e:
            print(f"Erreur lors de la sélection du fichier : {e}")
            return None

    def analyze_csv(self, file_path):
        try:
            with open(file_path, 'r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                header = next(csv_reader, None)

                if header:
                    table_window = tk.Tk()
                    table_window.title("Tableau CSV")

                    table = ttk.Treeview(table_window)
                    table["columns"] = header
                    table.heading("#0", text='Nombre de Ligne')

                    for col in table["columns"]:
                        table.column(col, anchor="w", width=100)
                        table.heading(col, text=col, anchor="w")

                    for i, row in enumerate(csv_reader, start=1):
                        table.insert("", "end", iid=i, text=i, values=row)

                    table.pack(expand=True, fill="both")

                    table_window.mainloop()
                else:
                    print("Le fichier CSV est vide.")

        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def run(self):
        try:
            file_path = self.choose_file()
            if file_path:
                nom_fichier = os.path.basename(file_path)
                print(f"Vous avez choisi le fichier : {nom_fichier}")
                self.analyze_csv(file_path)

        except Exception as e:
            print(f"Une erreur s'est produite : {e}")


csv_analyzer = CSVAnalyzer()
csv_analyzer.run()
