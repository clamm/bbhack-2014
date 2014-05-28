# vim: set fileencoding=utf-8 :
#
# Copyright (c) 2013 Daniel Truemper <truemped at googlemail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
from __future__ import (absolute_import, division, print_function,
                        with_statement)

import logging
import operator

from stemming.porter2 import stem

from bbhack.base import BaseListener


LOG = logging.getLogger(__name__)

termFreq = {}
counter = 0
maxLen = 100


class HashTagLogger(BaseListener):
    def __init__(self, zmq_sub_string, channel):
        super(HashTagLogger, self).__init__(zmq_sub_string, channel)

    def addToDict(self, tag):
        tag = tag.lower()
        tag = stem(tag)

        if tag in termFreq.keys():
            termFreq[tag] += 1
        else:
            if len(termFreq) > maxLen:
                sortedTermFreq = sorted(termFreq.iteritems(), key=operator.itemgetter(1), reverse=True)
                last = sortedTermFreq[-1]

                print ("removing " + str(last))
                del termFreq[last[0]]
                termFreq[tag] = last[1] + 1
            else:
                termFreq[tag] = 1


        sortedTermFreq = sorted(termFreq.iteritems(), key=operator.itemgetter(1), reverse=True)

        print(sortedTermFreq)



    def on_msg(self, tweet):

        if 'entities' in tweet and 'hashtags' in tweet['entities']:
            tags = tweet['entities']['hashtags']
            for tag in tags:
                elem = tag['text']
                self.addToDict(elem)

        return


def main():
    """Start the HashTagLogger."""

    import argparse

    p = argparse.ArgumentParser()
    p.add_argument('--zmq_sub_string', default='tcp://*:5556')
    p.add_argument('--channel', default='tweet.stream')

    options = p.parse_args()

    stream = HashTagLogger(options.zmq_sub_string, options.channel)
    # this call will block
    stream.start()
