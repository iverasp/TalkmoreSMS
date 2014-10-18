import atom.data
import gdata.data
import gdata.contacts.client
import gdata.contacts.data

import argparse
import json
import os

from talkmoreapi import *

def main():

    config_file = "%s/.talkmore.json" % os.getenv("HOME")
    config = json.loads(open(config_file, 'r').read())

    phonenumber = config["phonenumber"]
    password = config["password"]
    
    t = TalkmoreAPI(phonenumber, password)
    t.login()
    t.send_sms(['98026170'], 'test')

if __name__ == '__main__':
    main()

