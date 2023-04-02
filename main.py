from tkinter import *
import requests
from PIL import Image, ImageTk


def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    print(quote)
    quote_label.config(text=quote)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

window.background_img = ImageTk.PhotoImage(Image.open("background.png"))
quote_label = Label(window, image=window.background_img, compound=CENTER, text="Kanye Quote Goes HERE",
                    width=300, height=414, font=("Arial", 30, "bold"), fg="white", wraplength=250)
quote_label.grid(row=0, column=0)

window.kanye_img = ImageTk.PhotoImage(Image.open("kanye.png"))
kanye_button = Button(window, image=window.kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()
