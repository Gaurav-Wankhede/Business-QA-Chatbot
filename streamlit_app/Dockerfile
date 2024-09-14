# This is the container with python
FROM python:3.9-slim

# This copy everything present in the directory
COPY . /app

# Set /app as Working Directory
WORKDIR /app

# Run pip install requirements
RUN pip install -r requirements.txt

# Tell Docker to run port 80 at runtime. Port 80 refers to HTTP
EXPOSE 8080

# Set default command for the container to run the app with Streamlit
ENTRYPOINT ["streamlit", "run"]

# This command tells Streamlit to run the main.py file
CMD ["main.py"]