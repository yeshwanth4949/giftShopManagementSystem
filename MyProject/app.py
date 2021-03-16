from flask import Flask,render_template,url_for,redirect,request
import sqlite3

app = Flask(__name__) #creating the flask class object

@app.route("/")
def main():
  return "Welcome to My Flask Project"

@app.route("/admin")
def demo3():
  return "Hello Admin"

@app.route("/guests/<guests>")
def hello_guests(guests):
  return "Hi Welcome %s as Guest" %guests

@app.route("/user/<name>")
def hello_user(name):
  if name == 'admin':
    return redirect(url_for('admin'))
  else:
    return redirect(url_for('guests',guests=name))




#Project

@app.route("/index")
def index():
  return render_template('index.html')

@app.route("/register")
def register():
  return render_template('register.html')

@app.route("/about")
def about():
  return render_template('about.html')

@app.route("/stockmanager")
def stockmanager():
  return render_template('stockManagerLogin.html')

@app.route("/stockmanagerhome")
def stockmanagerhome():
  return render_template('stockManager_home.html')


@app.route("/shopowner")
def shopowner():
  return render_template('/shopOwnerLogin.html')

@app.route("/shopownerhome")
def shopownerhome():
  return render_template('/shopOwner_home.html')

@app.route("/customer")
def customer():
  return render_template('/customer.html')

@app.route("/customer_register")
def customer_register():
  return render_template('/customer_register.html')

@app.route("/customerhome")
def customerhome():
  return render_template('/customer_home.html')

@app.route("/adduser")
def adduser():
  return render_template('/adduser.html')

@app.route("/insertuser", methods=["POST","GET"])
def insertuser():
  db_connection = sqlite3.connect("flaskprojectdemo.db")
  if request.method=="POST":
    try:
      name=request.form["name"]
      email=request.form["email"]
      password=request.form["password"]
      location=request.form["location"]
      print(name,email,password,location)
      db_cursor = db_connection.cursor()
      db_cursor.execute("insert into registration(name,email,password,location) values(?,?,?,?)", (name,email,password,location))
      db_connection.commit()
      return render_template('display.html',message="User Added Successfully")
    except Exception as e:
      print(e)
      db_connection.rollback()
      return render_template('display.html',message="Fail to add User")

@app.route("/deleteuser")
def deleteuser():
  return render_template('/deleteuser.html')

@app.route("/deleteoperation", methods=["POST","GET"])
def deleteoperation():
  db_connection = sqlite3.connect("flaskprojectdemo.db")
  if request.method=="POST":
    try:
      id=request.form["id"]
      db_cursor = db_connection.cursor()
      i = db_cursor.execute("delete from registration where id=?",id)
      db_connection.commit()
      if(i>0):
        return "<h2>User Record Deleted</h2>"
      else:
        return "<h2>User Record Not Deleted</h2>"
    except Exception as e:
      print(e)
      db_connection.rollback()
      return "<h2>Fail to delete User</h2>"

@app.route("/viewusers")
def viewusers():
    db_connection = sqlite3.connect("flaskprojectdemo.db")
    db_connection.row_factory = sqlite3.Row
    db_cursor = db_connection.cursor()
    db_cursor.execute("select * from registration")
    rows = db_cursor.fetchall()
    return render_template("viewusers.html",rows=rows)


@app.route("/deleteuserbyid/<string:uid>")
def deleteuserbyid(uid):
  try:
    db_connection = sqlite3.connect("flaskprojectdemo.db")
    db_cursor = db_connection.cursor()
    db_cursor.execute("delete from registration where id=?",uid)
    db_connection.commit()
    return "Record Deleted"
  except Exception as e:
    return e



if __name__=='__main__':
  app.run(debug=True)