## Examen para vacante Backend en EMQU M&eacute;xico

📚 Backend en Python con Flask y SQL Lite para persistencia

1. Login

2. Gesti&oacute;n de Equipos

3. Ejecuci&oactue;n y Estadisticas


### Ejecucion

1. Clone the repository

```
        git clone https://github.com/keymanky/backend_emqu_exam
```

2. Run with Docker

```
        docker build -t backend_emqu_exam_jsm .
        docker run -p 4321:4321 backend_emqu_exam_jsm
```

2. Or run with virtual environment

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

3. Test API, for example import Collation in postman
