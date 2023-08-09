# main.py
# import the necessary packages
from flask import Flask, render_template, Response, request, send_from_directory, redirect, jsonify, url_for
#from camera import VideoCamera
import os
import io
from time import sleep
from threading import Condition
from picamera2 import Picamera2
from picamera2.encoders import JpegEncoder
from picamera2.outputs import FileOutput
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

@app.route('/')
def index():
    file_url = url_for('get_photo', filename='mi_foto.jpg')
    return render_template('index.html', file_url=file_url) #you can customze index.html here

# main.py
# import the necessary packages
from flask import Flask, render_template, Response, request, send_from_directory, redirect, jsonify, url_for
#from camera import VideoCamera
import os
import io
from time import sleep
from threading import Condition
from picamera2 import Picamera2
from picamera2.encoders import JpegEncoder
from picamera2.outputs import FileOutput
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

@app.route('/')
def index():
    file_url = url_for('get_photo', filename='mi_foto.jpg')
    return render_template('index.html', file_url=file_url) #you can customze index.html here

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
@app.route('/take_picture')
def take_picture():
	print("tomando imagen")
	sleep(1)
	date = datetime.today().strftime('%Y-%m-%d_%H:%M:%S')
	name_foto = "mi_foto-"+date+".jpg"
	request = picam2.capture_request()
	request.save("main", name_foto)
	request.release()
	print("Imagen tomada!")
	#local_path = os.path.dirname(os.path.abspath(__file__))
	print(local_path)
	os.rename(local_path+"/"+name_foto, local_path+"/static/fotos/"+name_foto)
	print("Imagen reubicada!")
	
	file_url = url_for( 'get_photo', filename=name_foto )
	print(file_url)
	return render_template('index.html', file_url=file_url)
	

@app.route('/test', methods =['GET'])
def test():
   return jsonify({"Result": "Welcome to GeeksForGeeks"})

@app.route('/polarizacion')
def polarizacion():
    return render_template('polarizacion.html')


if __name__ == '__main__':
	picam2 = Picamera2()
	picam2.configure(picam2.create_video_configuration(main={"size": (640, 480)}))
	#picam2.configure(picam2.create_video_configuration(main={"size": (1920, 1080)},
	# lores={"size": (640, 480)}, display="lores"))
	output = StreamingOutput()
	picam2.start_recording(JpegEncoder(), FileOutput(output))
	try:
		app.run(host='0.0.0.0', debug=False)
	finally:
		picam2.stop_recording()


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
@app.route('/take_picture')
def take_picture():
	print("tomando imagen")
	sleep(1)
	date = datetime.today().strftime('%Y-%m-%d_%H:%M:%S')
	name_foto = "mi_foto-"+date+".jpg"
	request = picam2.capture_request()
	request.save("main", name_foto)
	request.release()
	print("Imagen tomada!")
	#local_path = os.path.dirname(os.path.abspath(__file__))
	print(local_path)
	os.rename(local_path+"/"+name_foto, local_path+"/static/fotos/"+name_foto)
	print("Imagen reubicada!")
	
	file_url = url_for( 'get_photo', filename=name_foto )
	print(file_url)
	return render_template('index.html', file_url=file_url)
	

@app.route('/test', methods =['GET'])
def test():
   return jsonify({"Result": "Welcome to GeeksForGeeks"})



if __name__ == '__main__':
	picam2 = Picamera2()
	picam2.configure(picam2.create_video_configuration(main={"size": (640, 480)}))
	#picam2.configure(picam2.create_video_configuration(main={"size": (1920, 1080)},
	# lores={"size": (640, 480)}, display="lores"))
	output = StreamingOutput()
	picam2.start_recording(JpegEncoder(), FileOutput(output))
	try:
		app.run(host='0.0.0.0', debug=False)
	finally:
		picam2.stop_recording()
