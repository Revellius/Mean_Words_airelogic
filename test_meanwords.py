import unittest
import meanwords
from unittest.mock import patch,MagicMock
import json

class TestMeanwords(unittest.TestCase):

    def test_format_artist_name(self):

        """ unit tests to check that format artist name behaves as intended"""

        self.assertEqual(meanwords.format_artist_name(' this is a test '),'this is a test')
        self.assertEqual(meanwords.format_artist_name('right test      '),'right test')
        self.assertEqual(meanwords.format_artist_name('       left test'),'left test')

    def test_word_count(self):

        """unit tests to check that the word_count function behaves correctly"""
        
        self.assertEqual(meanwords.word_count(''),0)
        self.assertEqual(meanwords.word_count('This sentence has five words'),5)
        

    
    @patch('builtins.input', side_effect=['','','Hello World'])
    def test_choose_artist(self,mock_input):

        """ unit test to check that the behaviour of choose_artist is correct given a  series of bad inputs."""

        result = meanwords.choose_artist()
        self.assertEqual(result,'Hello World')
    
    @patch('builtins.input', side_effect=['','Yes','','No','yes'])
    def test_get_song_display_flag_1(self,mock_input):

        """ unit test to check that the behaviour of get_song_display_flag is correct given a series of bad inputs."""

        result = meanwords.get_song_display_flag()
        self.assertEqual(result,'yes')

    @patch('builtins.input', side_effect=['YES','','','NO','nO','no'])
    def test_get_song_display_flag_2(self,mock_input):

        """ unit test to check that the behaviour of get_song_display_flag is correct given a series of bad inputs."""

        result = meanwords.get_song_display_flag()
        self.assertEqual(result,'no')

    @patch('meanwords.get_song_data')
    def test_get_song_data1(self,mock_api_call):
            """ unit test to check that a successful api call is made"""
            mock_api_call.return_value.ok = MagicMock(status_code=200,response=json.dumps({'key':'value'}))
            data=meanwords.get_song_data('Dido')
            self.assertTrue(data,True)

    @patch('meanwords.get_song_data')
    def test_get_song_data2(self,mock_api_call):
            """ unit test to check that an unsuccessful api call is made"""
            mock_api_call.return_value.ok = MagicMock(status_code=404,response=[])
            data=meanwords.get_song_data('Dido')
            self.assertTrue(data,True)

    def test_display_song_info(self):
        """ unit test to check that display_song_info behaves correctly"""
        self.assertEqual(meanwords.display_song_info(10,3),'A total of 3 songs used in calculation. The total number of words in the song titles is 10.')
        self.assertEqual(meanwords.display_song_info(0,0),'Sorry, no songs were found.')
    
    def test_get_mean_word_count(self):
        """ unit tests to check that get_mean_word_count behaves correctly"""
        self.assertEqual(meanwords.get_mean_word_count(6,3),2)
        self.assertEqual(meanwords.get_mean_word_count(7,2),3.5)
   



if __name__== '__main__':
    unittest.main()