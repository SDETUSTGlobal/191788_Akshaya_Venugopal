from flask import Flask, render_template, request
from flask_mysqldb import MySQL
dbd = Flask(__name__)


dbd.config['MYSQL_HOST'] = 'localhost'
dbd.config['MYSQL_USER'] = 'root'
dbd.config['MYSQL_PASSWORD'] = 'root'
dbd.config['MYSQL_DB'] = 'sakila'

mysql = MySQL(dbd)


@dbd.route('/', methods=['GET', 'POST'])
def nav():
    if request.method == "POST":
        info = request.form
        a = info['ab']
        b = info['cd']
        c = info['ef']
        d = info['gh']
        e = info['ij']

        connect = mysql.connection.cursor()
        connect.execute("INSERT INTO Final(Fullname, Company , UID, Email, Password) VALUES (%s, %s, %s, %s, %s)", (a, b, c, d, e))
        mysql.connection.commit()
        connect.close()
        return render_template('welcome.html', rname=a, rcname=b, rnumber=c, remail=d, rpass=e)
    return render_template('index.html')

@dbd.route('/welcome')
def page2():
    return render_template('welcome.html')


if __name__ == '__main__':
    dbd.run()