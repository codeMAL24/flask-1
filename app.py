from flask import Flask

#app is a flask object
app = Flask(__name__)

@app.route("/")
def heloWorld():
    return "helo again" 

@app.route("/info")
def intro():
    return "okay bye"

@app.route("/lol")
def ga():
    return "why are we still here"

if(__name__ == "__main__"):
    app.run(debug=True)
    #app.run(debug=True , port = 8000)

