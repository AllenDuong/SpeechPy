#!/usr/bin/env python3

import os
import speech_recognition as sr
import sys
from pydub import AudioSegment

# Constants
ARGUMENTS   = sys.argv[1:]
AUDIO_FILE	= ''
OUTPUT_FILE = ''

# Functions
def usage(exitCode = 0):
    print('''Usage: {} [-a AudioFile -s BOOL -sn OutputFile]
    -a   AudioFile 	File Path of Audio (.WAV or .FLAC)
    -s   True/False 	Bool Whether to Save Output to File
    -sn  OutputFile 	Name for Output File. If Empty then AudioFile.txt Used'''.format(os.path.basename(sys.argv[0])))
    sys.exit(exitCode)

def audioRecognize():
	# Create Instance of AudioData Class
	name = sr.AudioFile(AUDIO_FILE)
	with name as source: audio = r.record(source) # AudioData Object

	# Create Instance of Recognizer Class - Subclass Google Cloud Speech
	r = recognize_google_cloud(AUDIO_FILE)

	# Check Whether to Save to File
	if OUTPUT_FILE.empty():
		pass
	else:
		with open(OUTPUT_FILE, "w") as output:
		    output.write(r)
		    
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

    # Perform Audio Analysis
