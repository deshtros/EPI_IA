from enum import Enum

passages = [{1,4},{0,2},{1,3},{2,7},{0,5,8},{4,6},{5,7},{3,6,9},{4,9},{7,8}]
pass_ext = [{1,4},{0,2,5,7},{1,3,6},{2,7},{0,5,8,9},{4,6,1,8},{5,7,2,9},{3,6,9,1},{4,9,5},{7,8,4,6}]

CHOOSE_CARD_TO_PLAY_SERVER_ASK = ["Tuiles", "disponibles"]
ENABLE_POWER_SERVER_ASK = ["activer","le","pouvoir"]
CHOOSE_POSITION_SERVER_ASK = ["positions","disponibles"]
CHOOSE_COLOR_SERVER_ASK = ["Avec" "quelle" "couleur" "échanger"]

SERVER_ASK_WORD_ARRAY = [CHOOSE_CARD_TO_PLAY_SERVER_ASK, ENABLE_POWER_SERVER_ASK, CHOOSE_POSITION_SERVER_ASK, CHOOSE_COLOR_SERVER_ASK]

class ServerOutputType(Enum):
    CHOOSE_CARD_TO_PLAY = 0
    ENABLE_POWER = 1
    CHOOSE_POSITION = 2
    CHOOSE_COLOR = 3
    NOT_IMPLEMENTED = 4


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
        return "[ServerMessage] content: " + str(self.content) + " messageType: " + str(self.messageType) 




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
    if possibleServerOutput == CHOOSE_CARD_TO_PLAY_SERVER_ASK:
        return ServerOutputType.CHOOSE_CARD_TO_PLAY
    else:
        return ServerOutputType.NOT_IMPLEMENTED

def serverOutputToServerMessage(line):
    serverMessage = ServerMessage(ServerOutputType.NOT_IMPLEMENTED, 0, True) 
    for  serverAskArray in SERVER_ASK_WORD_ARRAY:
        if checkLineWith(serverAskArray, line) == True:
            serverOutput = serverOutputWordToENum(serverAskArray)
            if serverOutput == ServerOutputType.CHOOSE_CARD_TO_PLAY:
                serverMessage = ServerMessage(ServerOutputType.CHOOSE_CARD_TO_PLAY, getTilePosFromLine(line), True)
    return serverMessage 






class Serializer:

    def __init__(self,serverOutputFilePath, serverInputfilePath):
        self.serverOutputFilePath = serverOutputFilePath
        self.serverInputfilePath = serverInputfilePath





    def serialize(self):
        print("[serializer] serialize : start serialize")
        serverMessageArray = []
        f = open(self.serverOutputFilePath, 'r')
        for line in f.readlines():
            serverMessageArray.append(serverOutputToServerMessage(line))
        return serverMessageArray
            
    
    def serverMessageToServerInput(self, serverMessage):
        if serverMessage.messageType == ServerOutputType.CHOOSE_CARD_TO_PLAY:
            self.writeNumberResponse(serverMessage.content)
        else:
            self.writeNumberResponse(0)    

    def writeNumberResponse(self, number):
        rf = open(self.serverInputfilePath,'w')
        rf.write(str(number))
        rf.close()



    def deserialize(self, serverMessage):
        print("[deserialize] deserialize : start deserialize")
        self.serverMessageToServerInput(serverMessage)