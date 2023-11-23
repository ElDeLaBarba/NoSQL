# NoSQL

Proyecto final para la materia Base de datos NoSQL de la carrera Tecnólogo en Informática, hecho en Python y MongoDB.

## Tecnologías elegidas:

Elegimos MongoDB debido a que creemos que, de las opciones que tenemos disponibles, es la más accesible y a la que mayor potencial podemos exprimirle de cara a futuro. Utilizamos MongoDB Compass como interfaz gráfica y MongoDB Atlas para almacenar datos en la nube.

Python, por su lado, es una tecnología accesible y con una gran compatibilidad con MongoDB, por lo que fue la opción más adecuada para esta tarea. Utilizamos pymongo para conectar ambas de manera sencilla.

## El modelo de datos
+ Dada la elección de tecnologías, el tipo de base de datos que se debió sugerir es de tipo Documental conforme al comportamiento y funcionamiento de MongoDB.
+ La base cuenta con dos tablas principales, Personas y Domicilios, cuya disposición será la siguiente:
    Personas: { CI*, nombre, apellido, edad }
    Domicilio: { Persona, { Departamento, Localidad, Calle, Nro, Apartamento, Padrón, Ruta, Km, Letra, Barrio } }

## Descarga, inicialización y uso del proyecto:


### Requisitos previos:

+ Python 3.11
+ MongoDB Compass
+ Postman
+ VS Code
+ Jenkins

### Inicialización: 

Para comenzar con la instalación, será necesario tener este repo descargado en su sistema local. Desde el CMD de Windows/Linux, se ejecuta el siguiente comando: 

> pip install pymongo

De esta manera, se instalará pymongo (librería necesaria para inicializar el proyecto). Luego, será necesario que instale la extensión de Python en VS Code. Ahora ya es posible ejecutar el proyecto y añadir, ver y filtrar datos en la BD. 

### Configuración de MongoDB Compass:

Para ver los cambios en la BD en tiempo real, será necesario acceder a ésta utilizando MongoDB Compass. Para ello, luego de tener el programa instalado, se deberá crear una conexión utilizando el siguiente URI: 

> mongodb+srv://GuestUser:SoyUnaPass12345678@cluster0.o1jktdl.mongodb.net/

De esta manera, se iniciará sesión con un usuario genérico, permitiendo ver los datos. 

### Configuración de Postman: 

Luego de inicializar el proyecto, y habiendo instalado y configurado el programa previamente especificado con su cuenta de usuario, se deberá acceder al siguiente link: 

> https://www.postman.com/cloudy-meteor-237196/workspace/nosql-postmanaccess 

Y forkear las colecciones llamadas 'MongoDB Data API' y 'MongoDB Data API for Domicilios'. Ahora, podrá hacer requests de prueba directamente a la BD desde Postman. La primera colección permite trabajar con Personas, y la segunda con Domicilios. Ambas generan datos aleatorios. 

### Utilizando Jenkins: 

Luego de instalar y settear el programa siguiendo esta guía: 

> https://www.jenkins.io/doc/book/installing/windows/

Y habiendo iniciado sesión en el programa, deberá crear una nueva tarea del tipo pipeline, con un nombre a elección. Luego, en la configuración de la tarea, deberá marcar la opción 'GitHub Project' y pegar la URL de este repositorio en el campo que se le desbloqueará a continuación. Para finalizar con el proceso, en la opción 'Pipeline', colocará el siguiente código: 

```
pipeline{

    agent any
    
    stages {
    
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/ElDeLaBarba/NoSQL']]])
            }
        }
        stage('Build') {
            steps {
                git branch: 'main', url: 'https://github.com/ElDeLaBarba/NoSQL'
                bat 'pip install pymongo'
                bat 'pip install pytest'
                bat 'python -u main.py'

            }
        }
        stage('Test') {
            steps {
                bat 'python -m main'
            }
        }
    }
}
```

Ahora, Jenkins se ocupará de comprobar que el programa compila y no contiene errores de código en la ejecución. 

### Pruebas de cargas de datos 
Para probar la base de datos y el tráfico que pudiera soportar se hicieron distintas pruebas de carga de datos.
Las mismas se hicieron con la herramienta "Locust", pensada para ser usada junto con python.

Para ejecutar la misma es necesario instalarla con el comando:

> pip install locust

Y crear un archivo de prueba que será ejecutado con el comando:

> locust -f {nombre_del_archivo}.py

En nuestro caso, ya creamos dos archivos: 'loadtest.py' y 'loadtest_create.py', que prueban peticiones de find y create respectivamente.
Una vez cargado el comando, nos podremos redirigir al navegador en la dirección default (http://0.0.0.0:8089) para revisar el funcionamiento de las pruebas y organizar el ritmo/fuerza de las mismas.

Para nuestro caso hicimos pruebas de lectura y carga de personas y domicilios, descubriendo límites de concurrencia en torno a los 400 usuarios y 800 escrituras:
1) [2023-11-22 22:52:53,316] DESKTOP-AO296UM/WARNING/locust.runners: Your selected spawn rate is very high (>100), and this is known to sometimes cause issues. Do you really need to ramp up that fast?
2) DESKTOP-AO296UM/WARNING/root: CPU usage above 90%! This may constrain your throughput and may even give inconsistent response time measurements! See https://docs.locust.io/en/stable/running-distributed.html for how to distribute the load over multiple CPU cores or machines

Para cadencias de carga de usuarios menos, como 40 concurrencias y 80 cargas en 15 segundos el sistema pudo resolver sin problemas, persistiendo la totalidad de los datos.
