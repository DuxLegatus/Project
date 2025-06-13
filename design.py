from tkinter import *
from tkinter import ttk
import translator1



window = Tk()
window.geometry("960x720")
window.title("Translator")
window.config(background="#383737")
translations_english = {}
translations_georgian = {}





def buttonfunc():
    text1 = entry.get("1.0", END).strip()
    lang = opt.get().lower().strip()

    if lang == "english":
        text1 = text1.lower()

    translated_text = translator1.translate_text(text1, lang)

    entry2.config(state="normal")
    entry2.delete("1.0", END)
    entry2.insert(END, translated_text)
    entry2.config(state="disabled")



def georgianLanguage(event):
    dict1 = {
        'a': 'ა',
        'b': 'ბ',
        'c': 'ც',
        "C":"ჩ",
        'd': 'დ',
        'e': 'ე',
        'f': 'ფ',
        'g': 'გ',
        'h': 'ჰ',
        'i': 'ი',
        'j': 'ჯ',
        "J":"ჟ",
        'k': 'კ',
        'l': 'ლ',
        'm': 'მ',
        'n': 'ნ',
        'o': 'ო',
        'p': 'პ',
        'q': 'ქ',
        'r': 'რ',
        "R":"ღ",
        's': 'ს',
        't': 'ტ',
        "T":"თ",
        'u': 'უ',
        'v': 'ვ',
        'w': 'წ',
        "W":"ჭ",
        'x': 'ხ',
        'y': 'ყ',
        'z': 'ზ',
        "Z":"ძ"
    }
    lang = opt.get().lower().strip()
    if lang == "georgian":
        char = event.char
        if dict1.get(char):
            entry.insert(END, dict1[char])
            return "break"



style = ttk.Style()
style.configure(
    "Custom.TCombobox",
    fieldbackground="#2c2c2c",  
    background="#2c2c2c",      
    foreground="#000000",       
    arrowcolor="#1a1a1a",       
    bordercolor="#444444",     
    lightcolor="#444444",       
    darkcolor="#1a1a1a",        
    padding=5,
    font=("Arial", 12)
)

def update_second_dropdown(event):
    selected_lang = opt.get()
    if selected_lang == "English":
        opt2.set("Georgian")
    else:
        opt2.set("English")
    

languages = ["Georgian","English"]
opt = StringVar(value="Georgian")
language = ttk.Combobox(window, textvariable=opt, values=languages, style="Custom.TCombobox", state="readonly",)
language.place(x=120,y=50)
language.bind("<<ComboboxSelected>>", update_second_dropdown)


opt2 = StringVar(value="English")
language2 = ttk.Combobox(window, textvariable=opt2, values=languages, style="Custom.TCombobox", state="disabled")
language2.place(x=700, y=50)




entry = Text(window, font=("Sylfaen", 10), bg="#282727", fg="#D9D9E1", width=50)
entry.place(x=30, y=150)

entry.bind("<Key>", georgianLanguage)

entry2 = Text(window,font=("Sylfaen",10),bg="#282727",fg="#D9D9E1",width=50,state="disabled")
entry2.place(x=585,y=150)




button = Button(window,text="Translate",
                bg="#282727",padx=50,pady=10,
                fg="#D9D9E1",font=("arial",15),
                command=buttonfunc,
                )
button.place(x=390,y=10)

window.mainloop()





