from lib.diary import Diary, DiaryEntry

"""
Given a new Diary Entry is instatiated with a title and contents as strings
diaryentry.title returns the title
"""

"""
Given a new Diary Entry is instatiated with a title and contents as strings
diaryentry.contents returns the contents
"""

"""
Given a diary entry of 20 words
diaryentry.count_words returns 20
"""

"""
Given a diary entry of 5 words
diaryentry.count_words returns 5
"""

"""
Given a diary entry of 20 words and a wpm of 20
reading_time returns 1
"""

"""
Given a diary entry of 100 words and a wpm of 20
reading_time returns 5
"""

"""
When given words per minute and an integer with number of minutes a user has got to read
will return a string with the contents that the user can read in the given number of minutes
"""

"""
When some of the content has already been read, the next chunk is provided for the user to read in the specified number of minutes
"""

"""
When there is some content left but less words than the available words that can be read, 
It only returns the remaining words and doesn't wrap back to the start
"""

"""
Given there is no diary content left and the user asks for the next reading chunk
It returns the chunk that starts from the beginning 
"""

"""
Given a wpm of 0
#reading-time throws an error
"""

"""
Given a wpm of a negative number
#reading-time throws an error
"""


"""
Given a diary entry of 0 words
throws error "Entry contents is empty"
"""
