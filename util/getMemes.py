#!/usr/bin/env python3
import requests
import os
# import json


API_URL = 'https://api.imgflip.com/get_memes'


class Memes:

    def __init__(self):

        # could probably find a way to do this in a functional manner
        self.memes = self.get_memes()
        self.memes = self.get_array_of_memes()

    def get_memes(self):
        return requests.get(API_URL).json()

    def get_array_of_memes(self):
        return [{'description': meme['name'], 'url': meme['url']} for meme in self.memes['data']['memes']]

    def download_templates(self):

        utilfolder = os.path.dirname(os.path.abspath(__file__))
        projectroot = os.path.abspath(os.path.join(utilfolder, '..'))
        trainingdatafolder = os.path.abspath(
            os.path.join(projectroot, 'trainingdata'))

        for meme in self.memes:
            memedirectory = os.path.join(
                trainingdatafolder, meme['description'])

            if not os.path.exists(memedirectory):
                os.makedirs(memedirectory)
                r = requests.get(meme['url'], stream=True)
                with open(os.path.join(memedirectory, 'template.jpg'), 'wb') as fd:
                    for chunk in r.iter_content(chunk_size=128):
                        fd.write(chunk)
             # endif


if __name__ == "__main__":
    import pprint

    memes = Memes()
    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(memes.get_array())

    memes.download_templates()
