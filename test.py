import unittest
from unittest.mock import MagicMock, patch
from app import app, make_tweet_fn, delete_tweet_fn
import time

class TestApp(unittest.TestCase):
    '''
    @patch('app.OAuth1Session')
    def test_make_tweet_fn(self, mock_oauth_session):
        mock_response = MagicMock()
        mock_response.status_code = 403  # Change the status code to 403 for a forbidden request
        mock_response.json.return_value = {
            'detail': 'You are not allowed to create a Tweet with duplicate content.',
            'status': 403,
            'title': 'Forbidden',
            'type': 'about:blank'
        }
        mock_oauth_session().post.return_value = mock_response

        text = {'text': 'Test tweet content'}
        response = make_tweet_fn(text)
        expected_response = {
            'detail': 'You are not allowed to create a Tweet with duplicate content.',
            'status': 403,
            'title': 'Forbidden',
            'type': 'about:blank'
        }
        self.assertEqual(response, expected_response)
    '''

    created_id = None
    
    @patch('app.OAuth1Session')
    def test_make_tweet_fn(self, mock_oauth_session):
        # mock_response = MagicMock()
        # mock_response.status_code = 200
        # mock_response.json.return_value = {
        #     "data": {
        #         "edit_history_tweet_ids": ["1702854925385138637"],
        #         "id": "1702854925385138637",
        #         "text": "Test tweet content"
        #     }
        # }
        # mock_oauth_session().post.return_value = mock_response

        text = {'text': 'Test tweet content'}
        response = make_tweet_fn(text)
        # self.created_id = response["data"]["id"]

        print(response)
        print(self.created_id)
        print(type(self.created_id))

        # Check the "text" part of the response
        # expected_text = "Test tweet content"
        # self.assertEqual(response["data"]["text"], expected_text)
    
    time.sleep(5)

    # @patch('app.OAuth1Session')
    # def test_delete_tweet_fn(self, mock_oauth_session):
    #     mock_response = MagicMock()
    #     mock_response.status_code = 200
    #     mock_response.json.return_value = {'success': 'tweet deleted'}
    #     mock_oauth_session().delete.return_value = mock_response

    #     with app.app_context():  # Set up the application context
    #         response = delete_tweet_fn('1702857571139481880')
    #         print(response)
    #         expected_response = {'success': 'tweet deleted'}
    #         self.assertEqual(response, expected_response)

    
if __name__ == '__main__':
    unittest.main()
