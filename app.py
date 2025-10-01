from flask import Flask,jsonify

app=Flask(__name__)


@app.route("/")
def index():
    return "Hello World !"


@app.route("/health")
def health():
    return jsonify({"status":"ok"})

@app.route("/echo/<msg>")
def echo(msg):
    return jsonify({"echo":msg})

if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)