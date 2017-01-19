#!/usr/bin/python

'''
@todo

    1. Make a table in HTML that will display game history
        - Columns:
            - Player 1 Name
            - Player 1 Score
            - Player 2 Name
            - Player 2 Score
    2. Make another table that shows unique name pairings and each win totals
        - Columns:
            - Player 1 Name
            - Player 1 Wins
            - Player 2 Name
            - Player 2 Wins
    3. Make the api routes
        - GET
            - Returns the list of games
        - POST
            - Saves latest game to the db
    4. Create our own modal instead of just a browser alert
        - To make it more awesome!
'''

import tornado.ioloop
import tornado.web
import os
import json

global game_data;

file_handle = open('./games.json', 'r')
raw_data = file_handle.read()

if not raw_data:
    saved_data = {'games': []}
else:
    saved_data = json.loads(raw_data)

file_handle.close()

# todo: code defensively
game_data = saved_data;

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("static/html/example.html")

class GameHandler(tornado.web.RequestHandler):
    """ HTTP METHODS """
    
    """
    GET - read only, single item or a set of items
    """
    def get(self):
        self.set_header('Content-Type', 'application/json')
        self.write(json.dumps(game_data))
        self.finish()

    #"""
    #POST - for creating a record or set of records 
    #"""
    def post(self):
        if not self.request.body:
            self.set_status(400)
            return json.dumps({"status": 400, "message": "Empty request"})
        
        data = json.loads(self.request.body)
        game_data['games'].append(data)

        try:
            file_handle = open('./games.json', 'w')
            file_handle.write(json.dumps(game_data))
            file_handle.close()
        except Exception as e:
            print "Unable to save game data to disk"
            pass

        self.set_header('Content-Type', 'application/json')
        self.write(json.dumps({"status": 200, "message": "success", "games": game_data['games']}))
        self.finish()

    #"""
    #PUT - for updating a record or a set of records - should be idempotent
    #"""

    #"""
    #DELETE - for deleting a record or set of records
    ''' 
        @todo

        1. give each record an id
        2. remove that element from our in memory games array
        3. write our in memory games array to disc
        4. return our in memory games array
    '''
    #"""


def make_app():
    settings = {
        "static_path": os.path.join(os.path.dirname(__file__), "static")
    }

    return tornado.web.Application([ 
        (r"/", MainHandler),
        (r"/api/games", GameHandler)
    ], autoreload=True,
    **settings)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()