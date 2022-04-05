"""
Project Name: Real Time Translator
YouTube Transcript Summarizer API
"""


from flask import Flask, request, jsonify
from flask_cors import CORS

from translate import g_translate

app = Flask(__name__)
CORS(app)


@app.route('/api/', methods=['GET'])
def respond():

    # Get the input text
    text = request.args.get("ip_text", None)

    body = {}
    data = {}

    # Check if user doesn't provided  at all
    if not text or len(text) <= 0:
        data['message'] = "Failed"
        data['error'] = "No text found."

    else:
        data['message'] = "Success"
        data['hindi'] = g_translate(text, 'hi')
        data['gujarati'] = g_translate(text, 'gu')

    body["data"] = data

    # Return the response in json format
    return buildResponse(body)


# Welcome message to our server
@app.route('/')
def index():

    body = {}
    body['message'] = "Success"
    body['data'] = "Welcome to Translate API."

    return buildResponse(body)


def buildResponse(body):

    # from flask import json, Response
    # res = Response(response=json.dumps(body), status=statusCode, mimetype="application/json")
    # res.headers["Content-Type"] = "application/json; charset=utf-8"
    # return res

    response = jsonify(body)
    # response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == '__main__':

    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True)

# Deployment to Heroku Cloud.
