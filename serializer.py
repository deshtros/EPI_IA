from enum import Enum

passages = [{1,4},{0,2},{1,3},{2,7},{0,5,8},{4,6},{5,7},{3,6,9},{4,9},{7,8}]
pass_ext = [{1,4},{0,2,5,7},{1,3,6},{2,7},{0,5,8,9},{4,6,1,8},{5,7,2,9},{3,6,9,1},{4,9,5},{7,8,4,6}]

CHARACTER_INFOS_SERVER_INFO = ["Tuiles", "disponibles"]
ENABLE_POWER_SERVER_ASK = ["activer","le","pouvoir"]
CHOOSE_POSITION_SERVER_ASK = ["positions","disponibles"]
CHOOSE_COLOR_SERVER_ASK = ["Avec" "quelle" "couleur" "échanger"]

POSSIBLE_SERVER_OUTPUT = [CHARACTER_INFOS_SERVER_INFO, ENABLE_POWER_SERVER_ASK, CHOOSE_POSITION_SERVER_ASK, CHOOSE_COLOR_SERVER_ASK]

class ServerOutput(Enum):
    CHARACTER_INFOS = 0
    ENABLE_POWER = 1
    CHOOSE_POSITION = 2
    CHOOSE_COLOR = 3


class Character:
    def __init__(self,color):
        self.color = color
        self.isSuspected = True
        self.position = 0 
        self.canUseIsPower = True
    def __repr__(self):
        susp = "-suspect" if self.isSuspected else "-clean"
        return self.color + "-" + str(self.position) + susp

class ServerMessage:
    def __init__(self,messageType, content, shouldSendResponse):
        self.content = content
        self.messageType = messageType
        self.shouldSendResponse = shouldSendResponse
        
    def __repr__(self):
        return "[ServerMessage] " + str(self.content) 


def characterFronString(line):
    infoArray = line.split("-")
    character = Character(infoArray[0])
    character.position = int(infoArray[1])
    character.isSuspected = False
    if infoArray[2] == 'suspect':
        character.isSuspected = True
    return character

def getTilePosFromLine(line):
        if "Tuiles" in line and "disponibles" in line :
            line = line.split('[')[1]
            line = line.split(']')[0]
            cards = line.split(", ")
            characters = []
            for card in cards :
                characters.append(characterFronString(card))
            return characters

def checkLineWith(serverOutput, line):
    for word in serverOutput:
        if not word in line:
            return False
    return True

def serverOutputWordToENum(possibleServerOutput):
    if possibleServerOutput == CHARACTER_INFOS_SERVER_INFO:
        return ServerOutput.CHARACTER_INFOS

def serverOutputToServerMessage(line):
    for  element in POSSIBLE_SERVER_OUTPUT:
        if checkLineWith(element, line) == True:
            serverOutput = serverOutputWordToENum(element)
            if serverOutput == ServerOutput.CHARACTER_INFOS:
                serverMessage = ServerMessage(ServerOutput.CHARACTER_INFOS, getTilePosFromLine(line), False)
                return serverMessage 




class Serializer:
    def serialize(self, linebuffer):
        print("[serializer] serialize : start serialize")
        for line in linebuffer:
            print(serverOutputToServerMessage(line))
            
    
        


    def deserialize(self, linebuffer):
        print("[deserialize] deserialize : start deserialize")
        for line in linebuffer:
            print(line)