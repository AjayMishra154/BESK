from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)


@app.route("/")
def index():
    con = sqlite3.connect("Besk.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from Book")
    rows = cur.fetchall()
    print(rows)
    return render_template("index.html", rows=rows)


@app.route("/log")
def login():
    return render_template("login.html")


@app.route("/login_check", methods=["POST", "GET"])
def logincheck():
    # con = sqlite3.connect("Besk.db")
    # con.row_factory = sqlite3.Row
    # cur = con.cursor()
    # cur.execute("select * from Book")
    # rows = cur.fetchall()

    if request.method == "POST":
        username = request.form['username']
        password = request.form["password"]

        with sqlite3.connect("Besk.db") as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute("select * from users")
            rows = cur.fetchall()
            for user in rows:
                if username == user["user"] and password == user["password"]:
                    conn.row_factory = sqlite3.Row
                    cur = conn.cursor()
                    cur.execute("select * from Book")
                    rows = cur.fetchall()
                    return render_template("loggedin.html", rows=rows)

            return render_template("feedback.html", msg="failure")


@app.route("/signup")
def signup():
    return render_template("sign-up.html")


@app.route("/savedetails", methods=["POST", "GET"])
def saveDetails():
    msg = "msg"
    if request.method == "POST":
        try:
            username = request.form["username"]
            password = request.form["password"]
            with sqlite3.connect("Besk.db") as conn:
                cur = conn.cursor()
                cur.execute("INSERT into users(user,password)  values (?,?)", (username, password))
                conn.commit()
                msg = "logged in"

        except:
            conn.rollback()
            msg = "we can not add the user to the list"

        finally:
            conn.close()
            return render_template("feedback.html", msg=msg)


@app.route("/add")
def add():
    return render_template("add.html")


@app.route("/adding", methods=['POST', 'GET'])
def save():
    msg = "ggggggggg"
    if request.method == 'POST':

        name = request.form['name']
        book_name = request.form['book']
        description = request.form['description']
        book_img = request.form['image']
        email = request.form['email']
        try:
            with sqlite3.connect("Besk.db") as conn:
                cur = conn.cursor()
                cur.execute("INSERT into Book values (?,?,?,?,?)", (name, book_name, description, book_img, email))
                conn.commit()
                msg = "sucess"
        except:
            conn.rollback()
            msg = "we can not add the user to the list"

        finally:
            conn.close()
            return render_template("feedback.html", msg=msg)


@app.route("/view")
def view():
    con = sqlite3.connect("Besk.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from Book")
    rows = cur.fetchall()
    print(rows)
    return render_template("view.html", rows=rows)


if __name__ == "__main__":
    app.run()
