#!/usr/bin/env python

from sys import argv
import iaparser

class CmntKiKpl:
    def __init__(self, path):
        self.serializer = iaparser.Serializer(path+'/questions.txt', path+'/responses.txt')
        self.fantome_order = ['rouge', 'blanc', 'noir', 'gris', 'bleu', 'rose', 'violet', 'maron']
        self.inspector_order = ['noir', 'blanc', 'gris', 'rose', 'bleu', 'rouge', 'violet', 'maron']
        self.question = ''
        self.tuile = ''

    def play_personnage(self):
        if self.tuile == '':
            print('no tuil selected')
            return
        if self.tuile == 'rouge':
            self.play_red_personnage()
            return
        if self.tuile == 'blanc':
            self.play_white_personnage()
            return
        if self.tuile == 'noir':
            self.play_black_personnage()
            return
        if self.tuile == 'gris':
            self.play_grey_personnage()
            return
        if self.tuile == 'bleu':
            self.play_blue_personnage()
            return
        if self.tuile == 'rose':
            self.play_pink_personnage()
            return
        if self.tuile == 'violet':
            self.play_purple_personnage()
            return
        if self.tuile == 'maron':
            self.play_brown_personnage()
            return

    def tuile_disponible(self, order):
        i = 0
        while not self.question.__contains__(order[i]) & order.__len__() < i:
            i += 1
        if i == order.len:
            print('[tuile disponible] error no tuile found/matched with order')
            self.tuile = ''
        self.tuile = order[i]
        self.play_personnage()

    def play_ia(self, order):
        self.question = self.serializer.get_question()
        if self.question.content('Tuiles disponibles'):
            self.tuile_disponible(order)

    def play(self):
        print('[cmntkikpl] play : ia play')
        print(self.serializer.serialize().__str__())
        while self.serializer.getFinished():
            if self.serializer.getRole() == 'fantome':
                self.play_ia(self.fantome_order)
            else:
                self.play_ia(self.inspector_order)





ia = CmntKiKpl(argv[1])
ia.play()