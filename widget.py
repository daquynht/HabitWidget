import tkinter as tk

root = tk.Tk()
root.title("Habit Tracker")

#Størrelse, bakgrunn og ikon
root.geometry("250x120")
root.configure(bg="#2C2C2C")

label = tk.Label(
    root, text="Husk å drikke vann", 
    font=("Arial", 16, "bold"), 
    bg="#2C2C2C", 
    fg="white")
label.pack(expand=True)

root.mainloop()