# Morse Code to Text API

Este proyecto es una API REST creada con **FastAPI** que convierte texto en código Morse a texto legible. Utiliza **ANTLR** para el análisis y la conversión de código Morse.

## Requisitos

- Python 3.7 o superior
- **FastAPI**: Framework web para construir APIs rápidas.
- **Uvicorn**: Servidor ASGI para ejecutar FastAPI.
- **ANTLR**: Para generar el lexer y parser para el código Morse.

## Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_DIRECTORIO_DEL_REPOSITORIO>
   ```

2. **Instalar requerimientos**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Iniciar aplicación**:
   ```bash
   python -m uvicorn app:app --reload
   ```

## Dockerización y Publicación en Docker Hub
- **Construir imagen de docker**
```txt
docker build -t nombre_usuario/morse-api .

(ejemplo: 
docker build -t nombre_usuario/morse-api .)
```

- **Crear y ejecutar contenedor**
```txt
docker run -p 80:80 --name <nombre-contenedor> <nombre-de-imagen>

(ejemplo: 
docker run -p 80:80 --name morse-container mi_usuario/morse-api
)
```

- **Acceder al contenedor en ejecución**
```txt
docker exec -it <nombre-contenedor> /bin/bash
```

- **Etiquetar y Publicar la imagen en DockerHub**
```txt
docker login
docker tag <nombre-de-imagen> <usuario-dockerhub>/<nombre-de-imagen>:latest
docker push <usuario-dockerhub>/<nombre-de-imagen>:latest

(ejemplo:
docker tag mi_usuario/morse-api mi_usuario/morse-api:latest
docker push <usuario-dockerhub>/<nombre-de-imagen>:latest
)
```

### Otros Comandos Útiles

- **Iniciar un contenedor detenido**
```txt
docker start <nombre-contenedor>
```
- **Detener un contenedor en ejecución**
```txt
docker stop <nombre-contenedor>
```