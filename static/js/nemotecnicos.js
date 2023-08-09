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
export const campo_gravitatorio = '01';
export const polarizacion = '02';
export const young = '03';
export const velocidad_instantanea = '04';
export const fotoelectrico = '05';
export const tension_superficial = '06';

export const MG = 'MG'; //Motor de giro, necesita un valor de tecnico angulo
export const MX = 'MX'; //Movimiento en el eje x, necesita un valor de distancia
export const MY = 'MY'; //Movimiento en el eje y, necesita un valor de distancia

export const MV = 'MV'; //Inicia el movimiento del electroiman
export const LB = 'LB'; //Libera la esfera

