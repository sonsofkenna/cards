import uuid
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from pymongo import MongoClient

client = MongoClient('database', port=27017)
db = client.cards

app = Flask(__name__)

 
@app.route('/')
def index():
  api_calls = {
    'users': '/users',
    'cards': '/cards'
  }

  return jsonify(api_calls)

@app.route('/cards', methods=['POST', 'GET'])
def cards():

  reponse_object = {'status': 200}

  if request.method == 'GET':
    result = db.cards.find(
      filter={},
      projection={
        '_id': 0,
        'id': 1,
        'content': 1,
        'author': 1,
        'likes': 1,
        'shares': 1
      }
    )

    cards = []

    for card in result:
      cards.append(card)

    # reponse_object['cards'] = cards
    return jsonify({'result' : cards})
  elif request.method == 'POST':

    card = request.get_json()
    mycol = db["cards"]


    x = mycol.insert_one(card)
    reponse_object = {'status': 201}

  return jsonify(reponse_object)

@app.route('/users', methods=['POST', 'GET'])
def users():

  if request.method == 'GET':
    result = db.users.find(
      filter={},
      projection={
        '_id': 0,
        'id': 1,
        'first': 1,
        'last': 1,
        'nick': 1,
        'pfp': 1,
        'followers':1
      }
    )

    authors = []

    for author in result:
      authors.append(author)

    return jsonify({'result' : authors})
  elif request.method == 'POST':

    author = request.get_json()
    mycol = db["users"]


    x = mycol.insert_one(author)
    reponse_object = {'status': 201}

  return jsonify(reponse_object)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3000)
  # app.run(port=3000, debug=False)