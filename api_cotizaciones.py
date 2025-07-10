"""
Módulo para consultar cotizaciones de divisas.

Este módulo se encarga de obtener cotizaciones actualizadas de diferentes
divisas (USD, EUR, BRL) desde APIs externas y manejar errores de conexión.
"""

import requests
from typing import Dict, Optional


def obtener_cotizacion_dolar() -> Optional[Dict[str, float]]:
    """
    Obtiene la cotización del dólar oficial desde DolarApi.
    
    Returns:
        Dict con 'compra' y 'venta' del dólar, o None si hay error.
        
    Ejemplo:
        >>> cotizacion = obtener_cotizacion_dolar()
        >>> print(cotizacion['venta'])
        1280.0
    """
    try:
        url = "https://dolarapi.com/v1/dolares/oficial"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        return {
            'compra': float(data['compra']),
            'venta': float(data['venta'])
        }
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener cotización del dólar: {e}")
        return None
    except (KeyError, ValueError) as e:
        print(f"Error al procesar datos del dólar: {e}")
        return None
    

def obtener_cotizacion_euro() -> Optional[Dict[str, float]]:
    """
    Obtiene la cotización del euro desde una API de cambio.
    
    Returns:
        Dict con 'compra' y 'venta' del euro en pesos argentinos, o None si hay error.
    """
    try:
        # Primero obtenemos EUR a USD
        url = "https://api.exchangerate-api.com/v4/latest/EUR"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        eur_to_usd = data['rates']['USD']
        
        # Luego obtenemos el dólar oficial
        dolar_data = obtener_cotizacion_dolar()
        if dolar_data is None:
            return None
            
        # Calculamos EUR a ARS
        compra_ars = eur_to_usd * dolar_data['compra']
        venta_ars = eur_to_usd * dolar_data['venta']
        
        return {
            'compra': round(compra_ars, 2),
            'venta': round(venta_ars, 2)
        }
        
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener cotización del euro: {e}")
        return None
    except (KeyError, ValueError) as e:
        print(f"Error al procesar datos del euro: {e}")
        return None


def obtener_cotizacion_real() -> Optional[Dict[str, float]]:
    """
    Obtiene la cotización del real brasileño desde una API de cambio.
    
    Returns:
        Dict con 'compra' y 'venta' del real en pesos argentinos, o None si hay error.
    """
    try:
        # Primero obtenemos BRL a USD
        url = "https://api.exchangerate-api.com/v4/latest/BRL"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        brl_to_usd = data['rates']['USD']
        
        # Luego obtenemos el dólar oficial
        dolar_data = obtener_cotizacion_dolar()
        if dolar_data is None:
            return None
            
        # Calculamos BRL a ARS
        compra_ars = brl_to_usd * dolar_data['compra']
        venta_ars = brl_to_usd * dolar_data['venta']
        
        return {
            'compra': round(compra_ars, 2),
            'venta': round(venta_ars, 2)
        }
        
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener cotización del real: {e}")
        return None
    except (KeyError, ValueError) as e:
        print(f"Error al procesar datos del real: {e}")
        return None