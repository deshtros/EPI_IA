from enum import Enum

passages = [{1,4},{0,2},{1,3},{2,7},{0,5,8},{4,6},{5,7},{3,6,9},{4,9},{7,8}]
pass_ext = [{1,4},{0,2,5,7},{1,3,6},{2,7},{0,5,8,9},{4,6,1,8},{5,7,2,9},{3,6,9,1},{4,9,5},{7,8,4,6}]

CHOOSE_CARD_TO_PLAY_SERVER_ASK = ["Tuiles", "disponibles"]
ENABLE_POWER_SERVER_ASK = ["activer","le","pouvoir"]
CHOOSE_POSITION_SERVER_ASK = ["positions","disponibles"]
CHOOSE_COLOR_SERVER_ASK = ["Avec" "quelle" "couleur" "échanger"]
GHOST_ROLE_INDICATION = ["!!!", "Le fantôme", "est"]
TURN_SERVER_SAY = ["Tour", "de"]
TURN_INFO_SERVER_SAY = ["Tour:", "Score:", "Ombre:", "Bloque:"]
CHOOSE_ROOM_TO_BLOCK_SERVER_ASK = ["Quelle", "salle", "bloquer"]
CHOOSE_EXIT_FROM_ROOM_TO_BLOCK_SERVER_ASK = ["Quelle", "sortie", "Chosir", "parmi"]
CHOOSE_ROOM_TO_SHADOW_SERVER_ASK = ["Quelle", "salle", "obscurcir" ] 

SERVER_ASK_WORD_ARRAY = [CHOOSE_CARD_TO_PLAY_SERVER_ASK, ENABLE_POWER_SERVER_ASK, CHOOSE_POSITION_SERVER_ASK, CHOOSE_COLOR_SERVER_ASK,TURN_SERVER_SAY, TURN_INFO_SERVER_SAY, CHOOSE_ROOM_TO_BLOCK_SERVER_ASK, CHOOSE_EXIT_FROM_ROOM_TO_BLOCK_SERVER_ASK, CHOOSE_ROOM_TO_SHADOW_SERVER_ASK]

class ServerOutputType(Enum):
    CHOOSE_CARD_TO_PLAY = 0
    ENABLE_POWER = 1
    CHOOSE_POSITION = 2
    CHOOSE_COLOR = 3
    TURN_INDICATION = 4
    TURN_INFO = 5
    CHOOSE_ROOM_TO_BLOCK = 6
    CHOOSE_EXIT_FROM_ROOM_TO_BLOCK = 7
    CHOOSE_ROOM_TO_SHADOW = 8
    NOT_IMPLEMENTED = 9

class ServerInputType(Enum):
    CHOOSE_CARD_TO_PLAY = 0
    ENABLE_POWER = 1
    CHOOSE_POSITION = 2
    CHOOSE_COLOR = 3
    CHOOSE_ROOM_TO_BLOCK = 4
    CHOOSE_EXIT_FROM_ROOM_TO_BLOCK = 5
    CHOOSE_ROOM_TO_SHADOW = 6
    NOT_IMPLEMENTED = 7

class Character:
    def __init__(self,color):
        self.color = color
        self.isSuspected = True
        self.position = 0 
        self.canUseIsPower = True
    def __repr__(self):
        susp = "-suspect" if self.isSuspected else "-clean"
        return self.color + "-" + str(self.position) + susp

class TurnInfo:
    def __init__(self, turnNumber, score, placeWithShadow, waysLockedArray):
        self.turnNumber = turnNumber
        self.score = score
        self.waysLockedArray = waysLockedArray
        self.placeWithShadow = placeWithShadow

    def __repr__(self):
        return "Tour:" + str(self.turnNumber) + ", Score:" + str(self.score) + "/22, Ombre:" + str(self.placeWithShadow) + ", Bloque:" + str(self.waysLockedArray)


class ServerMessage:
    def __init__(self,messageType, content, shouldSendResponse):
        self.content = content
        self.messageType = messageType
        self.shouldSendResponse = shouldSendResponse
        
    def __repr__(self):
        return "[ServerMessage] content: " + str(self.content) + " messageType: " + str(self.messageType) + '\n'

class iAMessage:
    def __init__(self, messageType, content, shouldSendResponse):
        self.content = content
        self.messageType = messageType
        
    def __repr__(self):
        return "[IAMessage] content: " + str(self.content) + " messageType: " + str(self.messageType) + '\n'



def characterFronString(line):
    infoArray = line.split("-")
    character = Character(infoArray[0])
    character.position = int(infoArray[1])
    character.isSuspected = False
    if infoArray[2] == 'suspect':
        character.isSuspected = True
    return character

def getTilePosFromLine(line):
        if "Tuiles" in line and "disponibles" in line:
            line = line.split('[')[1]
            line = line.split(']')[0]
            cards = line.split(", ")
            characters = []
            for card in cards :
                characters.append(characterFronString(card))
            return characters

def getPlayerToPlayFromLine(line):
    if TURN_SERVER_SAY[0] in line and TURN_SERVER_SAY[1] in line:
         words = line.split(" ")
         characterName = words[-1].rstrip()
         return characterName

def getTurnInfofromLine(line):
    if TURN_INFO_SERVER_SAY[0] in line and TURN_INFO_SERVER_SAY[1] in line:
        words = line.split(":")
        
        turn = words[1]
        turn = int(turn.split(", ")[0])
        
        score = words[2]
        score = int(score.split("/")[0])

        shadow = words[3]
        shadow = int(shadow.split(", ")[0])

        wayBloqued = []
        wayBloquedString = words[4]
        wayBloquedString = wayBloquedString.split("{")[1]
        wayBloquedString = wayBloquedString.split("}")[0]
        wayBloquedString = wayBloquedString.split(", ")
        for numberString in wayBloquedString:
            wayBloqued.append(int(numberString))
        return TurnInfo(turn, score, shadow, wayBloqued)


def getPositionFromLine(line):
    positions = []
    line = line.split("{")[1]
    line = line.split("}")[0]
    numberStringArray = line.split(", ")
    for numberString in numberStringArray:
        positions.append(int(numberString))
    return positions

def checkLineWith(serverOutput, line):
    for word in serverOutput:
        if not word in line:
            return False
    return True


def serverOutputWordToENum(possibleServerOutput):
    if possibleServerOutput == CHOOSE_CARD_TO_PLAY_SERVER_ASK:
        return ServerOutputType.CHOOSE_CARD_TO_PLAY
    elif possibleServerOutput == TURN_SERVER_SAY:
        return ServerOutputType.TURN_INDICATION
    elif possibleServerOutput == TURN_INFO_SERVER_SAY:
        return ServerOutputType.TURN_INFO
    elif possibleServerOutput == ENABLE_POWER_SERVER_ASK:
        return ServerOutputType.ENABLE_POWER
    elif possibleServerOutput == CHOOSE_POSITION_SERVER_ASK:
        return ServerOutputType.CHOOSE_POSITION
    elif possibleServerOutput == CHOOSE_ROOM_TO_BLOCK_SERVER_ASK:
        return ServerOutputType.CHOOSE_ROOM_TO_BLOCK
    elif possibleServerOutput == CHOOSE_EXIT_FROM_ROOM_TO_BLOCK_SERVER_ASK:
        return ServerOutputType.CHOOSE_EXIT_FROM_ROOM_TO_BLOCK
    elif possibleServerOutput == CHOOSE_ROOM_TO_SHADOW_SERVER_ASK:
        return ServerOutputType.CHOOSE_ROOM_TO_SHADOW
    else:
        return ServerOutputType.NOT_IMPLEMENTED

def serverOutputToServerMessage(line):
    serverMessage = ServerMessage(ServerOutputType.NOT_IMPLEMENTED, 0, True) 
    for  serverAskArray in SERVER_ASK_WORD_ARRAY:
        if checkLineWith(serverAskArray, line) == True:
            serverOutput = serverOutputWordToENum(serverAskArray)
            if serverOutput == ServerOutputType.CHOOSE_CARD_TO_PLAY:
                serverMessage = ServerMessage(ServerOutputType.CHOOSE_CARD_TO_PLAY, getTilePosFromLine(line), True)
            elif serverOutput == ServerOutputType.TURN_INDICATION:
                serverMessage = ServerMessage(ServerOutputType.TURN_INDICATION, getPlayerToPlayFromLine(line), False)
            elif serverOutput == ServerOutputType.TURN_INFO:
                serverMessage =  ServerMessage(ServerOutputType.TURN_INFO,getTurnInfofromLine(line), True)
            elif serverOutput == ServerOutputType.ENABLE_POWER:
                serverMessage = ServerMessage(ServerOutputType.ENABLE_POWER, [0, 1], True)
            elif serverOutput == ServerOutputType.CHOOSE_POSITION:
                serverMessage = ServerMessage(ServerOutputType.CHOOSE_POSITION, getPositionFromLine(line), True)
            elif serverOutput == ServerOutputType.CHOOSE_ROOM_TO_BLOCK:
                serverMessage = ServerMessage(ServerOutputType.CHOOSE_ROOM_TO_BLOCK, range(10), True)
            elif serverOutput == ServerOutputType.CHOOSE_EXIT_FROM_ROOM_TO_BLOCK:
                serverMessage = ServerMessage(ServerOutputType.CHOOSE_EXIT_FROM_ROOM_TO_BLOCK, getPositionFromLine(line), True)
            elif serverOutput == ServerOutputType.CHOOSE_ROOM_TO_SHADOW:
                serverMessage = ServerMessage(ServerOutputType.CHOOSE_ROOM_TO_SHADOW, range(10), True)
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
            
    
    def serverMessageToServerInput(self, iAMessage):
        if iAMessage.messageType == ServerInputType.CHOOSE_CARD_TO_PLAY:
            self.writeNumberResponse(serverMessage.content)
        elif IAMessage.messageType == ServerInputType.ENABLE_POWER:
            if IAMessage.content == True:
                self.writeNumberResponse(1)
            else:
                self.writeNumberResponse(0)
        elif IAMessage.messageType == ServerInputType.CHOOSE_POSITION or IAMessage.messageType == CHOOSE_ROOM_TO_BLOCK or IAMessage.messageType == CHOOSE_EXIT_FROM_ROOM_TO_BLOCK or IAMessage.messageType ==  CHOOSE_ROOM_TO_SHADOW:
            self.writeNumberResponse(serverMessage.content)
        elif IAMessage.messageType == ServerInputType.CHOOSE_COLOR:
            self.writeStringResponse(serverMessage.content)
        else:
            self.writeNumberResponse(0)    

    def writeNumberResponse(self, number):
        rf = open(self.serverInputfilePath,'w')
        rf.write(str(number))
        rf.close()

    def writeStringResponse(self, stringToWrite):
        rf = open(self.serverInputfilePath,'w')
        rf.write(stringToWrite)
        rf.close()



    def deserialize(self, iAMessage):
        print("[deserialize] deserialize : start deserialize")
        self.serverMessageToServerInput(iAMessage)
