# server.py

# from flask import Flask, jsonify
#
# app = Flask(__name__)
#
# tasks = [
#     {
#         'id': 1,
#         'title': u'Buy groceries',
#         'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
#         'done': False
#     },
#     {
#         'id': 2,
#        'title': u'Learn Python',
#         'description': u'Need to find a good Python tutorial on the web',
#         'done': False
#     }
# ]
#
#
# @app.route('/todo/api/v1.0/tasks', methods=['GET'])
# def get_tasks():
#     return jsonify({'tasks': tasks})
#
#
# if __name__ == '__main__':
#     app.run(debug=True)


# -------------------------------------------------------------------

'''

delete(url, args)   Sends a DELETE request to the specified url

get(url, params, args)  Sends a GET request to the specified url

head(url, args) Sends a HEAD request to the specified url

patch(url, data, args)  Sends a PATCH request to the specified url

post(url, data, json, args) Sends a POST request to the specified url

put(url, data, args)    Sends a PUT request to the specified url

request(method, url, args)  Sends a request of the specified method to the specified url

'''

# client.py

import requests

import json

url = 'http://localhost:5000/todo/api/v1.0/tasks'

# response = requests.get(url)

# print(str(response))

# print('')

# print(json.dumps(response.json(), indent=4))


my_data = {'title': 'Read a book'}

response = requests.patch('https://httpbin.org / patch',

                          data=my_data)

# check status code for response received

# success code - 200

print(response)

# print content of request

print(response.content)
