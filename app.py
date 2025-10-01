from flask import Flask,jsonify,request

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


@app.route("/sum")
def cal_sum():
    a=int(request.args.get("a",0))
    b=int(request.args.get("b",0))
    return jsonify({"sum":a+b})


if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)