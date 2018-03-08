!/usr/bin/env python
import serializer as Serializer

class cmntkikpl:
    def __init__(self, path):
        self.path = path
        self.fantome = ''
        self.role = ''
        self.question = []
        self.personnage = []
        self.bloque = []
        self.tour = 0
        self.score = ''
        self.ombre = 0
        self.info_line = 0

    def get_role(self):
        infof = open(self.path + '/infos.txt', 'r')
        line = infof.readlines()
        infof.close()
        if line[self.info_line].__contains__('**************************'):
            self.role = 'inspecteur'
            self.info_line += 1
            return
        if line[self.info_line].__contains__('!!! Le fantôme est : '):
            self.role = 'fantome'
            self.info_line += 1
            self.fantome = line[self.info_line][len('!!! Le fantôme est : '):]
            self.info_line += 1
            return
        print('no role found !')
        exit()

    def parse_pos(self, elem):
        elem.split('-')

class CmntKiKpl:
    _level = 0

    def update_info(self):
        return

    def fantome_turn(self):
        if self.role != 'fantome':
            self.update_info()
            return

    def inspecteur_turn(self):
        if self.role != 'inspecteur':
            self.update_info()
            return

def main():
    filemanager = FileManager()
    serializer = Serializer.Serializer()
    ia = CmntKiKpl(0)
    linebuffer = filemanager.read_file("test")
    serializer.serialize(linebuffer)

    def start(self):
        fini = False
        self.get_role()
        self.get_context()
        while fini:
            infof = open(self.path + '/infos.txt', 'r')
            line = infof.readlines()
            infof.close()
            self.info_line += 1
            if line[self.info_line].__contains__('Tour de le fantome'):
                self.fantome_turn()
            else:
                self.inspecteur_turn()
            infof = open(self.path + '/infos.txt', 'r')
            lines = infof.readlines(self.info_line)
            self.info_line += 1
            infof.close()
            if len(lines) > 0:
                fini = "Score final" in lines[-1]
        print("partie finie")

cmntkikpl(argv[1]).start()
