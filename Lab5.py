# program1.py
import re

ukrainian_alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
latin_alphabet = "abcdefghijklmnopqrstuvwxyz"

ukr_order = {ch: i for i, ch in enumerate(ukrainian_alphabet)}
lat_order = {ch: i for i, ch in enumerate(latin_alphabet)}

def word_key(word):
    word_lower = word.lower()
    key = []
    for ch in word_lower:
        if ch in ukr_order:
            key.append((0, ukr_order[ch]))
        elif ch in lat_order:
            key.append((1, lat_order[ch]))
        else:
            key.append((2, ord(ch)))
    return key


file_path = r"Q:\LAB\text.txt"

with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

words = re.findall(r'\w+', text)
words = [w for w in words if len(w) > 1]

print("Вхідний список слів:", words)

sorted_words = sorted(words, key=word_key)
print("Відсортований список:", sorted_words)


# program2.py
import urllib.parse
import pyperclip

url = "https://uk.wikipedia.org/wiki/%D0%9A%D0%BD%D0%B8%D0%B3%D0%B0"

decoded_url = urllib.parse.unquote(url)
print("Перетворене посилання:", decoded_url)

pyperclip.copy(decoded_url)
print("Посилання скопійовано в буфер обміну!")

# program3.py
import json

students = {
    "Петренко": ["Іван", "Іванович", 2000],
    "Сидоренко": ["Марія", "Петрівна", 1999],
    "Коваленко": ["Олег", "Васильович", 2001],
    "Шевченко": ["Анна", "Ігорівна", 2002],
    "Мельник": ["Богдан", "Олександрович", 1998],
    "Ткаченко": ["Оксана", "Сергіївна", 2000],
    "Бондаренко": ["Юрій", "Миколайович", 1997],
    "Кузьменко": ["Ірина", "Андріївна", 2001],
    "Лисенко": ["Віталій", "Григорович", 1999],
    "Гончаренко": ["Наталія", "Володимирівна", 2002]
}


json_path = r"Q:\LAB\students.json"

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(students, f, ensure_ascii=False, indent=4)

with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

print("Записи з JSON файлу:")
for surname, info in data.items():
    print(f"{surname}: {info[0]} {info[1]}, {info[2]}")