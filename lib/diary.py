import math

class Diary:
    def __init__(self):
        self.entries = []

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        self.entries.append(entry)

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        pass

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        return sum(entry.count_words() for entry in self.entries)

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        return sum(entry.reading_time(wpm) for entry in self.entries)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        difference = None
        entry_to_read = []

        for entry in self.entries:
            reading_time = entry.reading_time(wpm)
            if reading_time <= minutes:
                if difference == None or (minutes - reading_time) < difference:
                    difference = minutes - reading_time
                    entry_to_read = [entry]
                elif (minutes - reading_time) == difference:
                    entry_to_read.append(entry)
                else:
                    continue
        if entry_to_read == []:
            raise Exception("No entry available.")
        else:
            return entry_to_read
                
        
        


# File: lib/diary_entry.py

class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings

        self.validate_input("title", title)
        self.validate_input("contents", contents)

        self.title = title
        self.contents = contents
        self.words = contents.split()
        self.words_read = 0
        
    def validate_input(self, field_name, value):
        if not isinstance(value, str):
            raise Exception(f"{field_name} must be a string.")
        if value == "":
            raise Exception(f"Entry {field_name} is empty")

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in the contents
        return len(self.words)

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        return math.ceil(self.count_words() / wpm)

    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
        if wpm <= 0:
            raise Exception("wpm can't be 0 or less")
        
        words_to_read = wpm * minutes

        if self.words_read >= len(self.words):
            self.words_read = 0

        if self.words_read == 0:
            chunk = ' '.join(self.words[:words_to_read])
            self.words_read += words_to_read
            return chunk
        else:
            chunk = ' '.join(self.words[self.words_read: self.words_read + words_to_read])
            self.words_read += words_to_read
            return chunk
            
# diary = Diary()
# entry_one = DiaryEntry("Monday", "I worked again.")
# entry_two = DiaryEntry("Tues", "I ate a ham sandwich and went to the park.")
# entry_three = DiaryEntry("Weds", "I ate a sandwich again.")
# diary.add(entry_one)
# diary.add(entry_two)
# diary.add(entry_three)
# diary.find_best_entry_for_reading_time(2,6)