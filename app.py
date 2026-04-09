from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    # Connect to MySQL database
    conn = mysql.connector.connect(
        host='db',
        user='root',
        password='rootpassword',
        database='flaskdb'
    )
    cursor = conn.cursor()
    cursor.execute("SELECT 'Hello from MySQL! Made with Flask and Docker!'")
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return str(result[0])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)