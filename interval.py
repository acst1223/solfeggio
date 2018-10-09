from play_interval import *


if __name__ == '__main__':
    # training_notes = ['C4', 'D4', 'E4', 'F4', 'G4', 'A3', 'B3']
    training_notes = ['C4', 'E4', 'G4', 'F4', 'B3', 'A3', 'D4']
    for note in training_notes:
        play_interval_continuously(note, shuffle=True)