import sqlite3 as sl

con = sl.connect("messages.db")

def show_data():
    with con:
        data = con.execute("SELECT * FROM USER")
        for row in data:
            print(row)

def show_data_by_num(num):
    with con:
        data = con.execute("SELECT * FROM USER WHERE id IS {}".format(num))
        for row in data:
            print(row)

def add_data(num, message):
    sql = 'INSERT INTO USER (id, message) values(?, ?)'
    data = [
        (int(num), message)
    ]
    with con:
        con.executemany(sql, data)


def count_inc():
    with open("count", "r") as f:
        data = next(f)
        print(data)
    
    with open("count", "w") as f:
        f.write(str(int(data)+1))




if input("Increase Count? Y/N\n") == "Y":
    count_inc()

if input("Neue Date? Y/N\n") == "Y":
    add_data(int(input("Welche Nummer: ")),input("Welche Nachricht darfs sein: "))

if input("Show all? Y/N\n") == "Y":   
    show_data()

if input("Show by Number? Y/N\n") == "Y": 
    show_data_by_num(input())
