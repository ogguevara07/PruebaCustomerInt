# API CRUD

### Instalacion

Se sugiere utilizar un entorno virtual como virtualenv.

### Linux

ir a la carpeta donde esta el archivo main.py y ejecutar los siguientes comandos

```shel
    cd ~/path/PruebaTecnica
    virtualenv env
    source env/bin/activate
```
### windows 
```shell
    python -m venv env
    #cmd
    C:\> env\Scripts\activate.bat
    #powershell
    PS C:\> env\Scripts\Activate.ps1
```

Para poder ejecutar el script en python es necesario instalar algunas dependencias como pyjwt y en caso de que este en un entorno la libreria request, para ellos correremos el siguiente script en consola.


```shell
    pip install -r requirment.txt
```
### API Y DATA
utilice una de las herramientas de https://jsonplaceholder.typicode.com que me permite crear una API simple pero efectiva en este caso

las credenciales estan en JWT se puede utilizar la pagina https://jwt.io/ para desencriptar la crendicales pero una de estas es 

email=orlando@guevara.com \
password=12345678