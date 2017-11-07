# Flask Web App
A flask web app for controlling lamps from the [ESP8266](https://github.com/Landflier/ESP8266-Lamp-Controller) project. 

## Deployment
### Connection

To deploy locally, please edit the following variables in the backend_GPIO_Control.py script :<br />
webpage_address -> the address on which your webpage will be served <br />
webpage_port -> the port on which the webpage will be served, default set to 5000<br />
mqtt_broker_address -> The address, where the mqtt-broker is running<br />
mqtt_broker_port -> The port on which mqtt-broker is running, usually 1883<br />

### Using
#### Frontend Interface
When done with the setup, run the backend_GPIO_Control.py script and open in a browser the webpage_address:webpage_port address
set in the connection setup. <br />
A login screen should appear. Currently users are set in the python script in the users array. <br />
The default logins are user1:pass1 and user2:pass2 <br />

The templates for the current webpages are located withing the templates directory. It is addvised to add webpages <br />
to that directory only, since the python render_template package will look for html files there. <br />

#### Backend Communication

Backend and frontend communication is done through the SocketIO framework. The buttons in the current version send messages 
to two "topics": 'Relay_action' and 'PWM_action'. Their respective messages are handled by the python backend script in the @socketio.on() functions <br />


For the mqtt communication with ESP8266 devices, the topic is set in the device_topic variable. <br />
Currently messages are sent to a default group "A". To set up the ESP8266 devices, just send a message on the "lamps_set" topic <br />
and refer to the README on the [ESP8266](https://github.com/Landflier/ESP8266-Lamp-Controller) project page. <br />
 




## Built With
* [Flask](http://flask.pocoo.org/) - Main framework for the whole app.
* [SocketIO](https://socket.io/) - The SocketIO framework. Additional link to the [flask-socketio](https://flask-socketio.readthedocs.io/en/latest/) documentation 
* [Flask-Login](https://flask-login.readthedocs.io/en/latest/) - package for user management.
* [Paho-MQTT](https://pypi.python.org/pypi/paho-mqtt/1.1)- MQTT protocol communication for python.
* [Bootstrap](http://getbootstrap.com/) - Library for developing the frontend interface.


## Authors

Vasil Yordanov<br />
For further information contact vasil.r.yordanov@gmail.com

## License

This project is licensed under the GPLv3 License - see the [GPLv3](https://www.gnu.org/licenses/quick-guide-gplv3.en.html) site for details.
