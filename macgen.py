import requests


site = "https://miniwebtool.com/mac-address-generator/"
prefix = input("Enter the prefix of your Mac Address (The starting Characters): ")
format = input("Enter the Format type you want 1 - 4: ")
case = input("Choose if you want the letters to be uppercase\n(Uppercase) 0 - 1 (Lowecase): ")

if prefix == None or prefix == "":
    prefix = "0A"

if format == None or format == "" or format == " " or not format.isdigit() or not format.isnumeric():
    format = "0"

if case == None or case == "" or case == " " or not case.isdigit() or not case.isnumeric():
    case = "1"


req = requests.post(site, data=f"prefix: {prefix} format: {format} case: {case}")

print(f"New Mac Address is: {req.text}")