
from MisContantes import (
    CELSIUS_A_FAHRENHEIT,
    FAHRENHEIT_A_CELSIUS,
    CELSIUS_A_KELVIN,
    KELVIN_A_CELSIUS
)

class ConversorTemperatura:
    MENSAJE_BIENVENIDA = "Bienvenido al Conversor de Temperatura"

    def __init__(self):
        print(self.MENSAJE_BIENVENIDA)
        self.mostrar_menu()

    def mostrar_menu(self):
        while True:
            print("\n Menú de Conversión de Temperatura ")
            print("1. Convertir de Celsius a Fahrenheit")
            print("2. Convertir de Fahrenheit a Celsius")
            print("3. Convertir de Celsius a Kelvin")
            print("4. Convertir de Kelvin a Celsius")
            print("5. Salir")

            opcion = input("Selecciona una opción 1 al 5 : ")

            if opcion == '1':
                self.convertir_celsius_a_fahrenheit()
            elif opcion == '2':
                self.convertir_fahrenheit_a_celsius()
            elif opcion == '3':
                self.convertir_celsius_a_kelvin()
            elif opcion == '4':
                self.convertir_kelvin_a_celsius()
            elif opcion == '5':
                print("¡Gracias por usar el conversor!")
                break
            else:
                print("Opción no válida. Por favor, selecciona una opción del 1 al 5.")

    def convertir_celsius_a_fahrenheit(self):
        celsius = float(input("Ingresa la temperatura en Celsius: "))
        fahrenheit = CELSIUS_A_FAHRENHEIT(celsius)
        print(f"{celsius}°C es igual a {fahrenheit}°F")

    def convertir_fahrenheit_a_celsius(self):
        fahrenheit = float(input("Ingresa la temperatura en Fahrenheit: "))
        celsius = FAHRENHEIT_A_CELSIUS(fahrenheit)
        print(f"{fahrenheit}°F es igual a {celsius}°C")

    def convertir_celsius_a_kelvin(self):
        celsius = float(input("Ingresa la temperatura en Celsius: "))
        kelvin = CELSIUS_A_KELVIN(celsius)
        print(f"{celsius}°C es igual a {kelvin}K")

    def convertir_kelvin_a_celsius(self):
        kelvin = float(input("Ingresa la temperatura en Kelvin: "))
        celsius = KELVIN_A_CELSIUS(kelvin)
        print(f"{kelvin}K es igual a {celsius}°C")



if __name__ == "__main__":
    conversor = ConversorTemperatura()