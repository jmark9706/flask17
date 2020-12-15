# target web server for Arduino and ESP8266 devices

from flask import Flask
from flask import request, escape
import time

app = Flask(__name__)

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return ('key not found')
    return render_template('login.html', error=error)
    
@app.route('/parms')
def hello():
# init to legal defaults
    humidity = " NR "
    device = " NR "
    alt = " NR "
    temp = " NR "
    baro = " NR "
    humidity = request.args.get("humidity")
    device = request.args.get("device")
    alt = request.args.get("alt")
    temp = request.args.get("temp")
    baro = request.args.get("baro")
    device = request.args.get("device")
    # convert millibars to float
    mb_flt = float(baro) / 100
    # convert to inches of hg
    hg_flt =  0.0295301 * mb_flt
    seconds = time.time()
    local_time = time.ctime(seconds)
    fs=open("obs.txt", "w")
    fs.write("<h1>"+local_time +" device  "+ device +" temperature "+ temp +" humidity "+ humidity +" pressure mb " + str (mb_flt) + " pressure in. hg. " + str(hg_flt) + " altitude " + alt +"</H1>\n")
    fs.close()
    return '''<h1>The temperature is: {}</h1>
              <h1>The humidity is: {}</h1>
               <h1>The barometric pressure is: {}</h1>'''.format(temp, humidity, baro)

@app.route('/')
def hello_world2():
    fsi = open("obs.txt", "r")
    dat = fsi.read()
    return dat
    
@app.route('/bob')
def hello_world():
    return 'Hello, Bob!'

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="80")
    