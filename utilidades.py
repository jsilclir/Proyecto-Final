"""
Módulo de utilidades para el conversor de monedas.

Contiene funciones auxiliares para validación de datos, formateo de números
y otras operaciones de soporte.
"""

from typing import Optional


def validar_numero(entrada: str) -> Optional[float]:
    """
    Valida que una entrada sea un número válido.
    
    Args:
        entrada: String a validar
        
    Returns:
        Float del número si es válido, None si no es válido
        
    Ejemplo:
        >>> validar_numero("123.45")
        123.45
        >>> validar_numero("abc")
        None
    """
    try:
        numero = float(entrada.replace(',', '.'))
        if numero < 0:
            print("Error: El monto no puede ser negativo.")
            return None
        return numero
    except ValueError:
        print("Error: Por favor ingresa un número válido.")
        return None


def formatear_moneda(monto: float, moneda: str) -> str:
    """
    Formatea un monto con el símbolo de la moneda correspondiente.
    
    Args:
        monto: Monto a formatear
        moneda: Código de la moneda (USD, EUR, BRL, ARS)
        
    Returns:
        String formateado con símbolo de moneda
        
    Ejemplo:
        >>> formatear_moneda(1500.50, "USD")
        "USD $1,500.50"
    """
    simbolos = {
        'USD': 'USD $',
        'EUR': 'EUR €',
        'BRL': 'BRL R$',
        'ARS': 'ARS $'
    }
    
    simbolo = simbolos.get(moneda, f'{moneda} ')
    return f"{simbolo}{monto:,.2f}"


def mostrar_cotizacion(moneda: str, cotizacion: dict) -> None:
    """
    Muestra la cotización de una moneda en formato legible.
    
    Args:
        moneda: Nombre de la moneda
        cotizacion: Dict con valores de compra y venta
    """
    print(f"\n--- {moneda} ---")
    print(f"Compra: {formatear_moneda(cotizacion['compra'], 'ARS')}")
    print(f"Venta:  {formatear_moneda(cotizacion['venta'], 'ARS')}")