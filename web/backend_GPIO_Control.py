
import flask
from flask import Flask, render_template, request, json, redirect, session
from flask_socketio import SocketIO
import paho.mqtt.client as mqtt
import flask_login

mqtt_broker_address="****"
mqtt_broker_port=1883
webpage_address="****"
webpage_port=5000


app = Flask(__name__)

socketio = SocketIO(app)
mqttc=mqtt.Client()
mqttc.connect(mqtt_broker_address,mqtt_broker_port,60)
mqttc.loop_start()
device_topic_on_off= 'lamps_on_off'
device_topic_dim= 'lamps_dim'
users = {'user1': {'password': 'pass1'},
         'user2' : {'password': 'pass2'}}
app.secret_key = 'Afsklj34lfASdfj3453483457'



login_manager = flask_login.LoginManager()
login_manager.init_app(app)

#
class User(flask_login.UserMixin):
      pass
#
#
@login_manager.user_loader
def user_loader(email):
     if email not in users:
       return

     user = User()
     user.id = email
     return user

@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'GET':
        return render_template('signin.html')
    if flask.request.method == 'POST':
        email = flask.request.form['email']
        if flask.request.form['password'] == users[email]['password']:
            user = User()
            user.id = email
            flask_login.login_user(user)
            return redirect('/page')


@app.route('/logout')
def logout():
     flask_login.logout_user()
     return 'Logged out'

@app.route('/')
def goto_login():
    return redirect("/login")

@app.route('/page')
@flask_login.login_required
def main():
    return render_template('control_page.html')




@socketio.on('message')
def handle_string(msg):
    print (msg)

@socketio.on('Relay_action')
def handle_json(json_msg):
     relay_state=json_msg["relay_state"]
     print(str(json_msg))
     mqttc.publish(device_topic_on_off, relay_state)

@socketio.on('PWM_action')
def handle_json(json_msg):
    print(str(json_msg))
    dim = int(json_msg["dimming_level"])
    mqttc.publish(device_topic_dim, dim)








if __name__ == '__main__':
    socketio.run(app, host=webpage_address, port=webpage_port, debug=False)
