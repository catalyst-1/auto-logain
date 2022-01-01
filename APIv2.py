
import flask
from flask import Flask
from flask import request , render_template
import socket

app = Flask(__name__,template_folder="..")

@app.route("/apiv1")
def apiv1():
    fd = open("strconfig.txt","r+")
    data = str(fd.read())
    data = data.split(":")
    host = data[0]
    port = int(data[1])
    s = socket.socket()
    
    username = str(request.args.get("username"))
    method = str(request.args.get("method"))
    s.connect((host,port))
    method = method.upper()
    if method.lower() == "put":
        password = str(request.args.get("password"))
        payload = f"{method} {username}:{password}"
        s.send(payload.encode())
        flash(s.recv(2048).decode())
        
    elif method.lower() == "get":
        payload = f"{method} {username}"
        s.send(payload.encode())
        data = s.recv(2048)
        return data
    else :
        return "FAILED"
        

    return 'SUCCESS'
    
@app.route("/ui")
def ui():
    option = request.args.get("type")
    if option == "register":
        return render_template("register.html")
    if option == "login":
        return render_template("login.html")
    else:
        return render_template("register.html")

    if __name__== "__main__":
        app.run(debug=True)
