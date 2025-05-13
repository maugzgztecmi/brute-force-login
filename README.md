# Brute Force Login Tool (Para pruebas locales)

Este proyecto es una herramienta de **fuerza bruta** diseñada para realizar pruebas de seguridad en un formulario de login simulado. El proyecto consiste en un servidor Flask que expone un formulario de inicio de sesión, y un script que intenta encontrar la contraseña correcta utilizando un diccionario de contraseñas.

> ⚠️ **Advertencia:** Esta herramienta debe usarse exclusivamente en entornos controlados y con fines educativos o de prueba ética. No está diseñada para ser usada en sistemas reales sin el consentimiento explícito del propietario.

---

## 💻 Estructura del Proyecto

El proyecto está dividido en dos partes:

1. **Servidor Flask (`server/`)**  
   Un servidor web simple con un formulario de login simulado.

2. **Herramienta de Fuerza Bruta (`attacker/`)**  
   Un script que intenta descubrir la contraseña correcta mediante un ataque de fuerza bruta utilizando una lista de contraseñas.

---

## 🛠 Requisitos

### 1. Instalar Python

Asegúrate de tener Python 3.x instalado en tu sistema. Puedes verificarlo con:

```bash
python --version
```

Si no lo tienes, instálalo desde [https://www.python.org](https://www.python.org).

---

### 2. Instalar dependencias

El proyecto depende de las siguientes librerías de Python:

- `Flask`: para el servidor web.
- `requests`: para enviar peticiones HTTP desde el script de fuerza bruta.

Instálalas con:

```bash
pip install flask requests
```

---

### 3. Descargar `rockyou.txt`

Este proyecto utiliza el archivo `rockyou.txt` como diccionario de contraseñas para las pruebas de fuerza bruta. Esta lista contiene contraseñas populares y comúnmente usadas.

> ⚠️ **Importante:** Debido a su tamaño (~133 MB), este archivo no está incluido en el repositorio.

Puedes descargarlo desde:

📥 [https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt)

Una vez descargado, colócalo en la raíz del proyecto (junto a las carpetas `server/` y `attacker/`) y asegúrate de que se llame exactamente `rockyou.txt`.

---

## 🚀 Cómo Ejecutarlo

### 1. Levantar el servidor Flask

En una terminal, navega a la carpeta `server/` y ejecuta:

```bash
python app.py
```

Esto iniciará un servidor web en [http://127.0.0.1:5000](http://127.0.0.1:5000), con un formulario de login accesible desde tu navegador.

---

### 2. Ejecutar el script de fuerza bruta

En otra terminal, navega a la carpeta `attacker/` y ejecuta:

```bash
python brute_force.py
```

El script leerá `rockyou.txt` e intentará cada contraseña hasta encontrar la correcta. Al acertar, mostrará un mensaje indicando la contraseña descubierta.

---

## 🔐 Diccionario de contraseñas: `rockyou.txt`

Este archivo es ampliamente usado en pruebas de seguridad y contiene millones de contraseñas reales filtradas de bases de datos públicas.

> ⚠️ **Nota:** No se incluye por defecto en este repositorio. Debes descargarlo manualmente y colocarlo en la raíz del proyecto.

📥 [Descargar rockyou.txt](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt)

---

## ❓ ¿Cómo Funciona?

### Servidor Flask:
El servidor tiene un formulario de login que permite acceder solo con la combinación correcta de usuario y contraseña.  
Por defecto, el usuario es `admin` y la contraseña es `password123`.

### Ataque de Fuerza Bruta:
El script `brute_force.py` toma el archivo `rockyou.txt` y prueba cada una de las contraseñas contra el servidor Flask.  
Cuando el servidor responde con `"Login successful"`, el script detiene el ataque y muestra la contraseña correcta.

---

## 🚧 Futuras Mejoras

- Soporte para múltiples usuarios (por ejemplo, desde un archivo `usernames.txt`)
- Interfaz gráfica (Tkinter o CLI con `argparse`)
- Sistema de logs para registrar intentos
- Detección de bloqueo por IP o medidas anti-bot

---

## 📄 Licencia

Este proyecto se distribuye bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.
