#!/usr/bin/env python
from sys import argv
import iaparser as Parser

passages = [{1,4},{0,2},{1,3},{2,7},{0,5,8},{4,6},{5,7},{3,6,9},{4,9},{7,8}]
pass_ext = [{1,4},{0,2,5,7},{1,3,6},{2,7},{0,5,8,9},{4,6,1,8},{5,7,2,9},{3,6,9,1},{4,9,5},{7,8,4,6}]

class Game:
    def __init__(self, serializer):
        self.serializer = serializer
        self.fantome = ''
        self.role = ''
        self.question = Parser.ServerMessage(Parser.ServerOutputType.NOT_IMPLEMENTED, 0, True) 
        self.personnage = []
        self.bloque = []
        self.tour = 0
        self.score = ''
        self.ombre = 0
        self.info_line = 0

    def _get_nb_personnage_in_case(self,caseNumber):
        return 0
    def get_question(self):
        return self.question
    
    def get_role(self):
        return 'fantome'

    def get_finished(self):
        infosMessage = self.serializer.serializeInfosFile()
        questionMessage = self.serializer.serializeQuestionFile
        if infosMessage.messageType == Parser.ServerOutputType.END_GAME:
            return False
        else:
            return True

    def get_skill_case_allow(self):
        return [0]

    def is_alone(color):
        return false

    def write_answer(self, number):
        self.serializer.writeNumberResponse(number)

    def response(self, colorString):
        self.serializer.writeStringResponse(colorString)


