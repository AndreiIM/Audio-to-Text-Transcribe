import math

#Convert the transcription
def formatTranscript(results, audio_file):

    file = open( audio_file + ".txt", "w")
    # Numbering lines in file
    counter = 0
    SIZE = 20

    for result in results:
        alternatives = result.alternatives
        for alternative in alternatives:
            words = alternative.words
            transcript = ''
            if len(words) < SIZE:
                transcript = alternative.transcript
                counter = writeWordsToFile(counter, file, words , transcript, False)
            else:
                chunk = list(chunks(words, SIZE))
                for words in chunk:
                    counter = writeWordsToFile(counter, file, words , transcript, True)
    file.close()

#Writing the transcript
def writeWordsToFile(counter, file, words, transcript, flag):

    startTime = words[0].start_time
    endTime = words[-1].end_time

    startTimeSeconds = startTime.seconds + startTime.nanos * 1e-9
    endTimeSeconds = endTime.seconds + endTime.nanos * 1e-9

    if flag:
        section = transcript
        for word_info in words:
            section += word_info.word + " "
        counter = writeToFile(counter, endTimeSeconds, file, section, startTimeSeconds)
    else:
        counter = writeToFile(counter, endTimeSeconds, file, transcript, startTimeSeconds)
    return counter

#Writing on disk
def writeToFile(counter, end_time_seconds, file, section, start_time_seconds):
    counter += 1
    file.write(str(counter) + '\n')
    file.write(format_time(start_time_seconds) + ' --> ' + format_time(end_time_seconds) + '\n')
    file.write(section + "\n\n")
    return counter

#Time formatting for timestamps
def format_time(seconds):
    frac, whole = math.modf(seconds)
    f = frac * 1000
    m, s = divmod(whole, 60)
    h, m = divmod(m, 60)
    return "%d:%02d:%02d,%03d" % (h, m, s, f)


# Break up large transcript sections
def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

