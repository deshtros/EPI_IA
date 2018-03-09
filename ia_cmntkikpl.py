#!/usr/bin/env python

from sys import argv
import iaparser

passages = [{1,4},{0,2},{1,3},{2,7},{0,5,8},{4,6},{5,7},{3,6,9},{4,9},{7,8}]
pass_ext = [{1,4},{0,2,5,7},{1,3,6},{2,7},{0,5,8,9},{4,6,1,8},{5,7,2,9},{3,6,9,1},{4,9,5},{7,8,4,6}]

class CmntKiKpl:
    def __init__(self, path):
        self.serializer = iaparser.Serializer(path+'/questions.txt', path+'/responses.txt')
        self.fantome_order = ['rouge', 'blanc', 'noir', 'gris', 'bleu', 'rose', 'violet', 'maron']
        self.inspector_order = ['noir', 'blanc', 'gris', 'rose', 'bleu', 'rouge', 'violet', 'maron']
        self.question = ''
        self.personnage = ''
        self.case_move = -1
        self.case_power = -1

    def player_mov_fantome(self):
        nb = 8
        for i, move in passages[self.serializer.get_movement_position()]:
            nb_in_case = self.serializer._get_nb_personnage_in_case(move)
            if nb > nb_in_case:
                nb = nb_in_case
                self.case_move = move

    def player_mov_inspector(self):
        nb = 0
        for i, move in passages[self.serializer.get_movement_position()]:
            nb_in_case = self.serializer._get_nb_personnage_in_case(move)
            if nb < nb_in_case:
                nb = nb_in_case
                self.case_move = move

    def player_red_personnage(self):
        self.case_power = -1

    def play_personnage_skill(self):
        if self.personnage == '':
            print('no tuil selected')
            return
        if self.personnage == 'rouge':
            self.play_red_personnage()
            return
        if self.personnage == 'blanc':
            self.play_white_personnage()
            return
        if self.personnage == 'noir':
            self.play_black_personnage()
            return
        if self.personnage == 'gris':
            self.play_grey_personnage()
            return
        if self.personnage == 'bleu':
            self.play_blue_personnage()
            return
        if self.personnage == 'rose':
            self.play_pink_personnage()
            return
        if self.personnage == 'violet':
            self.play_purple_personnage()
            return
        if self.personnage == 'maron':
            self.play_brown_personnage()
            return

    def tuile_disponible(self, order):
        i = 0
        self.personnage = ''
        while order.__len__() > i:
            if self.question.__contains__(order[i]):
                if self.personnage == '':
                    self.personnage = order[i]
                if not self.serializer.is_alone(order[i]):
                    self.personnage = order[i]
                    i = order.__len__() - 1
            i += 1
        if self.personnage == '':
            print('[tuile disponible] error no tuile found/matched with order')
        self.serializer.response(self.personnage)

    def play_ia(self, order):
        if self.question == self.serializer.get_question():
            return
        self.question = self.serializer.get_question()
        if self.question.content('Tuiles disponibles'):
            self.tuile_disponible(order)
        if self.serializer.get_role() == 'fantome':
            self.player_mov_fantome()
        else:
            self.player_mov_inspector()
        self.play_persnnage_skill()

    def play(self):
        print('[cmntkikpl] play : ia play')
        print(self.serializer.serialize().__str__())
        while self.serializer.get_finished():
            if self.serializer.get_role() == 'fantome':
                self.play_ia(self.fantome_order)
            else:
                self.play_ia(self.inspector_order)





ia = CmntKiKpl(argv[1])
ia.play()