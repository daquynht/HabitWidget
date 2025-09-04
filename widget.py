import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
from plyer import notification #Støtte for varsler
import schedule #Planlegger varsler
import time        #For tidsstyring
import threading  #For å kjøre varsler i bakgrunnen

#------ Hovedvindu -----
root = tk.Tk()
root.title("Habit Tracker")
root.geometry("400x250")
root.resizable(False, False)

#Animert gif
gif_path = "background.gif"
gif = Image.open(gif_path)
frames = [ImageTk.PhotoImage(frame.copy().convert("RGBA")) for frame in ImageSequence.Iterator(gif)]

label_bg=tk.Label(root) #Bakgrunnslabel for GIF
label_bg.place(x=0, y=0, relwidth=1, relheight=1) #Fyll hele vinduet

#Funksjon som spiller av GIFen i en løkke
frame_index = 0
def animate_gif():
    global frame_index
    label_bg.config(image=frames[frame_index])
    frame_index = (frame_index + 1) % len(frames)
    root.after(100, animate_gif)  # Endre hastigheten på animasjonen her

animate_gif()

#Teksten oppå GIFen
label = tk.Label(root, text="💧 Husk å drikke vann!", 
      font=("Arial", 16, "bold"), fg="white", bg="#000000")

label.pack(pady=10)

#Knapp for å fullføre vanndrikkingen
def mark_as_done():
    label.config(text="Godt jobbet! Husk å drikke igjen om 30 min.")
    button_done.pack_forget()  # Skjul knappen etter at den er trykket

    button_done = tk.Button(
        root, text="Fullført",
        command=mark_as_done)
    button_done.pack(pady=5)

   # INPUT for ny påminnelse
def add_reminder():
    "Legger til ny påminnelse"
    reminder = entry.get()
    if reminder:
        label.config(text=reminder)
        entry.delete(0, tk.END)  # Tøm inntastingsfeltet
        button_done.pack(pady=5)  # Vis knappen igjen

    entry = tk.Entry(root, width=25)
    entry.pack(pady=5)

    button_add = tk.Button(
        root, text="Legg til påminnelse",
        command=add_reminder)
    button_add.pack(pady=5)

# ---- Varslingsfunksjon -----
def send_notification():
    notification.notify(
        title="Tid for å drikke vann!",
        message="Husk å drikke vann.",
        timeout=10  # Varighet i sekunder
    )
# Eksempel: send varsling når du legger til ny påminnelse
def daily_reminder():
    send_notification("💧 Husk å drikke vann!")
    label.config(text="💧 Husk å drikke vann!")
    button_done.pack(pady=5)

# Bruk schedule til å sende varsling på bestemte tider
schedule.every().day.at("10:00").do(daily_reminder)
schedule.every().day.at("14:00").do(daily_reminder)
schedule.every().day.at("20:00").do(daily_reminder)

def run_schedule():
    """Kjører schedule i en egen tråd slik at GUI ikke fryser"""
    while True:
        schedule.run_pending()
        time.sleep(60)  # Sjekk hvert minutt

# Start schedule i bakgrunnstråd
threading.Thread(target=run_schedule, daemon=True).start()

# ------------------------- START GUI -------------------------
root.mainloop()