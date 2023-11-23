import json
import csv
import os

def save_to_JSON(data):
    with open('Data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def save_to_CSV(data):
    file_exists = os.path.isfile('Table.csv')
    with open('Table.csv', 'a', newline='', encoding='cp1251') as file:
        fieldnames = ['Name', 'Age', 'Inventory', 'Character', 'EXP']
        writer = csv.DictWriter(file, delimiter=";", fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader() # если файл вообще не существует, записываем заголовки столбцов
        writer.writerow(data)

def double_save_to_CSV(data):
    file_exists = os.path.isfile('Table.csv')
    with open('Table.csv', 'a', encoding='cp1251', newline='') as file:
        writer = csv.DictWriter(file, delimiter=";", fieldnames=data.keys())
        if not file_exists:
            writer.writeheader() # если файл вообще не существует, записываем заголовки столбцов
        writer.writerow(data)

def Example_of_game():
    User_name = str(input("Write your name here: "))
    User_age = str(input("Write your age here: "))
    Inventory = "Empty hands"
    data = {
    "Name" : User_name,
    "Age" : User_age,
    "Inventory" : Inventory,
    "Character" : "Human",
    "EXP" : 100
    }
    save_to_JSON(data)
    save_to_CSV(data)
    Exit = str(input("Write 1 for restart. Write 0 to exit: "))
    if Exit == "1":
        Example_of_game()
    else:
        pass

Example_of_game()