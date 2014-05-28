# !/usr/bin/env python
# encoding=utf-8

# very simple example which constructs a table with three elements and randomly generates
# three numbers in the range 0..10, 0..5, 0..20 with means at

import sys

from streamdrill import StreamDrillClient


class StreamDrillUpdater:
    def __init__(self, trend={'name': 'my_trend', 'columns': 'hashtag'}):
        self.trend = trend
        # trend = { 'name': 'my_trend', 'columns': ['hashtag']}
        client = StreamDrillClient("http://localhost:9669")
        client.delete(self.trend['name'])
        client.create(self.trend['name'], self.trend['columns'], 1000, ("hour", "minute", "second"))
        self.stream = client.stream()

    def update(self, element):
        self.stream.update(self.trend['name'], [element])

    def close(self):
        self.stream.close()
