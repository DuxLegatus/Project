import sys
import os
from tkinter import *



translations_english = {}
translations_georgian = {}
def main():
    # get_dictionary()
    # something()
    ...
    

            

# ეს ფუნქცია ქმნის უსასრულო ლუპს იქამდე სანამ მომხმარებელი არ აირჩევს პროგრამის გაჩერებას. 
# თუ მომხმარებელი აირჩევს რომ ტექსტი გადათარგმნოს მაშინ ხდება translate_text ფუნქციის გამოძახება
# def something():
#     while True:
#         print("1. translate")
#         print("2. exit")
#         try:
#             action = int(input("what do you want to do: "))
#         except ValueError:
#             print("you should write int")
#             continue

#         if action == 2:
#             sys.exit()
#         elif action == 1:
#             language = input("language (english/georgian): ").strip().lower()
#             text = input("word to translate: ").strip().lower()
            
#             translate_text(text, language)
#         else:
#             print("wrong option")
#         print("\n")

# ეს ფუნქცია ხსნის ლექსიკონის ფაილს და ამ ფაილში არსებული ინფორმაცია გადმოაქვს დიქშენარიში
def get_dictionary():
    try:
        with open("dictionary.txt","r",encoding="utf-8") as file:
            for i in file:
                if ":" in i:
                    key, value = i.strip().split(":", 1)
                    translations_georgian[key.strip().lower()] = value.strip().lower()
    except FileNotFoundError:
        raise ValueError("georgian dictionary doesnt exist")
    try:
        with open("dictionary1.txt","r",encoding="utf-8") as file:
            for i in file:
                if ":" in i:
                    key, value = i.strip().split(":", 1)
                    translations_english[key.strip().lower()] = value.strip().lower()
    except FileNotFoundError:
        raise ValueError("english dictionary doesnt exist")


# ეს ფუნქცია იღებს ტექსტს და ენას ინფუთად და შემდეგ თუ ამ სიტყვის/ფრაზის თარგმანი არსებობს ლექსიკონში  გადათარგმნილ სიტყვას აბრუნებს
# ხოლო თუ თარგმანი არ არსებობს ხსნის ლექსიკონის ფაილს და იქ ამატებს სიტყვას და აგრეთვე უშუალოდ დიქშენარიშიც ხდება ფაილის დამატება
def translate_text(text, language):
    get_dictionary()
    if language == "english":
        if translations_english.get(text):
            return translations_english[text]
        else:
            translation = input("add translation of that word: ").strip().lower()
            with open("dictionary1.txt","a",encoding="utf-8") as f:
                if os.path.getsize("dictionary1.txt") > 0:
                    f.write("\n")
                f.write(f"{text}:{translation}")
            translations_english.update({text:translation})
            print("dictionary updated")
            return translation
    elif language == "georgian":
        if translations_georgian.get(text):
            return translations_georgian[text]
        else:
            translation = input("add translation of that word: ").strip().lower()
            with open("dictionary.txt","a",encoding="utf-8") as f:
                if os.path.getsize("dictionary.txt") > 0:
                    f.write("\n")
                f.write(f"{text}:{translation}")
            translations_georgian.update({text:translation})
            print("dictionary updated")
            return translation
    else:
        return "not valid language"



if __name__ == "__main__":
    main()
