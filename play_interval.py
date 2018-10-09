from note_relation import *
from play_midi import play_midi
import define
import random


def play_scale(note, scale_f):

    scale = scale_f(note)

    for i in scale[1: ]:

        print(define.note_name_display[note] + ' ' + define.note_name_display[i])

        piano_midi = pretty_midi.PrettyMIDI()
        piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
        piano = pretty_midi.Instrument(program=piano_program)

        note_number = pretty_midi.note_name_to_number(note)
        nt = pretty_midi.Note(velocity=100, pitch=note_number, start=0, end=0.5)
        piano.notes.append(nt)

        note_number = pretty_midi.note_name_to_number(i)
        nt = pretty_midi.Note(velocity=100, pitch=note_number, start=0.5, end=1)
        piano.notes.append(nt)

        note_number = pretty_midi.note_name_to_number(note)
        nt = pretty_midi.Note(velocity=100, pitch=note_number, start=1, end=2)
        piano.notes.append(nt)
        note_number = pretty_midi.note_name_to_number(i)
        nt = pretty_midi.Note(velocity=100, pitch=note_number, start=1, end=2)
        piano.notes.append(nt)

        piano_midi.instruments.append(piano)
        piano_midi.write('midi.mid')

        play_midi('midi.mid')


def play_scale_continuously(note, scale_f, shuffle=False):

    scale = scale_f(note)
    if shuffle:
        temp_scale = scale[1: ]
        random.shuffle(temp_scale)
        scale = [scale[0]] + temp_scale
    print("scale of " + define.note_name_display[note] + ": " + ", ".join([define.note_name_display[x] for x in scale]))

    cnt = 0
    cycle_length = 2

    piano_midi = pretty_midi.PrettyMIDI()
    piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
    piano = pretty_midi.Instrument(program=piano_program)

    for i in scale[1: ]:

        note_number = pretty_midi.note_name_to_number(note)
        nt = pretty_midi.Note(velocity=100, pitch=note_number, start=cycle_length * cnt + 0, end=cycle_length * cnt + 0.5)
        piano.notes.append(nt)

        note_number = pretty_midi.note_name_to_number(i)
        nt = pretty_midi.Note(velocity=100, pitch=note_number, start=cycle_length * cnt + 0.5, end=cycle_length * cnt + 1)
        piano.notes.append(nt)

        note_number = pretty_midi.note_name_to_number(note)
        nt = pretty_midi.Note(velocity=100, pitch=note_number, start=cycle_length * cnt + 1, end=cycle_length * cnt + cycle_length)
        piano.notes.append(nt)
        note_number = pretty_midi.note_name_to_number(i)
        nt = pretty_midi.Note(velocity=100, pitch=note_number, start=cycle_length * cnt + 1, end=cycle_length * cnt + cycle_length)
        piano.notes.append(nt)

        cnt += 1

    piano_midi.instruments.append(piano)
    piano_midi.write('midi.mid')

    play_midi('midi.mid')


def play_interval(note):

    # note should be white, and denoted in the form of str

    octave = next_octave_note(note)

    play_scale(note, up_c_scale)
    play_scale(octave, down_c_scale)
    play_scale(note, up_semitone_scale)
    play_scale(octave, down_semitone_scale)


def play_interval_continuously(note, shuffle=False):

    # note should be white, and denoted in the form of str

    octave = next_octave_note(note)

    play_scale_continuously(note, up_c_scale, shuffle=shuffle)
    play_scale_continuously(octave, down_c_scale, shuffle=shuffle)
    play_scale_continuously(note, up_semitone_scale, shuffle=shuffle)
    play_scale_continuously(octave, down_semitone_scale, shuffle=shuffle)
