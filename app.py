from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", error="incorrect username")

@app.route('/process', methods=['GET'])
def process():
    username = request.args.get('username')
    password = request.args.get('password')

    conn = sqlite3.connect("database/data.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM data WHERE name = ? AND password = ?", (username, password))
    result = cur.fetchall()

    if result:
        id = result[0][0]
        return f"Log-in Successfully. ID: {id}", 302, {'Location': f"/user?id={id}"}
    else:
        return f'No Entry Username: {username}, Password: {password}'

@app.route('/user', methods=['GET'])
def user():
    user_id = request.args.get('id')
    conn = sqlite3.connect("database/data.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM data WHERE ID == ?", (user_id,))
    data = cur.fetchall()
    print(data)
    username = data[0][1]
    phno = data[0][2]
    mail = data[0][3]
    pasW = data[0][4]
    return render_template("welcome.html",name = username , phoneno = phno , mail = mail , pawd = pasW )

if __name__ == "__main__":
    app.run(port=80)
