import os
from sys import argv
from googleTranscribe import transcribeFile

searchDirectory = argv[1]

#Run the google API for each file inside the specified directory
def runTranscript(directoryFile):

    files = os.listdir(directoryFile)
    # Removes any unwanted spaces in the file names
    for file in files:
        os.rename(os.path.join(directoryFile, file), os.path.join(directoryFile, file.replace(' ', '_')))

    # Get each video file in directory and run the speech to text recognition API
    for file in os.listdir(directoryFile):
        # For video file,change the extension and uncomment
        if file.endswith(".wav"):
            print("Converting " + file)
            filePath = os.path.join(directoryFile, file)
            transcribeFile(filePath)

        else:
            continue

runTranscript(searchDirectory)