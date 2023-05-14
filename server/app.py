# Hello world!
import os
from flask import Flask, request, jsonify, make_response
import requests
import random

app = Flask(__name__)
DEBUG = app.debug
API_KEY = "Bearer sW9VtHDsn6h_dkjQtZLewCsb2v1Cg9dHCoSX2oJHJXeVYvIuxJbCbO0daDiFe40iQG8rckCFOR1e_SXWSAMsCIfagLOjm0btopnwLc60UGEv1ak3Wz3pl_IlFgxgZHYx"
URL = "https://api.yelp.com/v3/businesses/search"

headers = {
    "accept": "application/json",
    "Authorization": API_KEY
}

#####################################################
# CORS section
#####################################################
@app.after_request
def after_request_func(response):
    if DEBUG:
        print("in after_request")
    origin = request.headers.get('Origin')
    if request.method == 'OPTIONS':
        response = make_response()
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Headers', 'x-csrf-token')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET, POST, OPTIONS, PUT, PATCH, DELETE')
        if origin:
            response.headers.add('Access-Control-Allow-Origin', origin)
    else:
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        if origin:
            response.headers.add('Access-Control-Allow-Origin', origin)

    return response


#####################################################
# end CORS section
#####################################################


@app.route('/')
def hello():
    return 'Welcome to Zipfinder Server Home page'


@app.route('/getrestaurant', methods=['GET'])
def restaurant():
    zipcode = "90277" # Test Value
    url = URL + '?location=' + zipcode + "&categories=food&sort_by=best_match&limit=20"

    response = requests.get(url, headers=headers)
    length = len(response.json()["businesses"])
    rand_business = random.randrange(0, length)
    return response.json()["businesses"][rand_business]["name"]
    

if __name__ == '__main__':
    app.run()