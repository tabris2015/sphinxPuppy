import os
from os import path
from pocketsphinx import pocketsphinx
from pocketsphinx import Decoder
import speech_recognition as sr
from utils import *
import serial

#ser = serial.Serial('/dev/ttyUSB0', 38400)

#directories for english model

#MODELDIR = "webModel"

#config = Decoder.default_config()
#config.set_string('-hmm', path.join(MODELDIR, 'acoustic-model'))
#config.set_string('-lm', path.join(MODELDIR, 'language-model.lm.bin'))
#config.set_string('-dict', path.join(MODELDIR, 'pronounciation-dictionary.dict'))

#directories for aymara model

MODELDIR = "aymaraModel"

config = Decoder.default_config()
config.set_string('-hmm', path.join(MODELDIR, 'acousticModel'))
config.set_string('-lm', path.join(MODELDIR, 'cmd_games.lm'))
config.set_string('-dict', path.join(MODELDIR, 'aymara.dict'))



config.set_string("-logfn", os.devnull)
decoder = Decoder(config)





def callback(recognizer, audio):
	print "reconociendo..."
	raw_data = audio.get_raw_data(convert_rate=16000, convert_width=2)
	decoder.start_utt()
	decoder.process_raw(raw_data, False, True)
	decoder.end_utt()
	hypothesis = decoder.hyp()
	try:
		commands = hypothesis.hypstr.split()
		command, value = getCommand(hypothesis.hypstr)
		#ser.write(value)
		print commands, command, value
	except:
		print "nada reconocido"

print "creando objetos para el reconocimiento"
r = sr.Recognizer()
r.energy_threshold = 500 # minimum audio energy to consider for recording
r.pause_threshold = 0.5 # seconds of non-speaking audio before a phrase is considered complete
r.phrase_threshold = 0.2 # minimum seconds of speaking audio before we consider the speaking audio a phrase - values below this are ignored (for filtering out clicks and pops)
r.non_speaking_duration = 0.4 # seconds of non-speaking audio to keep on both sides of the recording

try:
	print "crea fuente"
	source = sr.Microphone()
	print "ajusta ruido"
	#r.adjust_for_ambient_noise(source, duration = 1)

	print "habla..."
	stop_listen = r.listen_in_background(source, callback)

	while True:
		pass	
except:
	pass