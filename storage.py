#importing neccecary modules
import socket #neccecary connections
import random #randomness
import os ,errno#os wile i/o , errno deal with errors
import sys #files stuff

print("[modules imported]")

HOST = "127.0.0.1"#localhost
PORT = random.randint(1111,9999)#grnerating a random port 
print("[variables set]")
fd = open("strconfig.txt","w+")

fd.write(f"{HOST}:{PORT}")
fd.close()
    
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#creaing an instance of a socket

print("[socket created]")

s.bind((HOST,PORT))#binding to HOST PORT
print(f"[binded to {HOST} {PORT}]")

s.listen(100)#listening for a hundred connetions

while True:
    #serving-loop exit via KEYBOARD INTERUPT Ctr+c
    
    c ,addr = s.accept()#accepting incoming connections
    
    print(f"[got a connection from {addr}]")
    
    data = str(c.recv(2048).decode())#receiving data from connection 
    
    data = data.split(' ')#spliting data by " " [method] ,[data]
    
    method = data[0]# method
    
    varz = data[1]# [data]
    
    print(data)

    varz = varz.split(':')# spliting varz by ":" [username] [password]
    
    print(varz)
    
    username = varz[0]#[username]
    
    if len(varz) == 2:#print parsed data
        password = varz[1]
        print(f"len {len(password)}")
        print(f"username {username} password {password}")
    else:
        print("username {username}")

    if method == "PUT": #stuffto do when method is PUT
        fd = open(username,"w+")
        fd.write(password)
        print("[file written]")
        print("written "+password)
        print("type"+str(type(password)))
        fd.close()
        try: # handles broken-pipe errors

            s.send("ACKNEWLEDGED".encode())#sending feedback that request has been honoured
        except IOError as e :
            pass
    
    elif method == "GET":#stuff to do when method is false
        username = username.replace("\n","")
        try :
       
            fd = open(username)

            dat = fd.read()
            
        except FileNotFoundError:# catching some file io errors
            print(f"username {username} not found ",file=sys.stderr)
            
        except PermissionError:
        
            print(f"permision unauthorised {path}",file=sys.stderr)
        


        c.send(dat.encode())#send requested data
        
        fd.close()
        ss
    c.close()
