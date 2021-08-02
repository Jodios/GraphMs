from service.Graphing import createSimpleGraph
from flask import Flask, json, make_response, request

port = 8080
app = Flask(__name__)

@app.route('/simpleGraph', methods=['POST'])
def getSimpleGraph():
	data = json.loads(request.data)
	output = createSimpleGraph(data['x'], data['y'], data['coin'], data['time']) 
	response = make_response(output)
	response.mimetype = 'image/png'
	return response 

if __name__ == '__main__':
	app.run(port=port)






























