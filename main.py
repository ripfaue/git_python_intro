import tkinter as tk
from tkinter import messagebox
import urllib.request
import json
import random


def hole_wetter(stadt):

    try:
        url = f"https://wttr.in/{stadt}?format=j1"
        with urllib.request.urlopen(url, timeout=5) as response:
            data = json.loads(response.read().decode())

        aktuell = data['current_condition'][0]
        temp = aktuell['temp_C']
        beschreibung = aktuell['lang_de'][0]['value'] if 'lang_de' in aktuell else aktuell['weatherDesc'][0]['value']

        return f"{temp}°C, {beschreibung}"
    except:
        return "Wetter konnte nicht abgerufen werden"


def hole_zitat():

    zitate = [
        "Jeder Tag ist ein neuer Anfang!",
        "Glaube an dich selbst und alles ist möglich.",
        "Das Leben ist schön - genieße jeden Moment!",
        "Deine positive Einstellung macht den Unterschied.",
        "Heute ist ein großartiger Tag für neue Abenteuer!",
        "Lächle und die Welt lächelt mit dir.",
        "Du bist stärker als du denkst!",
        "Kleine Schritte führen zu großen Zielen.",
        "Sei die Veränderung, die du sehen möchtest.",
        "Jeder Sonnenaufgang bringt neue Möglichkeiten."
    ]
    return random.choice(zitate)


def begruesse_user():
    name = name_eingabe.get().strip()
    ort = ort_eingabe.get().strip()

    if not name or not ort:
        messagebox.showwarning("Eingabe fehlt", "Bitte Name und Ort eingeben!")
        return

    # Begrüßungstext erstellen
    wetter = hole_wetter(ort)
    zitat = hole_zitat()

    begruessung = f"""
Hallo {name}! 

Schön, dass du aus {ort} kommst!

Das aktuelle Wetter: {wetter}

Dein Zitat des Tages:
"{zitat}"

Ich wünsche dir einen wundervollen Tag!
    """

    # Ergebnis-Fenster erstellen
    ergebnis_fenster = tk.Toplevel(root)
    ergebnis_fenster.title("Deine Begrüßung")
    ergebnis_fenster.geometry("400x300")
    ergebnis_fenster.configure(bg="#f0f8ff")

    text_label = tk.Label(ergebnis_fenster, text=begruessung,
                          font=("Arial", 12), bg="#f0f8ff",
                          justify="left", padx=20, pady=20)
    text_label.pack(expand=True)

    schliessen_btn = tk.Button(ergebnis_fenster, text="Schließen",
                               command=ergebnis_fenster.destroy,
                               font=("Arial", 10), bg="#4CAF50",
                               fg="white", padx=20, pady=5)
    schliessen_btn.pack(pady=10)


# Hauptfenster erstellen
root = tk.Tk()
root.title("Wetter-Begrüßung")
root.geometry("400x250")
root.configure(bg="#e3f2fd")

# Titel
titel = tk.Label(root, text="Willkommen! ",
                 font=("Arial", 18, "bold"), bg="#e3f2fd")
titel.pack(pady=20)

# Name-Eingabe
name_frame = tk.Frame(root, bg="#e3f2fd")
name_frame.pack(pady=10)
tk.Label(name_frame, text="Dein Name:", font=("Arial", 12),
         bg="#e3f2fd", width=12, anchor="w").pack(side="left")
name_eingabe = tk.Entry(name_frame, font=("Arial", 12), width=20)
name_eingabe.pack(side="left", padx=5)

# Ort-Eingabe
ort_frame = tk.Frame(root, bg="#e3f2fd")
ort_frame.pack(pady=10)
tk.Label(ort_frame, text="Dein Ort:", font=("Arial", 12),
         bg="#e3f2fd", width=12, anchor="w").pack(side="left")
ort_eingabe = tk.Entry(ort_frame, font=("Arial", 12), width=20)
ort_eingabe.pack(side="left", padx=5)

# Button
begruessen_btn = tk.Button(root, text="Begrüße mich!",
                           command=begruesse_user,
                           font=("Arial", 12, "bold"),
                           bg="#2196F3", fg="white",
                           padx=30, pady=10)
begruessen_btn.pack(pady=20)

# Enter-Taste binden
root.bind('<Return>', lambda event: begruesse_user())

root.mainloop()
