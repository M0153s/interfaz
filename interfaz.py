import tkinter as tk
from tkinter import ttk
import random

def create_random_records():
    
    records = []
    for _ in range(5):
        record = {
            'id': random.randint(1, 100),
            'description': 'Descripción ' + str(random.randint(1, 100)),
            'quantity': random.randint(1, 10),
            'unit_price': round(random.uniform(0.5, 10.0), 2)
        }
        records.append(record)
    return records


window = tk.Tk()
window.title("Interfaz gráfica")
window.geometry("650x455")
window.configure(bg="saddle brown")


left_frame = tk.Frame(window, bg="saddle brown")
left_frame.pack(side=tk.LEFT, padx=10, pady=10)

right_frame = tk.Frame(window, bg="saddle brown")
right_frame.pack(side=tk.RIGHT, padx=10, pady=10)


labels = ['ID Product', 'Name', 'Description', 'Quantity', 'Price']
lines = []

for label_text in labels:
    label = tk.Label(left_frame, text=label_text, fg="white", bg="saddle brown")
    label.pack(anchor=tk.W)
    
    line = tk.Frame(left_frame, width=1, height=20, bg="white")
    line.pack(side=tk.LEFT, pady=5)
    lines.append(line)

# Botones del lado derecho
button_save = tk.Button(right_frame, text="Save", fg="white", bg="green", width=10)
button_save.pack(pady=10)

button_delete = tk.Button(right_frame, text="Delete", fg="white", bg="red", width=10)
button_delete.pack(pady=10)

button_update = tk.Button(right_frame, text="Update", fg="black", bg="orange", width=10)
button_update.pack(pady=10)


tree = ttk.Treeview(right_frame, columns=("ID", "Description", "Quantity", "Unit Price"))
tree.heading("#0", text="ID Product")
tree.column("#0", width=80, anchor=tk.CENTER)
tree.heading("ID", text="ID")
tree.column("ID", width=80, anchor=tk.CENTER)
tree.heading("Description", text="Description")
tree.column("Description", width=200, anchor=tk.CENTER)
tree.heading("Quantity", text="Quantity")
tree.column("Quantity", width=80, anchor=tk.CENTER)
tree.heading("Unit Price", text="Unit Price")
tree.column("Unit Price", width=80, anchor=tk.CENTER)
tree.pack()


records = create_random_records()
for record in records:
    tree.insert("", tk.END, text=str(record['id']), values=(record['id'], record['description'],
                                                            record['quantity'], record['unit_price']))


window.mainloop()