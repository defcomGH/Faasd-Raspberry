def handle(req): #Funcion que se comunica con el servidor y devuelve la humedad

    import requests

    url= 'http://10.62.0.1:6000/temperatura'

    humedad= requests.get(url).text

    return humedad
