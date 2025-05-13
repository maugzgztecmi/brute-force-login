# Herramienta de Fuerza Bruta para Formularios de Login

⚠️ Esta herramienta es únicamente para **fines educativos** y debe ser usada en **entornos de prueba controlados**.

## Estructura

- `server/`: Contiene un servidor Flask con un formulario vulnerable a fuerza bruta.
- `attacker/`: Contiene el script que realiza el ataque automatizado.

## Uso

1. Inicia el servidor:
   ```bash
   cd server
   python app.py
   ```

2. Ejecuta el atacante desde otra terminal:
   ```bash
   cd attacker
   python brute_force.py
   ```

## Requisitos

- Python 3.x
- Flask (`pip install flask`)
- requests (`pip install requests`)
