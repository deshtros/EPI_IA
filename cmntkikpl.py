#!/usr/bin/env python
from sys import argv

passages = [{1,4},{0,2},{1,3},{2,7},{0,5,8},{4,6},{5,7},{3,6,9},{4,9},{7,8}]
pass_ext = [{1,4},{0,2,5,7},{1,3,6},{2,7},{0,5,8,9},{4,6,1,8},{5,7,2,9},{3,6,9,1},{4,9,5},{7,8,4,6}]

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

    def get_context(self):
        infof = open(self.path + '/infos.txt', 'r')
        line = infof.readlines()
        infof.close()
        lineparsed = line[self.info_line].split(' ')
        self.tour = lineparsed[0].split(':')[1]
        self.score = lineparsed[1].split(':')[1]
        self.ombre = lineparsed[2].split(':')[1]
        self.bloque = line[self.info_line].split(':')[4]
        self.info_line += 1
        self.personnage = line[self.info_line].split(' ')
        self.info_line += 1

    def get_question(self):
        qf = open(self.path + '/questions.txt', 'r')
        lines = qf.readlines()
        qf.close()
        self.question = lines

    def write_response(self):
        rf = open(self.path + '/reponses.txt', 'w')
        rf.close()

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