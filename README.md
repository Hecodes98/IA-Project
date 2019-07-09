**PLN: Procesamiento del lenguaje natural**

**1. Descripción**
   -Proyecto realizado para la materia de Inteligencia Artificial en la Universidad Tecnológica de Pereira
   con el fin de mediante del procesamiento del lenguaje natural, un asistente virtual responda tus preguntas acerca de la geografía básica de Colombia: Capitales, regiones, superficie, gentilicio o demás informacion sobre los departamentos de Colombia.
   
**2. Librerías utilizadas/requeridas**
   -Solicitaremos de las siguientes librerías para llevar a cabo correctamente la revisión del código:
   -speech_recognition: Biblioteca para realizar el reconocimiento de voz, con soporte para varios motores y API, online y offline.
   
   -spaCy: Una biblioteca de software de código abierto para el procesamiento avanzado de lenguaje natural, escrita en los lenguajes de programación Python y Cython.
   
   -pymongo: PyMongo es una distribución de Python que contiene herramientas para trabajar con MongoDB y es la forma recomendada de trabajar con MongoDB desde Python. Esta documentación intenta explicar todo lo que necesita saber para usar PyMongo.
   
   -MongoDb

   Todas estas librerías se pueden instalar con un simple pip install [NAME]

**3. Instalación**
   -En el programa también se encuentra adjunto un archivo llamado db.json, el cual contiene toda la informacion de los departamentos de Colombia que se usaron para este software, con este archivo podrás añadir esta información en tu cluster de Atlas, después de crear tu db desde tu shell de Mongo.
   Cuando estes parado en tu nueva db, solo deberias escribir el siguiente comando:
   db.[nombre_coleccion].insertMany("Aqui pegas toda la informacion de db.json").
