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
        self.question = Parser.ServerMessage(Parser.ServerOutputType.NOT_IMPLEMENTED, [], True)
        self.characterArray = []
        self.waysLockedArray = []
        self.turn = 0
        self.score = 0
        self.shadowRoom = 0
        self.info_line = 0
        self.isEndGame = False
        self.isGhost = False
        self.ghostColor = ''

    def __repr__(self):
        return "Tour:" + str(self.turn) + ", Score:" + str(self.score) + "/22, Ombre:" + str(self.shadowRoom) + ", Bloque:" + str(self.waysLockedArray) + " | question " + str(self.question) + "\n"


    def _get_nb_personnage_in_case(self,caseNumber):
        nb = 0
        for character in self.characterArray:
            if character.position == caseNumber:
                nb = nb + 1
        return nb

    def get_question(self):
        return self.question
    
    def get_role(self):
        if self.isGhost == True:
            return 'fantome'
        else:
            return ''

    def processInfosMessage(self, message):
        if message.messageType == ServerOutputType.GHOST_ROLE:
            self.isGhost = True
            self.ghostColor = message.content
        elif message.messageType == ServerOutputType.TURN_INDICATION:
            pass
        elif message.messageType == ServerOutputType.TURN_INFO:
            self.turn = message.content.turnNumber
            self.score = message.content.score
            self.waysLockedArray =  message.content.waysLockedArray
            self.shadowRoom = message.content.placeWithShadow
        elif message.messageType == ServerOutputType.END_GAME:
            self.isEndGame = True
            
        
    def get_finished(self):
        infosMessage = self.serializer.serializeInfosFile()
        self.question = self.serializer.serializeQuestionFile()
        if infosMessage.messageType == Parser.ServerOutputType.END_GAME:
            return False
        else:
            return True

    def get_skill_case_allow(self):
        return self.question.content

    def colorToPosition(self, color):
        for character in self.characterArray:
            if character.color == color:
                return character.position


    def is_alone(self, color):
        characterPosition = self.colorToPosition(color)
        if self._get_nb_personnage_in_case(characterPosition) == 1:
            return True
        return False

    def write_answer(self, number):
        self.serializer.writeNumberResponse(number)

    def playCharacter(self, color):
          i = 0
          for character in self.characterArray:
            if character.color == color:
                self.write_answer(i)
            i = i + 1

    def response(self, colorString):
        self.serializer.writeStringResponse(colorString)


