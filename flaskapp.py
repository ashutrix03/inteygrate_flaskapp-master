from flask import Flask
from flask import request
import os
#WA[
from whatsapp import Client
expected_token = 'The_piano_has_been_drinking'
#]WA

app = Flask(__name__)



@app.route('/')
def hello_world():

    return 'Hello World!'

@app.route('/msg', methods = ['POST'])
def msg():
    to = request.form['to']
    return str(to)

@app.route('/sendmsg',methods = ['GET'])
def sendmsg():
    to = request.args.get('to')
    msg = request.args.get('msg')
    token = request.args.get('token')
    if(str(token) == expected_token):
        client = Client(login='918763869438', password='cb1Ucch52E4J+3gfGGMuuS6xBog=')
        res = client.send_message(to, msg)  
    
    else:
        res = 'Unauthorized'
    
    return str(res)

if __name__ == '__main__':
# Bind to PORT if defined, otherwise default to 5000.Changed by Ashutosh
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
