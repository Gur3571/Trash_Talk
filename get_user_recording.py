import sounddevice
from scipy.io.wavfile import write
import numpy as np
import wavio


def getUserRecording() :
    fs = 44100
    #second = int(input("Enter time duration in seconds: "))
    print("\n*** NOW RECORDING ***")
    record_voice = sounddevice.rec( int ( 3 * fs ) , samplerate = fs , channels = 2, dtype=np.int16)
    #print(record_voice)
    # record_voice = sounddevice.rec( int ( 5 * fs ) , samplerate = fs , channels = 2, dtype=np.int16)

    sounddevice.wait()

    wavio.write('out.wav', record_voice, fs ,sampwidth=2)
    print("*** NOW FINISHED! ***\n")