#app.py
from flask import Flask, render_template, jsonify, request
from flask_mysqldb import MySQL,MySQLdb #pip install flask-mysqldb https://github.com/alexferl/flask-mysqldb
 
app = Flask(__name__)
      
app.secret_key = "caircocoders-ednalan"
      
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Fidellio17!'
app.config['MYSQL_DB'] = 'testingdb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)
 
@app.route('/')
def main():
    return render_template('index.html')
 
@app.route("/insert",methods=["POST","GET"])
def insert():  
    cursor = mysql.connection.cursor()
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        insert = request.form['checkboxvalue'] 
        cur.execute("INSERT INTO checkbox (name) VALUES (%s)",[insert])
        mysql.connection.commit()
        cur.close() 
        msg = 'Data Inserted Successfully!'
    else:
        msg = 'Invalid'
    return jsonify(msg)
     
if __name__ == '__main__':
    app.run(debug=True)
