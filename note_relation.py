import pretty_midi


def next_white(note):

    # note should be white, and denoted in the form of str

    head = note[0]
    tail = int(note[1])

    head = chr(ord(head) + 1)
    if head == 'H':
        head = 'A'
    if head == 'C':
        tail += 1

    return head + str(tail)


def prev_white(note):

    # note should be white, and denoted in the form of str

    head = note[0]
    tail = int(note[1])

    head = chr(ord(head) - 1)
    if head == '@':
        head = 'G'
    if head == 'B':
        tail -= 1

    return head + str(tail)


def next_note(note):

    # note should be denoted in the form of str

    return pretty_midi.note_number_to_name(pretty_midi.note_name_to_number(note) + 1)


def prev_note(note):

    # note should be denoted in the form of str

    return pretty_midi.note_number_to_name(pretty_midi.note_name_to_number(note) - 1)


def next_octave_note(note):

    # note should be denoted in the form of str

    head = note[0: -1]
    tail = int(note[-1])

    return head + str(tail + 1)


def prev_octave_note(note):

    # note should be denoted in the form of str

    head = note[0: -1]
    tail = int(note[-1])

    return head + str(tail - 1)


def note_equal(note1, note2):

    return pretty_midi.note_name_to_number(note1) == pretty_midi.note_name_to_number(note2)


def up_c_scale(note):

    # note should be white and denoted in the form of str

    res = list()
    octave_note = next_octave_note(note)

    while True:
        res.append(note)
        if note_equal(note, octave_note):
            break
        note = next_white(note)

    return res


def down_c_scale(note):

    # note should be white and denoted in the form of str

    res = list()
    octave_note = prev_octave_note(note)

    while True:
        res.append(note)
        if note_equal(note, octave_note):
            break
        note = prev_white(note)

    return res


def up_semitone_scale(note):

    # note should be denoted in the form of str

    res = list()
    octave_note = next_octave_note(note)

    while True:
        res.append(note)
        if note_equal(note, octave_note):
            break
        note = next_note(note)

    return res


def down_semitone_scale(note):

    # note should be denoted in the form of str

    res = list()
    octave_note = prev_octave_note(note)

    while True:
        res.append(note)
        if note_equal(note, octave_note):
            break
        note = prev_note(note)

    return res
