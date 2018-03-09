#!/usr/bin/env python

from sys import argv
import iaparser

class CmntKiKpl:
    def __init__(self, level, path):
        self._level = level
        self.serializer = iaparser.Serializer(path+'/questions.txt', path+'/responses.txt')

    def play(self):
        print("[cmntkikpl] play : ia play")
        if self._level == 0:
            self.playlevelz()

    def playlevelz(self):
        print("[cmntkikpl] playlevelz : play level 0")
        print(self.serializer.serialize().__str__())
        if



ia = CmntKiKpl(0, argv[1])
ia.play()