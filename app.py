#raise(SyntaxError("ERR"))
import pyaudio
import wave, os

p = pyaudio.PyAudio()
# for ii in range(p.get_device_count()):
#     print(ii, p.get_device_info_by_index(ii).get('name'))


def record_audio():
    
    # The directory that 'test.py' is stored
    directory = os.path.dirname(os.path.abspath(__file__))
    # The path to the 'checklist.txt'
    wav_output_filename = os.path.join(directory, 'record2.wav')

    form_1 = pyaudio.paInt32 # 16-bit resolution
    chans = 1 # 1 channel
    samp_rate = 44100 # 44.1kHz sampling rate
    chunk = 4096 # 2^12 samples for buffer
    record_secs = 20 # seconds to record
    dev_index = 1 # device index found by p.get_device_info_by_index(ii)
    #wav_output_filename = 'test2.wav' # name of .wav file

    audio = pyaudio.PyAudio() # create pyaudio instantiation

    # create pyaudio stream
    stream = audio.open(format = form_1,rate = samp_rate,channels = chans, \
                        input_device_index = dev_index,input = True, \
                        frames_per_buffer=chunk)
    print("recording")
    frames = []

    # loop through stream and append audio chunks to frame array
    for ii in range(0,int((samp_rate/chunk)*record_secs)):
        data = stream.read(chunk, exception_on_overflow = False)
        frames.append(data)

    print("finished recording")

    # stop the stream, close it, and terminate the pyaudio instantiation
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # save the audio frames as .wav file
    wavefile = wave.open(wav_output_filename,'wb')
    wavefile.setnchannels(chans)
    wavefile.setsampwidth(audio.get_sample_size(form_1))
    wavefile.setframerate(samp_rate)
    wavefile.writeframes(b''.join(frames))
    wavefile.close()

    return wav_output_filename
