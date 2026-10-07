import os
import psycopg2
from flask import Flask, render_template, request

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(os.environ["DATABASE_URL"])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit-ticket", methods=["POST"])
def submit_ticket():
    requester_name = request.form["requester_name"]
    requester_email = request.form["requester_email"]
    issue_description = request.form["issue_description"]

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO tickets (requester_name, requester_email, issue_description)
        VALUES (%s, %s, %s)
        """,
        (requester_name, requester_email, issue_description)
    )

    conn.commit()
    cur.close()
    conn.close()

    return "<h2>Ticket submitted successfully!</h2><a href='/'>Submit another ticket</a>"

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/dashboard")
def dashboard():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT id, requester_name, requester_email, issue_description,
               category, priority, status, assigned_to,
               resolution_notes, created_at
        FROM tickets
        ORDER BY created_at DESC
    """)

    tickets = cur.fetchall()

    cur.close()
    conn.close()

    return render_template("dashboard.html", tickets=tickets)
