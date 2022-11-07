def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    import time
    import board
    import adafruit_dht
    #import RPi

    #Iniciar el sensor dht, conectado al pin 17
    dhtDevice = adafruit_dht.DHT11(board.D17)

    try:
        temperature = float(dhtDevice.temperature)
        return (temperature)
    except RuntimeError as error:
        print(error.args[0])
    return req 


