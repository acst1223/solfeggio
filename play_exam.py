import pretty_midi
from play_midi import play_midi


def play_exam(notes, std_duration=1, note_duration=0.5, notes_duration=2):

    piano_midi = pretty_midi.PrettyMIDI()
    piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
    piano = pretty_midi.Instrument(program=piano_program)

    note_number = pretty_midi.note_name_to_number('A4')
    nt = pretty_midi.Note(velocity=100, pitch=note_number, start=0, end=std_duration)
    piano.notes.append(nt)
    
    l = len(notes)
    
    if l == 1:
        note_duration = 0

    else:
        for i in range(l):
            note_number = pretty_midi.note_name_to_number(notes[i])
            nt = pretty_midi.Note(velocity=100, pitch=note_number, start=std_duration + note_duration * i,
                                  end=std_duration + note_duration * (i + 1))
            piano.notes.append(nt)

    for eachNote in notes:
        note_number = pretty_midi.note_name_to_number(eachNote)
        nt = pretty_midi.Note(velocity=100, pitch=note_number, start=std_duration + note_duration * l,
                              end=std_duration + note_duration * l + notes_duration)
        piano.notes.append(nt)
        
    piano_midi.instruments.append(piano)
    piano_midi.write('midi.mid')

    play_midi('midi.mid')