# Conversor de Monedas en Python

Programa para consultar cotizaciones de dólar estadounidense (USD), euro (EUR) y real (BRL) en tiempo real, y convertir montos a pesos argentinos (ARS).

## Requisitos
- Python 3.8+
- Librería `requests` (instalar con `pip install requests`).
- Conexión a internet (para consultar APIs).

## Instalación
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/tu-repo.git
   cd tu-repo

## Crear Entorno Virtual
 CLI
  python -m venv venv
  source venv/bin/activate  # Linux/Mac
  venv\Scripts\activate    # Windows

## Instalar Dependencias
   pip install -r requirements.txt

## Uso
- Ejecutar
    python conversor.py
- Opciones
    1. Ver cotizaciones actuales.
    2. Convertir USD a ARS.
    3. Convertir EUR a ARS.
    4. Convertir BRL a ARS.
    5. Salir del programa.

## Ejemplos de Uso
1. Ingresa la cantidad de dólares a convertir: 100
2. Resultado de la conversión:
 - Monto: USD $100.00
 - Al precio de compra: ARS $127,500.00
 - Al precio de venta: ARS $128,000.00

## Estructura del Proyecto
Proyecto Final/
│
├── conversor.py           # Programa principal
├── api_cotizaciones.py    # Módulo para consultas a APIs
├── utilidades.py          # Funciones auxiliares
├── requirements.txt       # Dependencias
├── .gitignore             # Archivos ignorados por Git
├── README.md              # Este archivo
└── venv/                  # Entorno virtual (creado localmente)

## APIs utilizadas
- DolarApi: https://dolarapi.com/v1/dolares/oficial
- ExchangueRate API: https://api.exchangerate-api.com/v4/latest/

## Autor
Silclir, Jaime - Proyecto Final - Programación I