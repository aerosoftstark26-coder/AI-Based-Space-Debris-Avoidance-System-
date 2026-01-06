import tkinter as tk

def launch_gui():
    root = tk.Tk()
    root.title("ORBITAI Control Center")
    label = tk.Label(root, text="Monitoring...", font=("Arial",14))
    label.pack(pady=20)
    return root, label