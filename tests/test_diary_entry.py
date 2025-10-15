from lib.diary import DiaryEntry
import pytest

"""
Given a new Diary Entry is instatiated with a title and contents as strings
diaryentry.title returns the title
"""

def test_new_entry_title_returned():
    entry = DiaryEntry("Monday", "Today I went to the shops")
    assert entry.title == "Monday"

"""
Given a new Diary Entry is instatiated with a title and contents as strings
diaryentry.contents returns the contents
"""

def test_new_entry_contents_returned():
    entry = DiaryEntry("Monday", "Today I went to the shops")
    assert entry.contents == "Today I went to the shops"

"""
Given a diary entry of 20 words
diaryentry.count_words returns 20
"""

def test_word_count_returned():
    entry = DiaryEntry("Tuesday", "One two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty.")
    assert entry.count_words() == 20

"""
Given a diary entry of 20 words and a wpm of 20
reading_time returns 1
"""

def test_correct_reading_time_simple():
    entry = DiaryEntry("Tuesday", "One two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty.")
    assert entry.reading_time(2) == 10

"""
Given a diary entry of 100 words and a wpm of 20
reading_time returns 5
"""

def test_correct_reading_time_complex():
    entry = DiaryEntry("Tuesday", "One two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty.")
    assert entry.reading_time(3) == 7

"""
When given words per minute and an integer with number of minutes a user has got to read
will return a string with the contents that the user can read in the given number of minutes
"""

def test_first_reading_chunk_returned():
    entry = DiaryEntry("Tuesday", "One two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty.")
    assert entry.reading_chunk(2,4) == "One two three four five six seven eight"

"""
When some of the content has already been read, the next chunk is provided for the user to read in the specified number of minutes
"""

def test_second_reading_chunk_returned():
    entry = DiaryEntry("Tuesday", "One two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty.")
    entry.reading_chunk(2,2)
    assert entry.reading_chunk(2,2) == "five six seven eight"

"""
When there is some content left but less words than the available words that can be read, 
It only returns the remaining words and doesn't wrap back to the start
"""

def test_returns_only_last_section_when_extra_time_given():
    entry = DiaryEntry("Tuesday", "One two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty.")
    entry.reading_chunk(2,4)
    assert entry.reading_chunk(2,12) == "nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty."

"""
Given there is no diary content left and the user asks for the next reading chunk
It returns the chunk that starts from the beginning 
"""

def test_returns_to_start_when_contents_have_been_read():
    entry = DiaryEntry("Tuesday", "One two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty.")
    entry.reading_chunk(2,4)
    entry.reading_chunk(2,12)
    assert entry.reading_chunk(2,3) == "One two three four five six"

"""
Given a wpm of 0
#reading-time throws an error
"""

def test_0_wpm_throws_error():
    entry = DiaryEntry("Tuesday", "One two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty.")
    with pytest.raises(Exception) as e:
        entry.reading_chunk(0,3)
    assert str(e.value) == "wpm can't be 0 or less"

"""
Given a wpm of a negative number
#reading-time throws an error
"""

def test_less_than_0_wpm_throws_error():
    entry = DiaryEntry("Tuesday", "One two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty.")
    with pytest.raises(Exception) as e:
        entry.reading_chunk(-4,3)
    assert str(e.value) == "wpm can't be 0 or less"

"""
Given a diary entry of 0 words
throws error "Entry contents is empty"
"""

def test_empty_entry_throws_error():
    with pytest.raises(Exception) as e:
        DiaryEntry("Tuesday", "")
    assert str(e.value) == "Entry contents is empty"

"""
Given a non string title
throws error "Please submit title as a string"
"""

def test_non_string_title_throws_error():
    with pytest.raises(Exception) as e:
        DiaryEntry(3, "afasfsdfsdf")
    assert str(e.value) == "title must be a string."

"""
Given a non string entry
throws error "Please submit entry as a string"
"""

def test_non_string_contents_throws_error():
    with pytest.raises(Exception) as e:
        DiaryEntry("title", ["afasfsdfsdf"])
    assert str(e.value) == "contents must be a string."