from lib.diary import Diary, DiaryEntry


"""
Given one diary entry is provided and diary.add() is called
Diary entry is added to the Diary / entry is returned
"""

def test_diary_entry_is_added():
    diary = Diary()
    entry = DiaryEntry("Tuesday", "Today I went to the park with my dog.")
    diary.add(entry)
    assert diary.entries == [entry]

"""
Given 3 entries are added
#diary.all returns all 3 entries
"""

def test_multiple_entries_added():
    diary = Diary()
    entry_one = DiaryEntry("Tuesday", "Today I went to the park with my dog.")
    entry_two = DiaryEntry("Wednesday", "Did some shopping")
    entry_three = DiaryEntry("Thursday", "Went to the pub with my friend in the evening to watch the football.")
    diary.add(entry_one)
    diary.add(entry_two)
    diary.add(entry_three)
    assert diary.entries == [entry_one, entry_two, entry_three]

"""
Given 1 diary entry of 9 words
#count_words returns 9
"""

def test_word_count_for_one_entry_returned():
    diary = Diary()
    entry = DiaryEntry("Tuesday", "Today I went to the park with my dog.")
    diary.add(entry)
    assert diary.count_words()== 9

"""
Given 2 diary entries of 5 words each
#count_words returns 10
"""

def test_word_count_for_3_entries_returned():
    diary = Diary()
    entry_one = DiaryEntry("Tuesday", "Today I went to the park with my dog.")
    entry_two = DiaryEntry("Wednesday", "Did some shopping")
    entry_three = DiaryEntry("Thursday", "Went to the pub with my friend in the evening to watch the football.")
    diary.add(entry_one)
    diary.add(entry_two)
    diary.add(entry_three)
    assert diary.count_words()== 26

"""
Given a wpm of 5 and one 5 word entry
#reading_time returns 1
"""

def test_reading_time_returned_for_one_entry():
    diary = Diary()
    entry_one = DiaryEntry("Monday", "I ate a ham sandwich.")
    diary.add(entry_one)
    assert diary.reading_time(5) == 1

"""
Given a wpm of 5 and 25 total words of entries
#reading_time returns 5
"""

def test_reading_time_returned_for_three_entries():
    diary = Diary()
    entry_one = DiaryEntry("Monday", "I ate a ham sandwich.")
    entry_two = DiaryEntry("Tuesday", "I ate two ham sandwiches.")
    entry_three = DiaryEntry("Wednesday", "I ate three ham sandwiches.")
    diary.add(entry_one)
    diary.add(entry_two)
    diary.add(entry_three)
    assert diary.reading_time(5) == 3

"""
Given a non integer reading time is calculated
#reading_time returns an integer rounded up
"""

def test_reading_time_is_rounded_up():
    diary = Diary()
    entry_one = DiaryEntry("Monday", "I ate a ham sandwich.")
    entry_two = DiaryEntry("Tuesday", "I ate two ham sandwiches.")
    entry_three = DiaryEntry("Wednesday", "I ate three ham sandwiches and slept.")
    diary.add(entry_one)
    diary.add(entry_two)
    diary.add(entry_three)
    assert diary.reading_time(5) == 4

"""
Given one entry of 25 words, and a wpm of 5 and 5 minutes
#best_entry returns the entry
"""

"""
Given no entry under 25 words and a wpm of 5 and 5 minutes
#best_entry returns "No entry available."
"""

"""
Given 3 entries, all under 25 words, and a wpm of 5 and 5 minutes
#best_entry returns the closest entry under 25 words
"""


"""

"""