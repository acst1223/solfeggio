note_alphabet = {
    'C': 'do',
    'D': 're',
    'E': 'mi',
    'F': 'fa',
    'G': 'sol',
    'A': 'la',
    'B': 'si',
    'C#': 'hi',
    'Db': 'hi',
    'D#': 'fu',
    'Eb': 'fu',
    'F#': 'yo',
    'Gb': 'yo',
    'G#': 'i',
    'Ab': 'i',
    'A#': 'mu',
    'Bb': 'mu'
}
note_name_display = dict()
for i in range(9):
    if i == 0:
        note_name_display['A0'] = 'LA2'
        note_name_display['A#0'] = 'MU2'
        note_name_display['Bb0'] = 'MU2'
        note_name_display['B0'] = 'SI2'
    elif i == 8:
        note_name_display['C8'] = 'do5'
    elif i <= 2:
        for j in note_alphabet.keys():
            note_name_display[j + str(i)] = note_alphabet[j].upper()
            if i == 1:
                note_name_display[j + str(i)] += '1'
    else:
        for j in note_alphabet.keys():
            note_name_display[j + str(i)] = note_alphabet[j]
            if i != 3:
                note_name_display[j + str(i)] += str(i - 3)
