import csv
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import os

root = tk.Tk()
root.withdraw()

try:
    # Boîte de dialogue pour choisir un fichier
    chemin_fichier = filedialog.askopenfilename(title="Sélectionnez un fichier")

    if chemin_fichier:
        # Récupérer le nom du fichier à partir du chemin
        nom_fichier = os.path.basename(chemin_fichier)
        print(f"Vous avez choisi le fichier : {nom_fichier}")

        # Lire le contenu du fichier ou effectuer d'autres opérations
        with open(chemin_fichier, 'r') as fichier:
            contenu = fichier.read()
            # Faire quelque chose avec le contenu du fichier

except IOError as e:
    print(f"Erreur lors de la lecture du fichier : {e}")
except Exception as e:
    print(f"Une erreur s'est produite : {e}")
    


def analyze_cvs(file_path):
    try:
        with open(file_path, 'r') as csv_file:
            # Use the CSV reader to read the contents of the file
            csv_reader = csv.reader(csv_file, delimiter=',')
            
            # Create a Tkinter window
            table_window = tk.Tk()
            table_window.title("Tableau CSV")

            # Create a Treeview widget for the table
            table = ttk.Treeview(table_window)
            table["columns"] = next(csv_reader)  # Use the header as column identifiers
            table.heading("#0", text='Nombre de Ligne')  # Column for line numbers

            # Configure columns
            for col in table["columns"]:
                table.column(col, anchor="w", width=100)
                table.heading(col, text=col, anchor="w")

            # Insert data into the table
            for i, row in enumerate(csv_reader, start=1):
                table.insert("", "end", iid=i, text=i, values=row)

            # Pack the table into the window
            table.pack(expand=True, fill="both")

            # Run the Tkinter main loop
            table_window.mainloop()

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

try:
        analyze_cvs(chemin_fichier)

except IOError as e:
    print(f"Erreur lors de la lecture du fichier : {e}")
except Exception as e:
    print(f"Une erreur s'est produite : {e}")