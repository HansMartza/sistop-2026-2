Hans Martinez Sanchez

PROBLEMA DE SINCRONIZACIÓN: SANTA CLAUS

Lenguaje utilizado:
Python 

Descripción del problema:
El problema de Santa Claus es un clásico de sincronización donde intervienen tres tipos de procesos: Santa Claus, los elfos y los renos. Santa duerme hasta que es despertado por los renos o por un grupo de elfos. Los renos tienen prioridad cuando los 9 han regresado de vacaciones, mientras que los elfos solo pueden despertar a Santa en grupos de 3 cuando tienen problemas.

Estrategia de sincronización:
Para resolver el problema se utilizaron semáforos y mutex. El semáforo santaSem se usa para despertar a Santa. Los semáforos elfSem y reindeerSem controlan la sincronización entre Santa y los elfos o renos respectivamente. El semáforo elfTex limita a que solo 3 elfos puedan acceder simultáneamente a Santa. Se utiliza un mutex para proteger las variables compartidas elfCount y reindeerCount y evitar condiciones de carrera.

Funcionamiento:
Santa permanece dormido hasta que es despertado. Si los 9 renos llegan, Santa los atiende con prioridad y prepara el trineo. Si hay 3 elfos, Santa los ayuda. El programa utiliza múltiples hilos que simulan el comportamiento concurrente de los actores.

Instrucciones de ejecución:
Todo esto se realiza en la terminal ubuntu
1. Abrir la terminal en la carpeta del proyecto.
2. Ejecutar el comando:
   python3 santa.py

Refinamientos:
Se implementó prioridad para los renos sobre los elfos, tal como lo establece el problema clásico. Además, se controló el acceso de los elfos en grupos de tres mediante semáforos, evitando problemas de sincronización y condiciones de carrera.


