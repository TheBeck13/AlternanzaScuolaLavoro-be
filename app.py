from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
import pandas as pd


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

class InputDTO:
    def __init__(self, name, club_from, club_to, league_from, league_to, country_from, country_to, position, age_from, age_to, value_from, value_to, loan, year_from, year_to):
        self.name = name
        self.club_from = club_from
        self.club_to = club_to
        self.league_from = league_from
        self.league_to = league_to
        self.country_from = country_from
        self.country_to = country_to
        self.position = position
        self.age_from = age_from
        self.age_to = age_to
        self.value_from = value_from
        self.value_to = value_to
        self.loan = loan
        self.year_from = year_from
        self.year_to = year_to

    def __init__(self):
        self.name = ""
        self.club_from = ""
        self.club_to = ""
        self.league_from = ""
        self.league_to = ""
        self.country_from = ""
        self.country_to = ""
        self.position = ""
        self.age_from = 0
        self.age_to = 100
        self.value_from = 0
        self.value_to = 1000000000
        self.loan = 0
        self.year_from = 0
        self.year_to = 2023

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_club_from(self):
        return self.club_from
    
    def set_club_from(self, club_from):
        self.club_from = club_from

    def get_club_to(self):
        return self.club_to
    
    def set_club_to(self, club_to):
        self.club_to = club_to
    
    def get_league_from(self):
        return self.league_from
    
    def set_league_from(self, league_from):
        self.league_from = league_from

    def get_league_to(self):
        return self.league_to
    
    def set_league_to(self, league_to):
        self.league_to = league_to
    
    def get_position(self):
        return self.position
    
    def set_position(self, position):
        self.position = position

    def get_age_from(self):
        return self.age_from
    
    def set_age_from(self, age_from):
        self.age_from = age_from

    def get_age_to(self):
        return self.age_to
    
    def set_age_to(self, age_to):
        self.age_to = age_to

    def get_value_from(self):
        return self.value_from
    
    def set_value_from(self, value_from):
        self.value_from = value_from

    def get_value_to(self):
        return self.value_to
    
    def set_value_to(self, value_to):
        self.value_to = value_to
    
    def get_loan(self):
        return self.loan
    
    def set_loan(self, loan):
        self.loan = loan

    def get_year_from(self):
        return self.year_from
    
    def set_year_from(self, year_from):
        self.year_from = year_from

    def get_year_to(self):
        return self.year_to
    
    def set_year_to(self, year_to):
        self.year_to = year_to

    def get_data(self):
        return {
            "name": self.name,
            "club_from": self.club_from,
            "club_to": self.club_to,
            "league_from": self.league_from,
            "league_to": self.league_to,
            "position": self.position,
            "age_from": self.age_from,
            "age_to": self.age_to,
            "value_from": self.value_from,
            "value_to": self.value_to,
            "loan": self.loan,
            "year_from": self.year_from,
            "year_to": self.year_to
        }
    
    def set_data(self, data):
        if self.name != data['name']:
            self.name = data["name"]
        if data['club_from'] != self.club_from:
            self.club_from = data["club_from"]
        if data['club_to'] != self.club_to:
            self.club_to = data["club_to"]
        if data['league_from'] != self.league_from:
            self.league_from = data["league_from"]
        if data['league_to'] != self.league_to:
            self.league_to = data["league_to"]
        if data['position'] != self.position:
            self.position = data["position"]
        if data['age_from'] != self.age_from:
            self.age_from = data["age_from"]
        if data['age_to'] != self.age_to:
            self.age_to = data["age_to"]
        if data['value_from'] != self.value_from:
            self.value_from = data["value_from"]
        if data['value_to'] != self.value_to:
            self.value_to = data["value_to"]
        if data['loan'] != self.loan:
            self.loan = data["loan"]
        if data['year_from'] != self.year_from:
            self.year_from = data["year_from"]
        if data['year_to'] != self.year_to:
            self.year_to = data["year_to"]

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Content-Type'] = 'application/json'
    return response
        
@app.route('/api/v1/health', methods=['GET'])
def health():
    input = InputDTO("Gennaro")
    print(input.get_data())
    return make_response(jsonify({'status': 'ok'})) #pass a dict

@app.route('/api/v1/echo', methods=['POST'])
def echo():
    data = request.get_json() #dict
    return make_response(jsonify(data))

@app.route('/api/v1/startvalues', methods=['GET'])
def startup():
    data = {
        "team_list": team_list,
        "country_list": country_list,
        "league_list": league_list,
        "position_list": position_list
    }
    return make_response(jsonify(data))

@app.route('/api/v1/search', methods = ['POST'])
def search():
    data = request.get_json()
    input = InputDTO()
    input.set_data(data)
    print(input.get_data())
    return make_response(jsonify(input.get_data()))


if __name__ == '__main__':
    df = pd.read_csv('archive.csv', low_memory=False, index_col=0)
    team_list = list(set(df['club_from'].unique()) | set(df["club_to"].unique()))
    country_list = list(set(df['country_from'].unique()) | set(df["country_to"].unique()))
    league_list = list(set(df['league_from'].unique()) | set(df["league_to"].unique()))
    position_list = list(df['position'].unique())
    
    app.run(debug=True, host='localhost', port=5000)