from play_exam import play_exam
from random import randint
import pretty_midi
import define


def interval_exam(noteCnt=2):
    notes = list()
    std_number = pretty_midi.note_name_to_number('A4')
    for i in range(noteCnt):
        note = pretty_midi.note_number_to_name(std_number + randint(-12, 12))
        while note in notes:
            note = pretty_midi.note_number_to_name(std_number + randint(-12, 12))
        notes.append(note)
    play_exam(notes)

    ans = [define.note_name_display[x] for x in notes]
    ans = ' '.join(ans)
    user_ans = input()
    if ans == user_ans:
        print('Correct!')
        return True
    else:
        print('Wrong! Correct answer is: ' + ans)
        return False


if __name__ == '__main__':
    while True:
        interval_exam()
