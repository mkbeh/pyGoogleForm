# -*- coding: utf-8 -*-
import time

import requests

from libs.pymongodb import pymongodb
from libs import decorators
from libs import utils


class AddNewPosts(object):
    def __init__(self):
        self.mongo = pymongodb.MongoDB('btt')
        self.documents = self.mongo.find({}, 'en_altcoins')
        self.form_url = ''
        self.client = requests.sessions.Session()

    @decorators.log
    def send_data(self, *args):
        time.sleep(2)

        params = {
            'entry.150819782': args[0],
            'entry.1803166929': args[1],
            'entry.750777297': args[2],
        }

        r = self.client.post(self.form_url, params)
        template = f'[STATUS CODE] {r.status_code} [POST TITLE] {args[0]}'

        return template

    def run(self):
        for document in self.documents:
            self.send_data(document['title'], document['link'], document['topic_started_date'])


if __name__ == '__main__':
    try:
        AddNewPosts().run()
    except:
        utils.logger('Success status: %s' % 'ERROR', 'script.log')
