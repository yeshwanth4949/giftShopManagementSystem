from flask import Flask,redirect,url_for,render_template,request,session
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'flaskdemo'

mysql = MySQL(app)

app.secret_key = "flask123"

@app.route("/index")
def index():
  return render_template('index.html')

@app.route("/register")
def register():
  return render_template('register.html')

@app.route("/about")
def about():
  return render_template('about.html')

@app.route("/requestforstock")
def requestforstock():
  return render_template('requestforstock.html')


@app.route("/stockmanager")
def stockmanager():
  return render_template('stockManagerLogin.html')

@app.route("/stockmanagerhome")
def stockmanagerhome():
  return render_template('stockManager_home.html')

@app.route("/stockmanagerupdate")
def stockmanagerupdate():
  return render_template('stockManager_update.html')

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

@app.route("/shopownerupdate")
def shopownerupdate():
  return render_template('/shopOwner_update.html')


@app.route("/customerupdate")
def customerupdate():
  return render_template('/customer_update.html')

@app.route("/stockmanagerupdate")
def shopmanagerupdate():
  return render_template('/stockManager_update.html')

@app.route("/adduser")
def adduser():
  return render_template('/adduser.html')

@app.route("/addstock")
def addstock():
  return render_template('/addstock.html')

@app.route("/deleteuser")
def deleteuser():
  return render_template('/deleteuser.html')

@app.route("/page2")
def page2():
  
  if "uname" in session:
    return session["uname"]
  else:
    return "Session Expired"








@app.route("/insertusers",methods=["POST","GET"])
def insertusers():
  if request.method=="POST":
    try:
      name=request.form["name"]
      gender=request.form["gender"]
      email=request.form["email"]
      uname=request.form["uname"]
      pwd=request.form["pwd"]
      mobile=request.form["mobile"]
      loc=request.form["loc"]
      print(name,gender,email,uname,pwd,mobile,loc)
      db_cursor = mysql.connection.cursor()
      db_cursor.execute("INSERT INTO register(name,gender,email,uname,pwd,mobile,loc) VALUES (%s,%s,%s,%s,%s,%s,%s)", [name,gender,email,uname,pwd,mobile,loc])
      mysql.connection.commit()
      #msg="User Added Successfully"
      return render_template("display.html",message="User Added Successfully")#message = param name and msg = param value
    except Exception as e:
      print(e)
      #msg="Fail to Add User Record"
      return render_template("display.html",message="Fail to Add User Record")#message = param name and msg = param value

@app.route("/checkusers",methods=["POST","GET"])
def checkusers():
  if request.method=="POST":
    try:
      uname=request.form["uname"]
      pwd=request.form["pwd"]
      print(uname,pwd)
      db_cursor = mysql.connection.cursor()
      db_cursor.execute("select * from register where uname=%s and pwd=%s ", [uname,pwd])
      n=db_cursor.fetchall()
      if(len(n)>0):
        return render_template("customer_home.html",message="Login Successfully")
      else:
        return render_template("customer.html",message="Fail to login")
    except Exception as e:
      #msg="Fail to Add User Record"
      return render_template("customer.html",message="Fail to login")

@app.route("/checkusersso",methods=["POST","GET"])
def checkusersso():
  if request.method=="POST":
    try:
      uname=request.form["uname"]
      pwd=request.form["pwd"]
      print(uname,pwd)
      db_cursor = mysql.connection.cursor()
      db_cursor.execute("select * from register_so where uname=%s and pwd=%s ", [uname,pwd])
      n=db_cursor.fetchall()
      if(len(n)>0):
        return render_template("shopOwner_home.html",message="Login Successfully")
      else:
        return render_template("shopOwnerLogin.html",message="Fail to login")
    except Exception as e:
      return render_template("customer.html",message="Fail to login")

@app.route("/checkusers_sm",methods=["POST","GET"])
def checkusers_sm():
  if request.method=="POST":
    try:
      uname=request.form["uname"]
      pwd=request.form["pwd"]
      db_cursor = mysql.connection.cursor()
      db_cursor.execute("select * from register_sm where uname=%s and pwd=%s ", [uname,pwd])
      n=db_cursor.fetchall()
      if(len(n)>0):
        return render_template("stockManager_home.html",message="Login Successfully")
    except Exception as e:
      return "Invalid Login"

@app.route("/insertstock",methods=["POST","GET"])
def insertstock():
  if request.method=="POST":
    try:
      gift_category=request.form["gift_category"]
      gift_name=request.form["gift_name"]
      gift_desc=request.form["gift_desc"]
      cost=request.form["cost"]
      quantity=request.form["quantity"]
      print(gift_category,gift_name,gift_desc,cost,quantity)
      db_cursor = mysql.connection.cursor()
      db_cursor.execute("INSERT INTO stocks(gift_category,gift_name,gift_desc,cost,quantity) VALUES (%s,%s,%s,%s,%s)", [gift_category,gift_name,gift_desc,cost,quantity])
      mysql.connection.commit()
      #msg="User Added Successfully"
      return render_template("display.html",message="User Added Successfully")#message = param name and msg = param value
    except Exception as e:
      print(e)
      #msg="Fail to Add User Record"
      return render_template("display.html",message="Fail to Add User Record")#message = param name and msg = param value



@app.route("/requeststock",methods=["POST","GET"])
def requeststock():
  if request.method=="POST":
    try:
      gift_category=request.form["gift_category"]
      gift_name=request.form["gift_name"]
      gift_desc=request.form["gift_desc"]
      cost=request.form["cost"]
      quantity=request.form["quantity"]
      status="not_accepted"
      print(gift_category,gift_name,gift_desc,cost,quantity,status)
      db_cursor = mysql.connection.cursor()
      db_cursor.execute("INSERT INTO stocks(gift_category,gift_name,gift_desc,cost,quantity,status) VALUES (%s,%s,%s,%s,%s,%s)", [gift_category,gift_name,gift_desc,cost,quantity,status])
      mysql.connection.commit()
      #msg="User Added Successfully"
      return render_template("display.html",message="User Added Successfully")#message = param name and msg = param value
    except Exception as e:
      print(e)
      #msg="Fail to Add User Record"
      return render_template("display.html",message="Fail to Add User Record")#message = param name and msg = param value




@app.route("/viewstocks")
def viewstocks():
    db_cursor = mysql.connection.cursor()
    db_cursor.execute("select * from stocks where status='accepted'")
    rows = db_cursor.fetchall()
    return render_template("viewstocks.html",rows=rows)

@app.route("/viewrequests")
def viewrequests():
  db_cursor = mysql.connection.cursor()
  db_cursor.execute("select * from stocks where status='not_accepted'")
  rows = db_cursor.fetchall()
  return render_template("viewrequests.html",rows=rows)



@app.route("/updateuser",methods=["POST","GET"])
def updateuser():
  if request.method=="POST":
    try:
      uname=request.form["uname"]
      pwd=request.form["pwd"]
      db_cursor = mysql.connection.cursor()
      n=db_cursor.execute("update register set pwd=%s where uname=%s", [pwd,uname])
      mysql.connection.commit()
      if(n>0):
        return render_template("display.html",message="Update Successfully")
      else:
        return render_template("display.html",message="Fail to Update")
    except Exception as e:
      print(e)
      return e

@app.route("/updateuser1",methods=["POST","GET"])
def updateuser1():
  if request.method=="POST":
    try:
      uname=request.form["uname"]
      pwd=request.form["pwd"]
      db_cursor = mysql.connection.cursor()
      n=db_cursor.execute("update register_so set pwd=%s where uname=%s", [pwd,uname])
      mysql.connection.commit()
      if(n>0):
        return render_template("display.html",message="Update Successfully")
      else:
        return render_template("display.html",message="Fail to Update")
    except Exception as e:
      print(e)
      return e


@app.route("/updateuser2",methods=["POST","GET"])
def updateuser2():
  if request.method=="POST":
    try:
      uname=request.form["uname"]
      pwd=request.form["pwd"]
      db_cursor = mysql.connection.cursor()
      n=db_cursor.execute("update register_sm set pwd=%s where uname=%s", [pwd,uname])
      mysql.connection.commit()
      if(n>0):
        return render_template("display.html",message="Update Successfully")
      else:
        return render_template("display.html",message="Fail to Update")
    except Exception as e:
      print(e)
      return e

@app.route("/updatereq/<string:sid>")
def updatereq(sid):
  try:
    db_cursor = mysql.connection.cursor()
    db_cursor.execute("update stocks set status=%s where id=%s", ["accepted",sid])
    mysql.connection.commit()
    return "Stock Added Successfully"
  except Exception as e:
      return e


if __name__ == '__main__':
  app.run(debug=True)