import os
import psycopg2
from flask import Flask

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(os.environ["DATABASE_URL"])

@app.route("/")
def home():
    return "<h1>Smart IT Help Desk</h1><p>ABC Company Capstone Project</p>"

@app.route("/test-db")
def test_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM tickets;")
    count = cur.fetchone()[0]
    cur.close()
    conn.close()

    return f"<h1>Database Connected</h1><p>Tickets in database: {count}</p>"

if __name__ == "__main__":
    app.run(debug=True)
