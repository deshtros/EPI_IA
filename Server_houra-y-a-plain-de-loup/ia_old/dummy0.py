from random import randrange

def lancer():
    fini = False
    old_question = ""
    while not fini:
        qf = open('./0/questions.txt','r')
        question = qf.read()
        qf.close()
        if question != old_question :
            rf = open('./0/reponses.txt','w')
            rf.write(str(randrange(2)))
            rf.close()
            old_question = question
        infof = open('./0/questions.txt','r')
        fini = "Score" in infof
        infof.close()