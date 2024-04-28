## 1. Which base image do you want to use?
FROM python:3.8-slim

## 2. Set the working directory
WORKDIR /app/

## 3. Copy the requirement.txt file into the working directory.
COPY flask-demo/requirements.txt .

## 4. Install the dependencies
RUN pip install -r requirements.txt

## 5. Copy the rest of application
COPY flask-demo/ . 

## 6. Document and inform the developer that the application will use PORT 5000 of the container.
EXPOSE 5000

## 7. Set the environment variable as asked.
ENV FLASK_APP=app.py

## 7. Define the command to run when the container starts.
CMD ["flask","run","--host=0.0.0.0"]