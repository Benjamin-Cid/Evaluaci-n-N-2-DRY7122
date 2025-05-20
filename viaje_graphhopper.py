import requests

# Coordenadas fijas para ciudades
ciudades = {
    "santiago": "-33.4489,-70.6693",
    "puerto montt": "-41.4717,-72.9396"
}

# Función principal
def obtener_datos_viaje(origen_coords, destino_coords, token):
    url = f"https://graphhopper.com/api/1/route?point={origen_coords}&point={destino_coords}&vehicle=car&locale=es&key={token}"
    response = requests.get(url)
    datos = response.json()

    distancia_km = datos['paths'][0]['distance'] / 1000
    duracion_seg = datos['paths'][0]['time'] / 1000

    horas = int(duracion_seg // 3600)
    minutos = int((duracion_seg % 3600) // 60)
    segundos = int(duracion_seg % 60)

    consumo_litros = distancia_km / 12  # Suponiendo rendimiento 12 km/l

    print(f"\n🧭 Narrativa del viaje:")
    print(f"De: {origen_coords}  A: {destino_coords}")
    print(f"Distancia: {distancia_km:.2f} km")
    print(f"Duración: {horas}h {minutos}m {segundos}s")
    print(f"Combustible estimado: {consumo_litros:.2f} litros\n")

# Programa principal
if __name__ == "__main__":
    token = "4c5f6c8e-ae86-4982-af1e-ed44fedcbf3b"

    while True:
        print("Ingrese 'q' para salir.")
        origen = input("Ciudad de origen (ej: Santiago): ").lower()
        if origen == "q":
            break
        destino = input("Ciudad de destino (ej: Puerto Montt): ").lower()
        if destino == "q":
            break

        if origen in ciudades and destino in ciudades:
            origen_coords = ciudades[origen]
            destino_coords = ciudades[destino]
            obtener_datos_viaje(origen_coords, destino_coords, token)
        else:
            print("❌ Ciudad no reconocida. Intenta con 'Santiago' o 'Puerto Montt'.\n")
