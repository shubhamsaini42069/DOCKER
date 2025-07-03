from flask import Flask, render_template, request, jsonify
from data import getdata
app=Flask(__name__)

@app.route("/")
def h():
    return "home page"
@app.route("/api",methods=["GET"])
def go():
    data = getdata()        
    data = {"data": data}  
    return jsonify(data)
if __name__=="__main__":
    app.run(port="8000",host='0.0.0.0',debug=True)
