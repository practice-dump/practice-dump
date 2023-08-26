# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 11:15:30 2020

@author: TANMEY
"""
# Run conda install -c conda-forge moviepy --y for spyder, !pip install moviepy for jupyter

import moviepy.editor
video=moviepy.editor.VideoFileClip('lifeback_testing.mp4') #Videofile address
audio=video.audio.write_audiofile('testing01.wav') #name of audiofile
from scipy.io import wavfile
samplerate, data = wavfile.read('testing01.wav') #Uploading audiofile
type(data)  # It is numpy.ndarray 
samplerate