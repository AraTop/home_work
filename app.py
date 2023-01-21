from flask import Flask , jsonify
from base import seach , years , ratings , genre
app = Flask(__name__)

@app.route("/movie/<title>")
def movie(title):
   data = seach(title)
   return jsonify(data)

@app.route("/movie/<int:one>/to/<int:two>")
def year(one , two):
   number = [one , two]
   data = years(min(number) , max(number)) 
   return jsonify(data)

@app.route("/rating/children")
def children():
   data = ratings("G")
   return jsonify(data)

@app.route("/rating/family")
def family():
   data = ratings("PG")
   data_two = ratings("PG-13")
   data_three = ratings("G")
   return jsonify(data , data_two , data_three)

@app.route("/rating/adult")
def adult():
   data = ratings("NC-17")
   data_two = ratings("R")
   return jsonify(data , data_two)
   
@app.route("/genre/<genr>")
def gen(genr):
   data = genre(genr)
   return jsonify(data)

app.run(debug=True) 
