# Instalar Flask

# 1. Actualizamos el sistema 
```  
sudo apt update
``` 

# 2. Instalamos Apache
```  
sudo apt install apache2
apache2 -version
``` 

# 3. Firewall
```  
sudo ufw app list
sudo ufw allow 'Apache'
``` 

# 4. Systemctl
```  
sudo systemctl status 'apache2'
Ctrl + C
``` 

# 5. Instalando librerias
```  
sudo apt-get install libapache2-mod-wsgi python-dev pyhton-pip -y
pip install flask
pip install flask_sqlalchemy
pip install tornado
``` 

# 6. Instalando librerias
```  
cd /var/www
mkdir webApp
cd webApp

mkdir webApp
cd webApp
``` 

# 7. Creammos el fichero de flask
```  
nano main.py
```  

```  
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
``` 

# 8. Configuramos el webApp.conf
```  
nano /etc/apache2/sites-available/webApp.conf
```  
```  
<VirtualHost *:80>
                ServerName 127.121.12.1212
                ServerAdmin email@email.com
                WSGIScriptAlias / /var/www/webApp/webapp.wsgi
                <Directory /var/www/webApp/webApp/>
                            Order allow,deny
                            Allow from all
                </Directory>
                ErrorLog ${APACHE_LOG_DIR}/error.log
                LogLevel warn
                CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```









