import requests

odpowiedz = requests.get("https://jsonplaceholder.typicode.com/users/1")

print("Status:", odpowiedz.status_code)

dane = odpowiedz.json()
print("Imię:", dane["name"])
print("Email:", dane["email"])