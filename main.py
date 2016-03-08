import speech_recognition as sr

WAV_FILE = "Audio.wav"
r = sr.Recognizer()

def main():
	with sr.WavFile(WAV_FILE) as source:
		audio = r.record(source)

	# print(r.recognize_google(audio))
	print(r.recognize_sphinx(audio))

if __name__ == "__main__":
	main()
