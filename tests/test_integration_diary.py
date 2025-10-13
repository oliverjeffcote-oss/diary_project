from lib.diary import Diary, DiaryEntry


"""
Given one diary entry is provided and diary.add() is called
Diary entry is added to the Diary / entry is returned
"""

def test_diary_entry_is_added():
    diary = Diary()
    entry = DiaryEntry("Tuesday", "Today I went to the park with my dog.")
    diary.add(entry)
    assert diary.entries == [{"title" : "Tuesday", "contents" : "Today I went to the park with my dog."}]

"""
Given 3 entries are added
#diary.all returns all 3 entries
"""

"""
Given 1 diary entry of 25 words
#count_words returns 25
"""

"""
Given 2 diary entries of 5 words each
#count_words returns 10
"""

"""
Given a wpm of 5 and 25 total words of entries
#reading_time returns 5
"""

"""
Given a wpm of 5 and one 5 word entry
#reading_time returns 1
"""

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