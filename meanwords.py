import sys
import requests

def choose_artist():

    """ This asks the user for an artist, if no artist is chosen it re asks for an input"""
    artist=input('Please input an artist: ')
    while len(artist) == 0:
        artist=input("If you wish to cancel search please type: cancel search \nPlease enter artist: ")
    if artist == 'cancel search':
        sys.exit(2)
    return artist

def format_artist_name(artist_name): 

    """ Function to ensure that extra spaces before and after artist name are ignored """

    artist_name = artist_name.lstrip(' ')
    artist_name = artist_name.rstrip(' ')
    return artist_name

def get_song_display_flag():

    """Asks the user whether they would like to see the songs included in the calculation and checks for valid input of yes or no."""

    flag = input("Would you like to see the songs included in the calculation \nPlease enter yes or no: ")
    while (flag != 'yes' and flag != 'no'):
        flag = input('Please enter yes or no:')
    return flag

def get_song_data(artist):

    """ Use the genius api to search for the first 20 results using keyword artist"""

    client_access_token = 'xYXqMVIXFU75lWHdDR3YU3EuMmsotY-P2gAOsedAQOwmoCsm4_bWL68-fh9iURKl'
    search_term = artist
    genius_search_url = f'http://api.genius.com/search?per_page=20&page=1&q={search_term}&access_token={client_access_token}'
    response = requests.get(genius_search_url)
    data=response.json()
    return data

def word_count(song_title):

    """ Function which gives the total number of words in a given song title"""

    word_list = song_title.split()
    number_of_words = len(word_list)
    return number_of_words

def total_word_and_song_count(data,song_display_flag):

    """ Takes the genius api data and song display flag to produce a total word and song count.
    If the user input yes when prompted for song display information, each song is printed as the words are counted """

    w_count = 0
    s_count = 0
    for song in data['response']['hits']:
        if song_display_flag == 'yes':
            print(song['result']['full_title'])
        w_count = w_count+word_count(song['result']['title'])
        s_count = s_count+1
    return w_count,s_count

def display_song_info(w_count,s_count):

    """ This prints to the user information about the word and song count """
    
    if s_count!=0:
        output_string=f'A total of {s_count} songs used in calculation. The total number of words in the song titles is {w_count}.'
        print(output_string)
    else:
        output_string='Sorry, no songs were found.'
        print(output_string)
    return output_string

def get_mean_word_count(w_count,s_count):

    """ Calculate mean word count in artists songs. If no songs were found return message to user."""

    mean_words = w_count/s_count
    return mean_words

    """ Program to obtain mean words of an artist's songs from their top 20 entries on genius"""
if __name__ == '__main__':
    artist = choose_artist()
    artist = format_artist_name(artist)
    song_display_flag = get_song_display_flag()
    data = get_song_data(artist)
    w_count,s_count = total_word_and_song_count(data,song_display_flag)
    display_song_info(w_count,s_count)
    if s_count != 0:
        mean_words=get_mean_word_count(w_count,s_count)
        print('The mean number of words in song titles by',artist,'is', mean_words)
