import unittest
import random
from app import app

class Apptest(unittest.TestCase):

    num = random.randint(1, 100)

    test_data = {"text": "testing"+str(num),
                 "id": 0}

    #check for response 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
    

    #check UI content
    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get("/")
        html = response.data.decode("utf8")
        self.assertIn("Create a Tweet", html)  
        self.assertIn("Get a Tweet", html)  
        self.assertIn("Deleta a Tweet", html)  

    #test create_tweet respond status_code
    def test_create_tweet1(self):
        tester = app.test_client(self)
        resp = tester.post("/tweet", data="texting")
        self.assertEqual(resp.status_code, 200)
        print("test1 complete")
    
    #test create_tweet respond type
    def test_create_tweet2(self):
        tester = app.test_client(self)
        resp = tester.post("/tweet", data="texting")
        self.assertEqual(resp.content_type, "application/json")
        print("test2 complete")

    #test create_tweet respond output
    def test_create_tweet3(self):
        tester = app.test_client(self)
        resp = tester.post("/tweet", data = "testing")
        self.assertTrue(b'detail'in resp.data)
        print("test3 complete")
    
    #test delete_tweet respond status_code
    def test_delete_tweet1(self):
        tester = app.test_client(self)
        resp = tester.delete("/delete?tweetId=$123")
        self.assertEqual(resp.status_code, 200)
        print("test4 complete")
    
    #test delete_tweet respond type
    def test_delete_tweet2(self):
        tester = app.test_client(self)
        resp = tester.delete("/delete?tweetId=$123")
        self.assertEqual(resp.content_type, "application/json")
        print("test5 complete")

    #test delete_tweet respond output
    def test_delete_tweet3(self):
        tester = app.test_client(self)
        resp = tester.delete("/delete?tweetId=$123")
        self.assertTrue(b'detail'in resp.data)
        print("test6 complete")

    

if __name__=="__main__":
    unittest.main()