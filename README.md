# sphinxPuppy
code repository for a little voice controlled quadruped robot using pocketsphinx

## how to use

You need to install the following in order to run this code properly:
  - pocketsphinx
  - sphinx-base
  - python-pocketsphinx
  - pyaudio
  - python speech recognition

Once you have all the requeriments, the main recognition program is contained in pocket_working.py

## description
`pocket_working.py` use speech_recognition module for connect with the microphone and pocketsphinx for the recognition.

A modified language model was defined in the webModel directory using an online tool. This language model is using 
an existing english acoustic model. The vocabulary of our model can be seen in the `0460.vocab`file.

A sequence of commands is sent through the serial port to a microcontroller for controlling the servos. Code will be updated soon.

