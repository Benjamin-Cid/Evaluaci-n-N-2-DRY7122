import requests

def obtener_info_viaje(origen, destino, token):
    url = f"https://graphhopper.com/api/1/route?point={origen}&point={destino}&vehicle=car&locale=es&calc_points=true&key={token}"
    
    response = requests.get(url)
    data = response.json()

    distancia_km = data['paths'][0]['distance'] / 1000
    duracion_segundos = data['paths'][0]['time'] / 1000
    duracion_horas = int(duracion_segundos // 3600)
    duracion_minutos = int((duracion_segundos % 3600) // 60)
    duracion_segundos = int(duracion_segundos % 60)

    # Suponiendo un consumo de 12 km por litro
    consumo_litros = distancia_km / 12

    print(f"\nNarrativa del viaje desde {origen} hasta {destino}:")
    print(f"Distancia: {distancia_km:.2f} km")
    print(f"Duración: {duracion_horas}h {duracion_minutos}m {duracion_segundos}s")
    print(f"Combustible estimado: {consumo_litros:.2f} litros\n")

if __name__ == "__main__":
    token = "TU_TOKEN_AQUI"
    while True:
        print("Ingrese 'q' en cualquier momento para salir.")
        origen = input("Ciudad de origen: ")
        if origen.lower() == 'q':
            break
        destino = input("Ciudad de destino: ")
        if destino.lower() == 'q':
            break

        # Convierte nombres a coordenadas (simplificado o puedes usar API de geocodificación)
        coordenadas = {
            "santiago": "-33.4489,-70.6693",
            "puerto montt": "-41.4717,-72.9396"
        }

        if origen.lower() not in coordenadas or destino.lower() not in coordenadas:
            print("Una o ambas ciudades no están disponibles en el programa.")
            continue

        origen_coords = coordenadas[origen.lower()]
        destino_coords = coordenadas[destino.lower()]

        obtener_info_viaje(origen_coords, destino_coords, token)
