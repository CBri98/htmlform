FROM python:3

#set della directory per l'app
WORKDIR ./

#copia tutti i file sul container
COPY . .

#installa dependencies
RUN pip install --no-cache-dir -r requirements.txt

#specifica della porta da utilizzare
EXPOSE 5000

#comando da avviare
CMD ["python", "./htmlform.py"]
