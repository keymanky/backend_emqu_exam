## Examen para vacante Backend en EMQU M&eacute;xico

📚 Backend en Python con Flask y SQL Lite para persistencia

1. Login

2. Gesti&oacute;n de Equipos

3. Ejecuci&oacute;n y Estadisticas


### Ejecucion

1. Clona el repositorio

```
        git clone https://github.com/keymanky/backend_emqu_exam
```
2. Renombra el archivo env.env a .env es decir que empiece en PUNTO es un archivo oculto ".env" si usas linux dentro del proyecto puedes usar:

```
        mv env.env .env
```

3. Corre Docker dentro del projecto

```
        docker build -t backend_emqu_exam_jsm .
        docker run -p 4321:4321 backend_emqu_exam_jsm
```

3. O correlo con virtual environment, version de python 3.10 

```
        python -m venv venv/
```

Windows

```
        venv\Scripts\activate
```
Linux/Mac OS

```
        source venv/bin/activate
```

```
        pip install -r requirements.txt
        python app.py
```

4. Por ultimo prueba los request de la coleccion de postman enviada
