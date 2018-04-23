from flask import Flask,jsonify,session,render_template,make_response
from flask_restful import Resource, Api,reqparse
from passlib.hash import sha256_crypt
import dc_classifer as dc
import os

app = Flask(__name__)
app.secret_key=os.urandom(24)
@app.before_first_request
def before_req():
    dc.intialize()
    
api = Api(app)


hash1 = sha256_crypt.using(rounds=40000).hash("Shankar123@");
hash2 = sha256_crypt.using(rounds=40000).hash("HeavyWater123@");
class HelloWorld(Resource):
    def get(self):
        headers={'Content-Type':'text/html'}
        return make_response(render_template('index.html'),200,headers)

parser = reqparse.RequestParser()
parser.add_argument('inp_str')
parser.add_argument('passw')
parser.add_argument('userName')

class testPost(Resource):
    def post(self):
        if 'user' in session:
            
            if(session['user']=='shankar' or session['user']=='heavywater'):
                args = parser.parse_args()
                inputJso=args['inp_str']
                pred=dc.predictionResult(inputJso)
                return {'output':'success','out':pred},201

            else:
                return {'output':'unauthorized'},404

        else:
            return {'output':'unauthorized'},404
        
        
class testGet(Resource):
    def get(self,inp):
        args = inp
        if 'user' in session:
            
            if(session['user']=='shankar' or session['user']=='heavywater'):
                processed=args.replace('%20', ' ')
                pred=dc.predictionResult(processed)
                
                return {'output':'success','out':pred},201

            else:
                return {'output':'unauthorized'},404

        else:
            return {'output':'unauthorized'},404
class verifyUser(Resource):
    def post(self):
        args=parser.parse_args()
        passw=args['passw']
        user=args['userName']
        if ((sha256_crypt.verify(passw, hash1) and user=='shankar') or (sha256_crypt.verify(passw, hash2) and user=='heavywater'))==True:
            session['user']=user
            return True,201
        else:
            return False,201


class getSession(Resource):
    def get(self):
        if 'user' in session:
            
            if(session['user']=='shankar' or session['user']=='heavywater'):
                return {'output':'success','session_user':session['user']},201

            else:
                return {'output':'unauthorized'},201

        else:
            return {'output':'unauthorized'},201
        
api.add_resource(HelloWorld, '/')
api.add_resource(testPost, '/test')
api.add_resource(testGet, '/testGet/<string:inp>')
api.add_resource(verifyUser, '/userAuth')
api.add_resource(getSession, '/getSession')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)
