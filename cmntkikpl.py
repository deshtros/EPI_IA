#!/usr/bin/env python
from sys import argv

passages = [{1,4},{0,2},{1,3},{2,7},{0,5,8},{4,6},{5,7},{3,6,9},{4,9},{7,8}]
pass_ext = [{1,4},{0,2,5,7},{1,3,6},{2,7},{0,5,8,9},{4,6,1,8},{5,7,2,9},{3,6,9,1},{4,9,5},{7,8,4,6}]

class cmntkikpl:
    def __init__(self, path):
        self.path = path
        self.fantome = ''
        self.role = ''
        self.question = {}
        self.personnage = {}
        self.suspe = {}
        self.Bloque = {}

    def get_role(self):
        infof = open(self.path + '/info.txt', 'r')
        line = infof.readline()
        infof.close()
        if line == '**************************':
            self.role = 'inspecteur'
            return
        if line.__contains__('!!! Le fantôme est : '):
            self.role = 'fantome'
            self.fantome = line[len('!!! Le fantôme est : '):]
            line = infof.readline()
            return
        print('no role found !')
        exit()

    def get_context(self):
        infof = open(self.path + '/info.txt', 'r')
        lines = infof.readlines()
        infof.close()
        self.Bloque += lines[lines.:]
        infof = open(self.path + '/info.txt', 'r')
        lines = infof.readlines()
        infof.close()

    def get_question(self):
        qf = open(self.path + '/questions.txt', 'r')
        lines = qf.readlines()
        qf.close()
        self.question = lines

    def write_response(self):
        rf = open(self.path + '/reponses.txt', 'w')

    def start(self):
        fini = False
        self.get_role()
        self.get_context()
        while fini:
            self.get_question()
            self.write_response()
            infof = open(self.path + '/info.txt', 'r')
            lines = infof.readlines()
            infof.close()
            if len(lines) > 0:
                fini = "Score final" in lines[-1]
        print("partie finie")

cmntkikpl(argv[0]).start()