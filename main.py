import sqlite3 as sl
from flask import Flask, request, jsonify, after_this_request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"

con = sl.connect("messages.db", check_same_thread = False)

@app.route("/show_data")
def show_data():
    with con:
        raw_data = con.execute("SELECT * FROM USER")
        data = []
        for row in raw_data:
            print(row)
            data.append(row)
        print(data)
        return data

def show_data_by_num(num):
    jsonresp = {"count": 44}
    with con:
        data = con.execute("SELECT message FROM USER WHERE id IS {}".format(num))
        jsonresp["message"] = next(data)
    
    print(jsonresp)

@app.route("/add_message", methods=['POST'])
def add_message(num, message):
    inbox = request.form
    print(inbox)
    print("I got Calls !!!!!")
    sql = 'INSERT INTO USER (id, message) values(?, ?)'
    data = [
        (int(num), message)
    ]
    with con:
        con.executemany(sql, data)

@app.route("/count_inc", methods=['GET'])
def count_inc():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    with open("count", "r") as f:
        data = next(f)
        print(data)
    
    with open("count", "w") as f:
        f.write(str(int(data)+1))
    
    jsonresp = {"count": int(data)}

    with con:
        message = con.execute("SELECT message FROM USER WHERE id IS {}".format(data))
        for row in message:
            print(row)
            jsonresp["message"] = "".join(row)
    print(jsonresp)
    return jsonify(jsonresp)

hello_world()
print ("helo")
"""
DONE
if input("Increase Count? Y/N\n") == "Y":
    count_inc()

if input("Show all? Y/N\n") == "Y":   
    show_data()

DONE
if input("Show by Number? Y/N\n") == "Y": 
    show_data_by_num(input())
if input("Neue Date? Y/N\n") == "Y":
    add_message(int(input("Welche Nummer: ")),input("Welche Nachricht darfs sein: "))
    """
