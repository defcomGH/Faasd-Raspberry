from flask import Flask
from flask import jsonify
import time
import board

app = Flask(__name__)

def getTemperatura():
    try:
        temperature = 5
        return (temperature)
    except RuntimeError as error:
        print(error.args[0])

@app.route("/temperatura")
def temperatura():
    temp= str(getTemperatura())
    return jsonify(valor=temp,
                   unidad='Celsius')

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=6001)
