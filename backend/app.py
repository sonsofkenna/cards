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

  print("here")
  reponse_object = {'status': 200}

  print('h')

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
      card['author']['_id'] = str(card['author']['_id'])
      cards.append(card)

    reponse_object['cards'] = cards
  elif request.method == 'POST':

    card = request.get_json()
    mycol = db["cards"]

    # card = { "content": "asdfasdf", "author": 1, "likes": 1 }

    x = mycol.insert_one(card)
    reponse_object = {'status': 201}

  return jsonify(reponse_object)

@app.route('/users')
def users():
  response_object = {'status': 200}

  if request.method == 'GET':
    cursor = db.users.find({})
    result = []

    for document in cursor:
      document['_id'] = str(document['_id'])
      result.append(document)

    response_object['users'] = result

  return jsonify(response_object)

@app.route('/users/<user_id>')
def user(user_id):
  response_object = {'status': 200}

  if request.method == 'GET':
    result = db.users.find_one({'id': user_id})
    result['_id'] = str(result['_id'])

    response_object['user'] = result

  return jsonify(response_object)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3000)
  # app.run(port=3000, debug=False)