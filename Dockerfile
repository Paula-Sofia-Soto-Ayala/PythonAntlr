# Usar la imagen base de Python
FROM python:3.12

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de requisitos al contenedor
COPY ./requirements.txt ./requirements.txt

# Instalar las dependencias desde requirements.txt
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

# Copiar todo el código fuente de la aplicación al contenedor
COPY . .

# Exponer el puerto en el que se ejecutará la aplicación
EXPOSE 80

# Comando para ejecutar la aplicación con Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
