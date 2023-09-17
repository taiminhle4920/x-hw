import unittest
import random
from app import app
import json

#code by Haoming
class Apptest(unittest.TestCase):

    test_data = {"text": "tweet"+str(random.randint(1, 10000)),
                  "id": 0}

 #check for response 200
    def test_homepage_(self):
        tester = app.test_client(self)
        response = tester.get("/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        print("test homepage complete")

    #tweet empty text
    def test_create_tweet_api_1(self):
        tester = app.test_client(self)
        resp = tester.post("/tweet", data="")
        resp_json = json.loads(resp.data.decode('utf-8'))
        self.assertEqual("content is empty", resp_json["error"])
        print("create test case 1 complete")

    #tweet random text
    def test_create_tweet_api_2(self):
        tester = app.test_client(self)
        resp = tester.post("/tweet", data='text='+self.test_data['text'])
        resp_json = json.loads(resp.data.decode('utf-8')) 
        self.assertEqual(self.test_data['text'], resp_json['data']['text'])
        self.test_data["id"] = resp_json['data']["id"]
        print("create test case 2 complete")
    
    #delete empty id
    def test_delete_tweet_api_1(self):
        tester = app.test_client(self)
        resp = tester.delete("/delete?tweetId=")
        resp_json = json.loads(resp.data.decode('utf-8'))
        self.assertEqual("tweetId is empty", resp_json["error"])
        print("delete test case 1 complete")
    
    #delete wrong id
    def test_delete_tweet_api_2(self):
        tester = app.test_client(self)
        resp = tester.delete("/delete?tweetId=$100")
        resp_json = json.loads(resp.data.decode('utf-8'))
        self.assertEqual("tweetID not found", resp_json["error"])
        print("delete test case 2 complete")
    
    #delete existing id
    def test_delete_tweet_api_3(self):
        tester = app.test_client(self)
        delete_id = self.test_data['id']
        resp = tester.delete("/delete?tweetId="+str(delete_id))
        resp_json = json.loads(resp.data.decode('utf-8'))
        self.assertEqual("tweet deleted", resp_json["success"])
        print("delete test case 3 complete")

    
if __name__=="__main__":
    unittest.main()
