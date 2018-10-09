from play_exam import play_exam
from random import randint
import pretty_midi
import define


def interval_exam(note_cnt=2):
    notes = list()
    std_number = pretty_midi.note_name_to_number('A4')
    for i in range(note_cnt):
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


def interval_exams(exam_cnt=20, note_cnt=2):
    succ_cnt = 0
    for i in range(exam_cnt):
        print('%d / %d' % (i + 1, exam_cnt))
        if interval_exam(note_cnt):
            succ_cnt += 1
            
    print()
    print("Acc: %d%%" % (succ_cnt / exam_cnt * 100))
    print()
    
    return succ_cnt / exam_cnt


if __name__ == '__main__':
    interval_exams()
