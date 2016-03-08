import speech_recognition as sr

WAV_FILE = "CYYZ-Twr-Mar-07-2016-2230Z_SMALL.wav"

# print(WAV_FILE)

r = sr.Recognizer()

with sr.WavFile(WAV_FILE) as source:
	# print(source)
	audio = r.record(source)
	# print(audio)
r.recognize_google(audio)
# print(r.recognize_sphinx(audio))