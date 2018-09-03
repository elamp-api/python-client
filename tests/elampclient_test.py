import unittest
import operator

from elampclient import eLampClient


class eLampClientTest(unittest.TestCase):

    def test_basic_client(self):
        client = eLampClient('Bearer token')
        #response = client.skills().get("SKI1", test='test') #.list(skill="SKI1")
        #response = client.powers().create(user='U1', skill='SKI1')
        response = client.api_call(method='applications/me/infos', http_method='get', domain='team.elamp.fr/admin/api')
        print(response)
        self.assertEqual(response, False)