# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


import requests
import urllib


HEADERS = {
    "Content-type": "application/x-www-form-urlencoded",
    "Accept": "text/plain",
    "User-Agent": "python"
}


class Client(object):

    def __init__(self, endpoint, username, password):
        self.endpoint = endpoint
        self.username = username
        self.password = password

    def grant_tgt(self):
        url = self.endpoint + '/v1/tickets'
        user = {'username': self.username, 'password': self.password}
        resp = requests.post(url, data=urllib.urlencode(user), headers=HEADERS)
        if resp.status_code != requests.codes.created:
            raise resp.raise_for_status()
        return resp.text

    def grant_st(self, service):
        url = self.endpoint + '/v1/tickets/%s' % self.grant_tgt()
        params = {'service': service}
        resp = requests.post(url,
                             data=urllib.urlencode(params),
                             headers=HEADERS)
        if resp.status_code != requests.codes.ok:
            print resp.text
            raise resp.raise_for_status()
        return resp.text
