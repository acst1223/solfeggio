import contextlib
with contextlib.redirect_stdout(None):
    import pygame as pg


def play_midi(midi_file):
    freq = 44100  # audio CD quality
    bitsize = -16  # unsigned 16 bit
    channels = 2  # 1 is mono, 2 is stereo
    buffer = 2048  # number of samples (experiment to get right sound)
    pg.mixer.init(freq, bitsize, channels, buffer)

    # optional volume 0 to 1.0
    pg.mixer.music.set_volume(0.8)

    try:
        clock = pg.time.Clock()
        try:
            pg.mixer.music.load(midi_file)
            # print("Music file {} loaded!".format(midi_file))
        except pg.error:
            print("File {} not found! {}".format(midi_file, pg.get_error()))
            return
        pg.mixer.music.play()
        # check if playback has finished
        while pg.mixer.music.get_busy():
            clock.tick(30)

    except KeyboardInterrupt:
        # if user hits Ctrl/C then exit
        # (works only in console mode)
        pg.mixer.music.fadeout(1000)
        pg.mixer.music.stop()
        raise SystemExit



