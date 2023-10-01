import requests

def obtener_informacion_ubicacion(geonames_username, lugar):
    geo_url = f"http://api.geonames.org/searchJSON?name={lugar}&maxRows=1&username={geonames_username}"
    
    try:
        response = requests.get(geo_url)
        data = response.json()
        if "geonames" in data and data["geonames"]:
            ubicacion = data["geonames"][0]
            ciudad = ubicacion['name']
            pais = ubicacion['countryName']
            poblacion = ubicacion['population']
            return ciudad, pais, poblacion
        else:
            print("Ubicación no encontrada.")
            return None, None, None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None, None, None

def obtener_datos_meteorologicos(api_key, ciudad, pais, poblacion):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}"
    
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            print(f"Temperatura en {ciudad}, {pais} (Población: {poblacion}):")
            temperatura = data["main"]["temp"] - 273.15  # Convertir de Kelvin a Celsius
            condiciones_climaticas = data["weather"][0]["description"]
            print(f"Temperatura: {temperatura:.2f}°C")
            print(f"Condiciones climaticas en {ciudad}, {pais}: {condiciones_climaticas}")
        else:
            print(f"No se pudo obtener la información meteorológica para {ciudad}.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    # Coloca tu usuario de geonames
    geonames_username = "giovanni"
    api_key = "8a08339ce31835f5b1f11664d2507857"
    lugar = "México"  # Cambia esto a la ubicación que desees consultar
    ciudad, pais, poblacion = obtener_informacion_ubicacion(geonames_username, lugar)

    if ciudad:
        obtener_datos_meteorologicos(api_key, ciudad, pais, poblacion)
