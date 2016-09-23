#!/usr/bin/env python3

import io, os, subprocess, wave, aifc, math, audioop
import collections, threading
import platform, stat
import json, hashlib, hmac, time, base64, random, uuid
import tempfile, shutil

# NOTE: this example requires PyAudio because it uses the Microphone class
from pocketsphinx import pocketsphinx
from pocketsphinx import Decoder
from sphinxbase import sphinxbase
import speech_recognition as sr




def recognizeTrucho(recog, audio_data, language = "webModel", keyword_entries = [], show_all = False):
        """
        Performs speech recognition on ``audio_data`` (an ``AudioData`` instance), using CMU Sphinx.
        The recognition language is determined by ``language``, an RFC5646 language tag like ``"en-US"`` or ``"en-GB"``, defaulting to US English. Out of the box, only ``en-US`` is supported. See `Notes on using `PocketSphinx <https://github.com/Uberi/speech_recognition/blob/master/reference/pocketsphinx.rst>`__ for information about installing other languages. This document is also included under ``reference/pocketsphinx.rst``.
        Returns the most likely transcription if ``show_all`` is false (the default). Otherwise, returns the Sphinx ``pocketsphinx.pocketsphinx.Decoder`` object resulting from the recognition.
        Raises a ``speech_recognition.UnknownValueError`` exception if the speech is unintelligible. Raises a ``speech_recognition.RequestError`` exception if there are any issues with the Sphinx installation.
        """
        # create decoder object

        MODELDIR = language

        config = Decoder.default_config()
        config.set_string("-hmm", os.path.join(MODELDIR, 'acoustic_model')) # set the path of the hidden Markov model (HMM) parameter files
        config.set_string("-lm", os.path.join(MODELDIR, 'language_model.lm.bin'))
        config.set_string("-dict", os.path.join(MODELDIR, 'pronounciation-dictionary.dict'))
        config.set_string("-logfn", os.devnull) # disable logging (logging causes unwanted output in terminal)
        decoder = Decoder(config)

        # obtain audio data
        raw_data = audio_data.get_raw_data(convert_rate = 16000, convert_width = 2) # the included language models require audio to be 16-bit mono 16 kHz in little-endian format

        # obtain recognition results
        if keyword_entries: # explicitly specified set of keywords
            with tempfile_TemporaryDirectory() as temp_directory:
                # generate a keywords file - Sphinx documentation recommendeds sensitivities between 1e-50 and 1e-5
                keywords_path = os.path.join(temp_directory, "keyphrases.txt")
                with open(keywords_path, "w") as f:
                    f.writelines("{} /1e{}/\n".format(keyword, 45 * sensitivity - 50) for keyword, sensitivity in keyword_entries)

                # perform the speech recognition with the keywords file (this is inside the context manager so the file isn;t deleted until we're done)
                decoder.set_kws("keywords", keywords_path)
                decoder.set_search("keywords")
                decoder.start_utt() # begin utterance processing
                decoder.process_raw(raw_data, False, True) # process audio data with recognition enabled (no_search = False), as a full utterance (full_utt = True)
                decoder.end_utt() # stop utterance processing
        else: # no keywords, perform freeform recognition
            decoder.start_utt() # begin utterance processing
            decoder.process_raw(raw_data, False, True) # process audio data with recognition enabled (no_search = False), as a full utterance (full_utt = True)
            decoder.end_utt() # stop utterance processing

        if show_all: return decoder

        # return results
        hypothesis = decoder.hyp()
        if hypothesis is not None: return hypothesis.hypstr
        raise UnknownValueError() # no transcriptions available

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Sphinx
try:
    print("Sphinx thinks you said " + recognizeTrucho(r, audio,language="webModel"))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

