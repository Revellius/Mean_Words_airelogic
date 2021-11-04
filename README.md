# Mean_Words_airelogic
Program for airelogic tech test by Philip Richardson

WHAT THIS PROGRAM DOES AND HOW TO RUN
 
Included in this repository there are two files. The first file meanwords.py is a program which can be run from the command line.
When run, it will prompt the user to enter an artist. Once given an artist as an input, it will ask the user if they would like to see the songs included in the calculation, it will then search the genius api for the top 20 entries involving that artist. To run the program enter

python3 meanwords.py

in the terminal.

The second file test_meanwords.py is a program which completes unittests on the functions included in meanwords.py. This can also be run from the command line using 

python3 test_meanwords.py

in the terminal.

LIST OF DEPENDENCIES
To run this program you will need the following python modules:
- sys
- requests
- json
- unittest

DESCRIPTION OF FUNCTIONS IN meanwords.py

choose_artist():

  This prompts the user for an artist. If no artist is given it reprompts the user to input an artist. This can be cancelled by entering "cancel search".

format_artist_name(artist):
  
  Given an artist this formats the name by stripping away excess spaces either side of the artist.
  
get_song_display_flag():
  
  Asks the user whether they would like to see the songs being used in the calculation. If the user enters 'yes' it displays song titles as they are found and if     the user enters 'no' it does not. If the user enters anything which is not 'yes' or 'no' then it reprompts for a valid input.
  
get_song_data(artist):
   
  Given an artist, this function searches the genius.api for the top 20 entries involving that artist. The output is stored as a dictionary.

word_count(song_title):

  Given a song title, this function counts the words in a song title and returns a word count.
  
total_word_and_song_count(data,song_display_flag):

  Given a dictionary of song data and the user's song display flag, this produces the cumulative word count of the song titles in data as well as the number of       songs.
  
display_song_info(w_count,s_count):

  Given a word count and song count, this function either outputs "Sorry, no songs were found" when song count is 0 or a message telling the user how many songs       were used and their total word count.

get_mean_word_count(w_count,s_count):
  
  Given a word count and song count, this function simply divides the word count by the song count to get the mean number of words per song. As this is only called when s!=0 we do not need to include an exception for when s_count=0.
  
KNOWN BUGS AND AREAS FOR FURTHER DEVELOPMENT

- As this program only searches the genius api using the keyword artist input by the user, if a popular song has another artists name in the title that will incorrectly be included as a song by the artist in the calculation.
- Currently this only pulls the top 20 results for a given artist. This could potentially be fixed by first performing a search of the artist, then checking the ids for a consistent value and then calling the api again with an artists id.
- The unittest for get_song_data needs expanding to cover more cases.
