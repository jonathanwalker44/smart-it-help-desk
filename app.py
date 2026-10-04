from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Smart IT Help Desk</h1><p>ABC Company Capstone Project</p>"

if __name__ == "__main__":
    app.run(debug=True)
