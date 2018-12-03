#!/usr/bin/env python3

import os
import speech_recognition as sr
import sys
from pydub import AudioSegment

# Constants
ARGUMENTS   = sys.argv[1:]
AUDIO_FILE	= ''
OUTPUT_FILE = ''
DURATION 	= 0
OFFSET 		= 0

# Functions
def usage(exitCode = 0):
    print('''Usage: {} [-a AudioFile -s BOOL ...]
    -a   AudioFile  	File Path of Audio (.WAV or .FLAC)
    -m   True			Use Microphone for Audio (Ignore File if Entered)
    -s   True 		 	Bool Whether to Save Output to File (Default: False)
    -sn  OutputFile 	Name for Output File. If Empty then AudioFile.txt Used
    -d   LENGTH     	Duration of the Audio to be Processed
    -o   OFFSET     	Starting Time (in Sec) to be Processed
    -g   True 			Play "Guess the Word" Game?'''.format(os.path.basename(sys.argv[0])))
    sys.exit(exitCode)

def recognizeFile():
	# TODO: Use adjust_for_ambient_noise() or SciPy for Noise Reduction
	pass

	# Create Instance of Recognizer Class
	r = sr.Recognizer()

	# Create Instance of AudioData Class
	name = sr.AudioFile(AUDIO_FILE)
	with name as source: audio = r.record(source) # AudioData Object

	# Analyze with Google Cloud Speech
    response = { # Set Up Response Object
        'success': True,
        'error': None,
        'transcription': None
    }
    try:
		response['transcription'] = r.recognize_google_cloud(audio)

	except sr.RequestError:
		# API was Unreachable or Unresponsive
		response['success'] = False
        response['error'] = 'API Unavailable'

    except sr.UnknownValueError:
        # speech was Unintelligible
        response["error"] = "Unable to Recognize Speech"

    # Catch Errors
    if response['error']:
    	print('ERROR: {}'.format(response['error']))
    	sys.exit(1)
    	
	# Check Whether to Save to File
	if OUTPUT_FILE.empty():
		pass
	else:
		with open(OUTPUT_FILE, 'w') as output:
		    output.write(script)

def recognizeMic():
	# Create Instance of Microphone Class
	mic = sr.Microphone()

	# Create Instance of Recognizer Class
	r = Recognizer()

	# Create Instance of AudioData Class
	with mic as source:
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)

	# Analyze with Google Cloud Speech

def convert2WAV():
	pass

# Main Execution
if __name__ == '__main__':

    # Parse Command Line Arguments
    while len(ARGUMENTS) and ARGUMENTS[0].startswith('-') and len(ARGUMENTS[0]) > 1:
        
        arg = ARGUMENTS.pop(0)
        
        if arg == '-a':
            AUDIO_FILE = ARGUMENTS.pop(0)

        elif arg == '-h':
            usage(0)

        else:
            usage(1)

    # Check Parameter Values
