// import './nemotecnicos';

/****************************************************************************************************************
   Comandos Experimento de Optica:

   MN | Comando(com)| Argumento(ar)| Ejemplo    | Return                          | Mensaje de error
      |             |              |            |                                 |
   MG | Mov de giro | int          | MG -4      | Posición                        | Error: comando no válido. (MG)
   MX | Mov en  X   | int          | MX -3      | Posición                        | Error: comando no válido. (MX)
   MY | Mov en  Y   | int          | MY -5      | Posición                        | Error: comando no válido. (MY)
   ST | Imprime Pos | char         | ST         | OK                              | N/A
   AB | Abort       | char         | AB         | STOP                            | N/A
   AA | MY delante  | char         | AA         | Posición                        | N/A
   CC | MY detras   | char         | CC         | Posición                        | N/A
   DD | MX delante  | char         | DD         | Posición                        | N/A
   EE | MX detras   | char         | EE         | Posición                        | N/A
   FF | MG derecha  | char         | FF         | ---                             | N/A
   HH | MG izquierda| char         | HH         | ---                             | N/A

   Sin espacios antes del mnenónico (MN)
   Un espacio entre el nemónico y el argumento
   No se tiene que poner espacio con los MN de los LED
   All <POS> arguments are signed long (32 bits)

   Cualquier otro mnemónico marcará error        Error entrada no válida
*****************************************************************************************************************/
const campo_gravitatorio = '01';
const polarizacion = '02';
const young = '03';
const velocidad_instantanea = '04';
const fotoelectrico = '05';
const tension_superficial = '06';

const MG = 'MG'; //Motor de giro, necesita un valor de tecnico angulo
const MX = 'MX'; //Movimiento en el eje x, necesita un valor de distancia
const MY = 'MY'; //Movimiento en el eje y, necesita un valor de distancia

const MV = 'MV'; //Inicia el movimiento del electroiman
const LB = 'LB'; //Libera la esfera


function takePicture(){
	fetch('/take_picture', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
		},
		body: JSON.stringify({picture: 'take'})
	})
	.then(response => {
		//console.log('then response');
		//let link = document.createElement('a');
		//link.innerHTML('descarga');
		//let divLinks = document.getElementByID("links_pictures");
		//divLinks.appendChild(link);
		//console.log('no descarga nada :(')
		response.text()
        })
	.then(result => {
		console.log('then result');
		console.log(result);
	})
	.catch(error => {
		console.error('Error', error);
	})
}

function sendAngulo(){
	//console.log(angulo);
	let angulo = document.getElementById('angulo');
	angulo = 'MG '+angulo;
	console.log(angulo);
	fetch('/get_polarizacion', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
		},
		body: JSON.stringify({angulo: angulo}),
	})
	.then(response => response.text())
	.then(result => {
		console.log(result);
	})
	.catch(error => {
		console.error('Error', error);
	});
}

function sendInstCampoGravit(id_exp, instruccion){
	console.log(id_exp, instruccion);
	let instruccionSend = id_exp+instruccion;
	console.log(instruccionSend);
	fetch('/inst_campo_gravit', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
		},
		body: JSON.stringify({instruccion: instruccionSend}),
	})
	.then(response => response.text())
	.then(result => {
		console.log(result);
	})
	.catch(error => {
		console.error('Error:', error);
	});
}

function sendInstPolarizacion(id_exp, instruccion, value){
	console.log(id_exp, instruccion, value);
	let instruccionSend = null;
	if(instruccion !== 'MG' && value === null){
		instruccionSend = id_exp+instruccion;	
	}else{
		instruccionSend = id_exp+instruccion+' '+value;
	}
	console.log(instruccionSend);
	fetch('/inst_campo_gravit', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
		},
		body: JSON.stringify({instruccion: instruccionSend}),
	})
	.then(response => response.text())
	.then(result => {
		console.log(result);
	})
	.catch(error => {
		console.error('Error:', error);
	});
}

function sendInstYoung(id_exp, instruccion){
	console.log(id_exp, instruccion);
	let motores = ['MG', 'MX', 'MY'];
	let recorridos = ['AA', 'CC', 'DD','EE', 'FF', 'HH']
	let instruccionSend = null;
	if(recorridos.includes(instruccion)){
		instruccionSend = id_exp+instruccion;	
	}else{
		instruccionSend = id_exp+instruccion+' ';
	}
	console.log(instruccionSend);
	fetch('/inst_young', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
		},
		body: JSON.stringify({id_exp: id_exp, instruccion: instruccionSend}),
	})
	.then(response => response.text())
	.then(result => {
		console.log(result);
	})
	.catch(error => {
		console.error('Error:', error);
	});
}

function sendInstTensionSup(id_exp, instruccion, value){
	console.log(id_exp, instruccion, value);
	//let  = ['MG', 'LA', 'LF'];
	// let instruccionSend = null;
	// if(!motores.includes(instruccion) && value === null){
	// 	instruccionSend = id_exp+instruccion;	
	// }else{
	// 	instruccionSend = id_exp+instruccion+' '+value;
	// }
	console.log(instruccion);
	fetch('/inst_tension', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
		},
		body: JSON.stringify({id_exp: id_exp, instruccion: instruccion}),
	})
	.then(response => response.text())
	.then(result => {
		console.log(result);
	})
	.catch(error => {
		console.error('Error:', error);
	});
}