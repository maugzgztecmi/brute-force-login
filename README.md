# Brute Force Login Tool (Para pruebas locales)

Este proyecto es una herramienta de **fuerza bruta** diseñada para realizar pruebas de seguridad en un formulario de login simulado. El proyecto consiste en un servidor Flask que expone un formulario de inicio de sesión, y un script que intenta encontrar la contraseña correcta utilizando un diccionario de contraseñas.

> ⚠️ **Advertencia:** Esta herramienta debe usarse exclusivamente en entornos controlados y con fines educativos o de prueba ética. No está diseñada para usarse en sistemas reales sin el consentimiento explícito del propietario.

## 💻 Estructura del Proyecto

El proyecto está dividido en dos partes:

1. **Servidor Flask (`server/`)**
   - Un servidor web simple con un formulario de login simulado.

2. **Herramienta de Fuerza Bruta (`attacker/`)**
   - Un script que intenta descubrir la contraseña correcta a través de un ataque de fuerza bruta utilizando una lista de contraseñas.

## 🛠 Requisitos

### 1. Instalar Python

Asegúrate de tener Python 3.x instalado en tu sistema. Puedes verificarlo con:

```bash
python --version
```

Si no lo tienes, instálalo desde [https://www.python.org](https://www.python.org).

### 2. Instalar dependencias

El proyecto depende de las siguientes librerías Python:

- **Flask**: Framework web para crear el servidor de login.
- **Requests**: Librería para hacer solicitudes HTTP desde el script de ataque.

Instálalas con:

```bash
pip install flask requests
```

### 3. Diccionario de contraseñas

Este proyecto utiliza una wordlist del repositorio **Probable-Wordlists**:

📂 `Top1575-probable.txt`

Contiene combinaciones comunes y realistas de contraseñas, muchas de ellas más complejas que las de rockyou.txt.

> ✅ Ya está incluida en el repositorio, no necesitas descargar nada adicional.

Asegúrate de que el archivo esté en la raíz del proyecto y se llame exactamente así:

```text
Top1575-probable.txt
```

## 🚀 Cómo Ejecutarlo

### 1. Levantar el servidor Flask

Abre una terminal, navega a la carpeta `server/` y ejecuta:

```bash
cd server
python app.py
```

Esto iniciará un servidor web en `http://127.0.0.1:5000`, con un formulario de login accesible desde tu navegador.

### 2. Ejecutar el script de fuerza bruta

En otra terminal, navega a la carpeta `attacker/` y ejecuta:

```bash
cd attacker
python brute_force.py
```

El script leerá `Top1575-probable.txt` y probará cada contraseña hasta encontrar la correcta.

## ❓ ¿Cómo Funciona?

- **Servidor Flask**: Tiene un formulario de login con credenciales ocultas en el código (`app.py`). Solo permite acceso si la combinación usuario/contraseña es correcta.
- **Ataque de fuerza bruta**: El script `brute_force.py` envía múltiples peticiones POST al servidor con las contraseñas de la lista hasta que recibe una respuesta que contiene `"Login successful"`.

## 🧪 Ejemplo

Cuando el script encuentra la contraseña correcta, imprime un mensaje como este:

```bash
[+] Contraseña encontrada: miContraseñaSegura123
```

## 🧩 Futuras mejoras

- Soporte para múltiples usuarios (`usernames.txt`)
- Interfaz gráfica con `argparse` o `Tkinter`
- Sistema de logs de intentos fallidos
- Manejo de bloqueos de IP (rate-limiting)

## 📄 Licencia

Este proyecto se distribuye bajo la Licencia MIT.

