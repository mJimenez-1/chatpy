# import flask dependencies
import json
from flask import Flask, request, make_response, jsonify

# initialize the flask app
app = Flask(__name__)

# default route
@app.route('/')
def index():
    return 'Hello World!'

# function for responses
def results():
    # build a request object
    req = request.get_json(force=True)

    # fetch action from json
    action = req.get('queryResult').get('action')
    
    parametro = req.get('queryResult').get('parameters')

    parametro["any"] = 'burger'
    parametro["any1"] = 'coke'
    
    

    with open('data.json') as f:
        data = json.load(f)
        for datos in data['pedidos']:
            if parametro['number'] == datos['numeropedido'] and parametro['number'] == datos['numeropedido']:
            
                return {'fulfillmentText': 'Hola ' + datos['cliente'] + ', Su datos fueron validados'}
                if datos['estado']=='pendiente':
                    return {'fulfillmentText': 'Tienes un pedido que sera entregado'}
                else:
                    return {'fulfillmentText': 'No tiene pedido, escribe solicitud y elegige una opcion.'}    


    # return a fulfillment response
   

# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # return response
    return make_response(jsonify(results()))

# run the app
if __name__ == '__main__':
   app.run()