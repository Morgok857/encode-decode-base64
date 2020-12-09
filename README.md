# Descripción
Este script esta pensado para tomar un archivo y cifrarlo en base64 o realizar la acción inversa. El archivo resultante de estas operaciones se deja en el mismo directorio que el archivo original.

Cree esta herramienta a fin de facilitarme el manejo de los los secretos en Kubernetes, los cuales requieren que antes de subirlos a nuestro cluster su contenido sea cifrado a base64.

**Versión:** 1.00

## Requerimientos:
- python3      
	
## Parámetros:

```
optional arguments:
  -h, --help            show this help message and exit
  -d, --decode          Decore File content form base64
  -e, --encode          Code File content to base64
  -f FILE, --file FILE  File to use
  -v, --version         Show Version
  -vvv, --verbose       Start logging in verbose mode
```

## Ejemplos de uso:

Imaginemos que tenemos el siguiente archivo:

```
$ cat to-convert.yaml

DATABASE: testdb
HOST: 192.168.3.68
USERNAME: root
PASSWORD: p4!@f^VG^A'
```

Si queremos cifrar nuestro archivo utilizaremos el comando:
```  
$ python3 main.py --file to-convert.yaml -e

Start to read and encode file: to-convert.yaml
Data saved into: to-convert.yaml.base64
Task completed successfully

```
Al revisar el contenido de nuestro nuevo archivo veremos los datos que necesitamos cifrados:

```
$ cat to-convert.yaml.base64 

DATABASE: dGVzdGRi
HOST: MTkyLjE2OC4zLjY4
USERNAME: cm9vdA==
PASSWORD: cDQhQGZeVkdeQSc=
```
	
Tomando el archivo que ciframos como ejemplo, si lo que queremos es descifrar nuestro archivo utilizaremos el comando:
```
$ python3 main.py --file to-convert.yaml.base64 -d

Start to read and decode file: to-convert.yaml.base64
Data saved into: to-convert.yaml.base64.txt
Task completed successfully
```

Ahora mostramos el contenido del nuevo archivo por pantalla y veremos algo similar a: 
```
$ cat to-convert.yaml.base64.txt

DATABASE: testdb
HOST: 192.168.3.68
USERNAME: root
PASSWORD: p4!@f^VG^A'
```
**Nota:** El parametro '--file' soporta que la ruta del archivo sea dinámica como estática.

# Instalación

Empezamos como siempre, clonamos el repositorio:

```
git clone https://github.com/Morgok857/encode-decode-base64.git
```

Ingresamos al directorio que nos creo Git:

```
cd encode-decode-base64
```

Listo, ya podemos empezar a utilizar nuestra herramienta !!!    