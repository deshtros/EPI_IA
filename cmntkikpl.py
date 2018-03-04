#!/usr/bin/env python


class FileManager:
    def read_file(self, filename):
        print("[FileManager] read_file : open file " + filename)
        with open(filename) as f:
            _content = f.readlines()
        return _content

    def write_file(self, filename, linebuffer):
        print("[FileManager] write_file : open file " + filename)
        file = open(filename, "w")
        for line in linebuffer:
            file.write(line)
        file.close()


class Serializer:
    def serialize(self, linebuffer):
        print("[serializer] serialize : start serialize")
        for line in linebuffer:
            print(line)

    def deserialize(self, linebuffer):
        print("[deserialize] deserialize : start deserialize")
        for line in linebuffer:
            print(line)

class CmntKiKpl:
    _level = 0

    def __init__(self, level):
        self._level = level

    def play(self):
        print("[cmntkikpl] play : ia play")
        if self._level == 0:
            self.playlevelz()

    def playlevelz(self):
        print("[cmntkikpl] playlevelz : play level 0")

def main():
    filemanager = FileManager()
    serializer = Serializer()
    ia = CmntKiKpl(0)
    linebuffer = filemanager.read_file("test")
    serializer.serialize(linebuffer)

if __name__ == "__main__":
    main()