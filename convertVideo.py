import subprocess

# Extract audio from video and compress audio
def processVideo(videoFile):

    fileWtihStrippedName = removeSuffix(video_file, ".mp4")
    newAudioFile = fileWtihStrippedName + ".wav"

    try:
        return callConversionProcess(fileWtihStrippedName, newAudioFile)

    except Exception as e:
        print("Error: " + str(e))
        return

#Convert and compress video file
def callConversionProcess(fileWtihStrippedName, newAudioFile):
    subprocess.call([
                        "ffmpeg -i " + video_file + " -acodec libopus -ac 1 -ar 16000 -compression_level 10 -application voip -vn " + newAudioFile],
                    shell=True)
    return fileWtihStrippedName


# Remove suffix from file name
def removeSuffix(string, suffix):
    if not string.endswith(suffix):
        return string
    return string[:len(string) - len(suffix)]
