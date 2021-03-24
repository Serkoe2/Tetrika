from flask import Flask , request
from appearance import appearance

app = Flask(__name__)

@app.route("/API/v1.1/appearance",methods=['POST'])
def powerOnDevice(deviceID):
    params = request.get_json()
    response = appearance(params)
    return str(response)

app.run()
