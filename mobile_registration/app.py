# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']
import random,json,math

from flask import Flask,render_template,request,jsonify,Request,redirect,url_for

from twilio.rest import Client

app = Flask(__name__ )

@app.route('/', methods=['GET','POST'])
def default():

    return render_template('index.html')



@app.route('/sendOTP', methods=['GET', 'POST'])
def register():
    if request.method=="POST":
        data=request.json
        mobile=data['mobile']
        otp=data['act_otp']
        if  request.method=='POST':
            is_registerd=False
            file="data.txt"
            f=open(file,"r")
            fdata=f.read()
            f.close()
            if fdata:
                x = fdata.split(",")
                for m in x:
                    if m == data['mobile']:
                        is_registerd=True
            
            if not is_registerd:
                account_sid='ACdd3be4154cfbf3751ac0417b4de41d97'
                auth_token='1669b17e03b1b333f80479f3303675df'
                client = Client(account_sid, auth_token)
                message = client.messages \
                        .create(
                             from_='+14454474429',
                             to="+91 " +mobile,
                             body="your activation code is:-"+str(otp)
                         )

        data['is_registerd']=is_registerd
        return data
   
    

@app.route('/verifyOTP', methods=['GET','POST'])
def varify_otp():
    data=request.json
    mobile=data['mobile']
    act_otp=data['act_otp']
    otp=data['otp']
    if  request.method=='POST':
        is_registerd=False
        if act_otp==otp:
            is_registerd=True
            file="data.txt"
            f=open(file,"a")
            f.write(',')
            f.write(mobile)
            f.close()

    data['is_registerd']=is_registerd
    return data


@app.route('/login', methods=['GET','POST'])
def varify_mobile():
    if request.method=="POST":
        data=request.json
        is_registerd=False
        file="data.txt"
        f=open(file,"r")
        fdata=f.read()
        f.close()
        if fdata:
            x = fdata.split(",")
            for m in x:
                if m == data['mobile']:
                    is_registerd=True
        
        data['is_registerd']=is_registerd
                
    return data
    



if __name__ == '__main__':
    app.run(debug=True)

