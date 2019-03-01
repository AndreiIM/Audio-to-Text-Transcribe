import os
from convertVideo import processVideo
from convertVideo import removeSuffix
from formatTranscript import formatTranscript
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
from google.cloud import storage

def transcribeFile(file):
    # Convert video file to audio file
    #audioFilePath = processVideo(videoFile)
    # Strip audio file
    audioFilePath = removeSuffix(file, ".wav")

    if audioFilePath:
        # Gcloud bucket name
        bucketName = 'bucket name' #
        audioFileName = os.path.basename(audioFilePath) + '.wav'

        #Set environment variable using your credentials
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/../.json"
        uploadToGcloud(bucketName, audioFilePath + '.wav', audioFileName)

        #Asynchronously transcribes the audio file specified by the gcs_uri.
        operation = callGoogleAPI(audioFileName, bucketName)

        if not operation.done():
            print('Waiting for audio transcript...')

        result = operation.result()

        # Output transcription
        results = result.results
        formatTranscript(results, audioFilePath)
    else:
        print('Could not process file!')
        return

#Invoke the Google API
def callGoogleAPI(audioFileName, bucketName):
    client = speech.SpeechClient()
    audio = types.RecognitionAudio(uri="gs://" + bucketName + "/" + audioFileName)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code='en-US',
        sample_rate_hertz=16000,
        enable_word_time_offsets=True
    )
    operation = client.long_running_recognize(config, audio)
    return operation

# uploads compressed audio to gcloud bucket
def uploadToGcloud(bucketName, fileName, blobName):
    storageClient = storage.Client()
    bucket = storageClient.get_bucket(bucketName)

    blob = bucket.blob(blobName)
    blob.upload_from_filename(fileName)