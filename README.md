Instalación y Configuración

-Clonar el Repositorio:

    git clone https://github.com/AdrianCortes35/RetoFinal.git
    cd RetoFinal


-Instalar Dependencias:

    pip install -r requirements.txt


-Configuración de la Base de Datos:

    Intrucciones de descarga de https://www.postgresql.org/download/linux/ubuntu/:

        # Create the file repository configuration:
        sudo sh -c 'echo "deb https://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

        # Import the repository signing key:
        wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

        # Update the package lists:
        sudo apt-get update

        # Install the latest version of PostgreSQL.
        # If you want a specific version, use 'postgresql-12' or similar instead of 'postgresql':
        sudo apt-get -y install postgresql


    En caso de que Postgresql no pueda conectarse al servidor:
        
        sudo make-ssl-cert generate-default-snakeoil --force-overwrite
        sudo service postgresql restart


    Creacion de Usuario/BBDD de psql:

        #Change the user to postgres :
        sudo su - postgres
            
        #Create User for Postgres (in the shell and NOT with psql)
        createuser user

        #Create Database (in the shell and NOT with psql)
	    createdb db

        #Access the postgres Shell
        psql #(enter the password for postgressql)

        #Provide the privileges to user
        alter user "user" with encrypted password 'admin';
        grant all privileges on database db to "user";


    Ejecutar manage.sh

        sh manage.sh

            FLASK_ENV=development: Establece la variable de entorno FLASK_ENV en development, lo que indica a Flask que se ejecute en modo de desarrollo. 

            DATABASE_URI=postgresql://user:admin@127.0.0.1:5432/db: Establece la variable de entorno DATABASE_URI con la cadena de conexión a la base de datos PostgreSQL.

            python3 manage.py: Ejecuta el script manage.py utilizando Python. Crea las tablas en la base de datos y realiza otras tareas relacionadas con la configuración inicial de la aplicación.    

-Tests

    Antes de los tests, ejecuta este comando para añadir el directorio actual a la variable de entorno PYTHONPATH.

        export PYTHONPATH="$PYTHONPATH:$PWD"

    Comando para ejecutar tests:
        
        pytest tests/tests_app.py

    Para ver Coverage (Min 80%)

        coverage run -m pytest tests/prueba.py
	    coverage report -m

-Git

    Subir cambios en una rama nueva

    git add file
    git commit -m "Comentario"
    git push

    SOLO si funcionen los test con un minimo de coverage de 80% subir pull request al repositorio de Git para juntar con main