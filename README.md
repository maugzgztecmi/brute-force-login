# Brute Force Login Tool (Para pruebas locales)

Este proyecto es una herramienta de **fuerza bruta** diseñada para realizar pruebas de seguridad en un formulario de login simulado. El proyecto consiste en un servidor Flask que expone un formulario de inicio de sesión, y un script que intenta encontrar la contraseña correcta utilizando un diccionario de contraseñas.

> **⚠️ Advertencia:** Esta herramienta debe usarse exclusivamente en entornos controlados y con fines educativos o de prueba ética. No está diseñada para ser usada en sistemas reales sin el consentimiento explícito del propietario.

## 💻 Estructura del Proyecto

El proyecto está dividido en dos partes:

1. **Servidor Flask (`server/`)**
   - Un servidor web simple con un formulario de login simulado.
   
2. **Herramienta de Fuerza Bruta (`attacker/`)**
   - Un script que intenta descubrir la contraseña correcta a través de un ataque de fuerza bruta utilizando una lista de contraseñas.

## 🛠 Requisitos

### 1. **Instalar Python**
   Asegúrate de tener Python 3.x instalado en tu sistema. Puedes verificarlo con:

   ```bash
   python --version

