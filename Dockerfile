#Base image for Google Cloud SDK
FROM gcr.io/google-appengine/python

# Create a virtualenv for dependencies. This isolates these packages from system-level packages.
RUN virtualenv /env

# Setting these environment variables are the same as running source /env/bin/activate.
ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

# Copy the application's requirements.txt and scripts
# Run pip to install all dependencies into the virtualenv.
RUN mkdir -p /usr/app
WORKDIR /usr/app
COPY Audio-to-Text-Transcribe-master/ /usr/app    	
RUN pip install -r /usr/app/requirements.txt

CMD ["python", "runAudioToTranscript.py","/usr/app/Examples/"]	 	