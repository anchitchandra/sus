from time import time
from flask import Flask, request, jsonify, render_template


# initilize flask app 
app = Flask(__name__)




@app.route('/', methods=['GET'])
def Home():
    print(request.remote_addr, "----------------" , "visited")
    return render_template("1.html")


if __name__ == '__main__':
    app.run(port=5000, debug=True)
