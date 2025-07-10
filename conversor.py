"""
Conversor de Monedas - Programa Principal

Aplicación para convertir divisas (USD, EUR, BRL) a pesos argentinos
usando cotizaciones actualizadas desde APIs externas.
"""

import api_cotizaciones
import utilidades


def mostrar_menu() -> None:
    """Muestra el menú principal de opciones."""
    print("\n" + "="*50)
    print("         CONVERSOR DE MONEDAS")
    print("="*50)
    print("1. Ver cotizaciones actuales")
    print("2. Convertir USD a ARS")
    print("3. Convertir EUR a ARS") 
    print("4. Convertir BRL a ARS")
    print("5. Salir")
    print("="*50)


def ver_cotizaciones() -> None:
    """Muestra las cotizaciones actuales de todas las monedas."""
    print("\n🔄 Obteniendo cotizaciones actualizadas...")
    
    # Obtener cotizaciones
    dolar = api_cotizaciones.obtener_cotizacion_dolar()
    euro = api_cotizaciones.obtener_cotizacion_euro()
    real = api_cotizaciones.obtener_cotizacion_real()
    
    # Mostrar resultados
    if dolar:
        utilidades.mostrar_cotizacion("DÓLAR ESTADOUNIDENSE", dolar)
    else:
        print("❌ No se pudo obtener la cotización del dólar")
        
    if euro:
        utilidades.mostrar_cotizacion("EURO", euro)
    else:
        print("❌ No se pudo obtener la cotización del euro")
        
    if real:
        utilidades.mostrar_cotizacion("REAL BRASILEÑO", real)
    else:
        print("❌ No se pudo obtener la cotización del real")


def convertir_moneda(tipo_moneda: str) -> None:
    """
    Convierte una cantidad de moneda extranjera a pesos argentinos.
    
    Args:
        tipo_moneda: Tipo de moneda a convertir (USD, EUR, BRL)
    """
    # Mapeo de monedas
    monedas = {
        'USD': {
            'nombre': 'dólares',
            'funcion': api_cotizaciones.obtener_cotizacion_dolar
        },
        'EUR': {
            'nombre': 'euros', 
            'funcion': api_cotizaciones.obtener_cotizacion_euro
        },
        'BRL': {
            'nombre': 'reales',
            'funcion': api_cotizaciones.obtener_cotizacion_real
        }
    }
    
    if tipo_moneda not in monedas:
        print("❌ Moneda no válida")
        return
    
    # Obtener cotización
    print(f"\n🔄 Obteniendo cotización del {tipo_moneda}...")
    cotizacion = monedas[tipo_moneda]['funcion']()
    
    if cotizacion is None:
        print(f"❌ No se pudo obtener la cotización del {tipo_moneda}")
        return
    
    # Mostrar cotización actual
    utilidades.mostrar_cotizacion(f"{tipo_moneda} - {monedas[tipo_moneda]['nombre'].upper()}", cotizacion)
    
    # Solicitar monto
    while True:
        entrada = input(f"\n💰 Ingresa la cantidad de {monedas[tipo_moneda]['nombre']} a convertir: ")
        monto = utilidades.validar_numero(entrada)
        
        if monto is not None:
            break
        print("Por favor, intenta nuevamente.")
    
    # Realizar conversión
    conversion_compra = monto * cotizacion['compra']
    conversion_venta = monto * cotizacion['venta']
    
    # Mostrar resultado
    print(f"\n💸 RESULTADO DE LA CONVERSIÓN:")
    print(f"📊 Monto: {utilidades.formatear_moneda(monto, tipo_moneda)}")
    print(f"🏦 Al precio de compra: {utilidades.formatear_moneda(conversion_compra, 'ARS')}")
    print(f"🏪 Al precio de venta: {utilidades.formatear_moneda(conversion_venta, 'ARS')}")


def main() -> None:
    """Función principal del programa."""
    print("¡Bienvenido al Conversor de Monedas! 🌍💱")
    
    while True:
        mostrar_menu()
        opcion = input("\n👉 Selecciona una opción (1-5): ").strip()
        
        if opcion == '1':
            ver_cotizaciones()
        elif opcion == '2':
            convertir_moneda('USD')
        elif opcion == '3':
            convertir_moneda('EUR')
        elif opcion == '4':
            convertir_moneda('BRL')
        elif opcion == '5':
            print("\n👋 ¡Gracias por usar el conversor! ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida. Por favor selecciona una opción del 1 al 5.")
        
        # Pausa para que el usuario pueda leer
        input("\n📋 Presiona Enter para continuar...")


if __name__ == "__main__":
    main()