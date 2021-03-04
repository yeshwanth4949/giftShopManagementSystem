from flask import Flask,render_template,url_for,redirect

app = Flask(__name__) #creating the flask class object

@app.route("/")
def main():
  return "My First Flask Web Application"

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

@app.route("/about")
def about():
  return render_template('about.html')

@app.route("/stockmanager")
def stockmanager():
  return render_template('stockManagerLogin.html')

@app.route("/shopowner")
def shopowner():
  return render_template('/shopOwnerLogin.html')

@app.route("/customer")
def customer():
  return render_template('/customer.html')

@app.route("/customer_register")
def customer_register():
  return render_template('/customer_register.html')

if __name__=='__main__':
  app.run(debug=True)