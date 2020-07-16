# The Dockerfile defines the image's environment
# Import Python runtime and set up working directory
FROM python:3
ENV PYBASE /pybase
ENV PYTHONUSERBASE $PYBASE
ENV PATH $PYBASE/bin:$PATH

WORKDIR /app
ADD . /app

RUN pip install virtualenv
RUN virtualenv venv
RUN source venv/bin/activate

# Install any necessary dependencies
# RUN pip install -r requirements.txt
RUN venv/bin/pip install -r requirements.txt

# Open port 80 for serving the webpage
EXPOSE 80

# Run main.py when the container launches
CMD ["python", "main.py"]
