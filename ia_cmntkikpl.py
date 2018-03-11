#!/usr/bin/env python

from sys import argv
import iaparser as Parser
import game as g

passages = [{1,4},{0,2},{1,3},{2,7},{0,5,8},{4,6},{5,7},{3,6,9},{4,9},{7,8}]
pass_ext = [{1,4},{0,2,5,7},{1,3,6},{2,7},{0,5,8,9},{4,6,1,8},{5,7,2,9},{3,6,9,1},{4,9,5},{7,8,4,6}]

class CmntKiKpl:
    def __init__(self, path):
        self.path = path
        serializer = Parser.Serializer(self.path + '/questions.txt', self.path + '/infos.txt', self.path + '/out.txt')
        self.game = g.Game(serializer)
        self.fantome_order = ['rouge', 'blanc', 'noir', 'gris', 'bleu', 'rose', 'violet', 'marron']
        self.inspector_order = ['noir', 'blanc', 'gris', 'rose', 'bleu', 'rouge', 'violet', 'marron']
        self.question = Parser.ServerMessage(Parser.ServerOutputType.NOT_IMPLEMENTED, 0, True) 
        self.personnage = ''
        self.case_move = -1
        self.case_power = -1

    def player_mov_fantome(self):
        case_allow = self.game.get_skill_case_allow()
        nb = 8
        for i, move in case_allow:
            nb_in_case = self.game._get_nb_personnage_in_case(move)
            if nb > nb_in_case:
                nb = nb_in_case
                self.case_move = i
        self.game.write_answer(self.case_power)

    def player_mov_inspector(self):
        case_allow = self.game.get_skill_case_allow()
        nb = 0
        for i in case_allow:
            nb_in_case = self.game._get_nb_personnage_in_case(i)
            if nb < nb_in_case:
                nb = nb_in_case
                self.case_move = i
        self.game.write_answer(self.case_power)

    def play_red_personnage(self):
        case_allow = self.game.get_skill_case_allow()
        self.case_power = -1

    def play_pink_personnage(self):
        case_allow = self.game.get_skill_case_allow()
        self.case_power = -1

    def play_blue_personnage(self):
        self.case_power = 1
        self.game.write_answer(self.case_power)
        wait_for_next question
        self.game.write_answer(self.case_power)
        self.case_power = -1

    def play_grey_personnage(self):
        self.case_power = 1
        if self.game.get_role() == 'fantome':
            p = 0
            for i in 10:
                if self.game._get_nb_personnage_in_case(i) > p:
                    self.case_power = i
                    p = self.game._get_nb_personnage_in_case(i)
        else:
            p = 8
            for i in 10:
                if self.game._get_nb_personnage_in_case(i) < p:
                    self.case_power = i
                    p = self.game._get_nb_personnage_in_case(i)
        self.game.write_answer(self.case_power)
        self.case_power = -1

    def play_black_personnage(self):
        if self.game.get_role() == 'fantome':
            self.case_power = 0
        else:
            self.case_power = 1
        self.game.write_answer(self.case_power)
        self.case_power = -1

    def play_white_personnage(self):
        p = self.game._get_nb_personnage_in_case(i)
        for i in p - 1:
            case_allow = self.game.get_skill_case_allow()
            g = 8
            y = 0
            for y, j in case_allow:
                if self.game._get_nb_personnage_in_case(j) < g:
                    g = self.game._get_nb_personnage_in_case(j)
                    self.case_power = y
            self.game.write_answer(self.case_power)
        self.case_power = -1



    def play_purple_personnage(self):
        case_allow = self.game.get_skill_case_allow()
        self.case_power = -1
        self.game.response('rose')
        self.case_power = -1

    def play_brown_personnage(self):
        case_allow = self.game.get_skill_case_allow()
        self.case_power = case_allow[0]
        self.game.write_answer(self.case_power)
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
            if self.question.content.color == order[i]:
                if self.personnage == '':
                    self.personnage = order[i]
                if not self.game.is_alone(order[i]):
                    self.personnage = order[i]
                    i = order.__len__() - 1
            i += 1
        if self.personnage == '':
            print('[tuile disponible] error no tuile found/matched with order')
        self.game.response(self.personnage)

    def play_ia(self, order):
        if self.question == self.game.get_question():
            return
        self.question = self.game.get_question()
        if self.question.messageType == Parser.ServerOutputType.CHOOSE_CARD_TO_PLAY:
            self.tuile_disponible(order)
        if self.question.messageType == Parser.ServerOutputType.CHOOSE_POSITION:
            if self.game.get_role() == 'fantome':
                self.player_mov_fantome()
            else:
                self.player_mov_inspector()
        if self.question.messageType == Parser.ServerOutputType.ENABLE_POWER:
            self.game.write_answer(1)
            wait_for_next question
            self.play_personnage_skill()

    def play(self):
        print('[cmntkikpl] play : ia play')
        while self.game.get_finished():
            print(self.game)
            if self.game.get_role() == 'fantome':
                self.play_ia(self.fantome_order)
            else:
                self.play_ia(self.inspector_order)





ia = CmntKiKpl(argv[1])
ia.play()
