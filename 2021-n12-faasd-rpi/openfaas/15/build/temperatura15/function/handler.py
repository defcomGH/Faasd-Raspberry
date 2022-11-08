def handle(req): #Funcion que se comunica con el servidor y devuelve la temperatura

    import requests

    url= 'http://10.0.0.15:6000/temperatura'

    temperatura= requests.get(url).text

    return temperatura
