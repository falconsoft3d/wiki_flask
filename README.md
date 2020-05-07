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
sudo apt-get install libapache2-mod-wsgi python-dev -y
``` 






