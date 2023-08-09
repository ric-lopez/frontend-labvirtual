# main.py
# import the necessary packages
from flask import Flask, render_template, Response, request, send_from_directory, redirect, jsonify, url_for
#from camera import VideoCamera
import os
import io
from time import sleep
from threading import Condition
# from picamera2 import Picamera2
# from picamera2.encoders import JpegEncoder
# from picamera2.outputs import FileOutput
# import serial, time
import socket
from udp_conect import send_msg, experimentos;


#from flask_uploads import UploadSet, IMAGES, configure_uploads
from datetime import datetime

class StreamingOutput(io.BufferedIOBase):
    def __init__(self):
        self.frame = None
        self.condition = Condition()

    def write(self, buf):
        with self.condition:
            self.frame = buf
            self.condition.notify_all()

#pi_camera = VideoCamera(flip=False) # flip pi camera if upside down.


# App Globals (do not edit)
app = Flask(__name__)
app.config['SECRET_KEY']='elotito'
app.config['UPLOADED_PHOTOS_DEST']='/static/fotos'
local_path = os.path.dirname(os.path.abspath(__file__))

#photos = UploadSet('photos', IMAGES)
#configure_uploads(app, photos)

# ~ @app.route('/')
# ~ def index():
    # ~ file_url = url_for('get_photo', filename='mi_foto.jpg')
    # ~ return render_template('index.html', file_url=file_url) #you can customze index.html here

def gen():
	#get camera frame
	while True:
		#frame = camera.get_frame()
		with output.condition:
			output.condition.wait()
			frame = output.frame
			yield (b'--frame\r\n'
			b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')               
	        

@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/fotos/<filename>')
def get_photo(filename):
	print(app.config['UPLOADED_PHOTOS_DEST'], filename)
	#return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], filename)
	return send_from_directory(local_path+app.config['UPLOADED_PHOTOS_DEST'], filename)

# Take a photo when pressing camera button
@app.route('/take_picture', methods=['POST', 'GET'])
def take_picture():
    if request.method == "POST":
        print(request.json)
        print("tomando imagen")
        sleep(1)
        date = datetime.today().strftime('%Y-%m-%d_%H:%M:%S')
        name_foto = "mi_foto-"+date+".jpg"
        req_camera = picam2.capture_request()
        req_camera.save("main", name_foto)
        req_camera.release()
        print("Imagen tomada!")
        #local_path = os.path.dirname(os.path.abspath(__file__))
        print(local_path)
        os.rename(local_path+"/"+name_foto, local_path+"/static/fotos/"+name_foto)
        print("Imagen reubicada!")

        file_url = url_for( 'get_photo', filename=name_foto )
        print(file_url)
        return send_from_directory(directory=local_path+"/static/fotos/", filename=name_foto, as_attachment=True)
        #return redirect(url_for("polarizacion"))
    return render_template("polarizacion.html")
	
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

@app.route('/inst_campo_gravit', methods =["GET", "POST"])
def inst_campo():
    if request.method == "POST":
        print(request.json)
        inst = request.json['instruccion']
        print('Running. Press CTRL-C to exit.')
        send_msg(inst)
        # if send_msg(inst) :
        #     print("exito")
        #     return redirect(url_for("campo_gravit"))
        # else:
        #     print("fallo")
        #     return redirect(url_for("campo_gravit"))
    return render_template("campo_gravit.html")

@app.route('/inst_polarizacion', methods =["GET", "POST"])
def inst_polarizacion():
    if request.method == "POST":
        if(request.form):
            rotacion = request.form.get("rotacion")
            rotacion = '01MG '+rotacion
            print("Los grados son "+rotacion)
            print('Running. Press CTRL-C to exit.')
            send_msg(rotacion)    
        elif(request.json):
            print(request.json)
            inst = request.json['instruccion']
            print('Running. Press CTRL-C to exit.')
            send_msg(inst)
            # if send_msg(inst) :
            #     print("exito")
            #     return redirect(url_for("campo_gravit"))
            # else:
            #     print("fallo")
            #     return redirect(url_for("campo_gravit"))
    return render_template("polarizacion.html")

@app.route('/inst_young', methods =["GET", "POST"])
def inst_young():
    if request.method == "POST":
        if(request.form):
            print(request.form)
            if(request.form.get("rotacion")):
                rotacion = request.form.get("rotacion")
                rotacion = '01MG '+rotacion
                print("Los grados son "+rotacion)
                print('Running. Press CTRL-C to exit.')
                send_msg(experimentos["young"], rotacion)     
            elif(request.form.get("desp_principal")):
                d_principal = request.form.get("desp_principal")
                d_principal = '01MX '+d_principal
                print("El desplazamiento es "+d_principal)
                print('Running. Press CTRL-C to exit.')
                #name_exp = request.form.get("id_experimento")
                send_msg(experimentos["young"], d_principal)
            elif(request.form.get("desp_secundario")):
                d_secundaria = request.form.get("desp_secundario")
                d_secundaria = '01MY '+d_secundaria
                print("Los grados son "+d_secundaria)
                print('Running. Press CTRL-C to exit.')
                send_msg(experimentos["young"], d_secundaria)
            else:
                 print("algo salio mal :(")
        elif(request.json):
            print(request.json)
            inst = request.json['instruccion']
            id = request.json['id_exp']
            print('Running. Press CTRL-C to exit.')
            send_msg(id, inst)
            # if send_msg(inst) :
            #     print("exito")
            #     return redirect(url_for("campo_gravit"))
            # else:
            #     print("fallo")
            #     return redirect(url_for("campo_gravit"))
    return render_template("young.html")

@app.route('/inst_tension', methods =["GET", "POST"])
def inst_tension():
    if request.method == "POST":
        if request.json:
            print("HOLA MUNDO")
            print(request.json)
            inst = request.json['instruccion']
            id = request.json['id_exp']
            print('Running. Press CTRL-C to exit.')
            send_msg(id, inst)
    return render_template("tensionsuper.html")


@app.route('/test', methods =['GET'])
def test():
   return jsonify({"Result": "Welcome to GeeksForGeeks"})



if __name__ == '__main__':
	#picam2 = Picamera2()
	#picam2.configure(picam2.create_video_configuration(main={"size": (640, 480)}))	
    #output = StreamingOutput()
	#picam2.start_recording(JpegEncoder(), FileOutput(output))
	#try:
	app.run(host='0.0.0.0', debug=False)
	#finally:
	#	picam2.stop_recording()

