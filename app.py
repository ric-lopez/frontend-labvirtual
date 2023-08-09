# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, request
import serial, time
 
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
 
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def home():
    return render_template('index.html')

@app.route('/exp')
def experimento():
    return render_template('experimento.html')

@app.route('/young')
def young():
    return render_template('young.html')

@app.route('/fotoelectrico')
def electro():
    return render_template('fotoelectrico.html')
 
@app.route('/tensionsuper')
def tension():
    return render_template('tensionsuper.html')

@app.route('/polarizacion')
def polarizacion():
    return render_template('polarizacion.html')

@app.route('/velocidad_inst')
def velocidad_inst():
    return render_template('velocidad_inst.html')

@app.route('/campo_gravit')
def campo_gravitatorio():
    return render_template('campo_gravit.html')

@app.route('/otros')
def experimento5():
    return render_template('experimento4.html')
    
@app.route('/get_polarizacion', methods =["GET", "POST"])
def getAngulo():
    if request.method == "POST":
        rotacion = request.form.get("rotacion")
        print("Los grados son "+rotacion)
        print('Running. Press CTRL-C to exit.')
        with serial.Serial("/dev/ttyACM0", 9600, timeout=1) as arduino:
            time.sleep(0.1) #wait for serial to open
            if arduino.isOpen():
                print("{} connected!".format(arduino.port))
                try:
                    while True:
                        #cmd=input("Enter command : ")
                        arduino.write(rotacion.encode())
                        #time.sleep(0.1) #wait for arduino to answer
                        while arduino.inWaiting()==0: pass
                        if  arduino.inWaiting()>0: 
                            answer=arduino.readline()
                            print(answer)
                            arduino.flushInput() #remove data after reading
                except KeyboardInterrupt:
                    print("KeyboardInterrupt has been caught.")
        #return "Los grados son "+rotacion
        return redirect(url_for("/polarizacion"))
    return render_template("index.html")


# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
